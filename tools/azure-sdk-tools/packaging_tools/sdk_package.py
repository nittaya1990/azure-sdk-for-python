import sys
import argparse
import json
import logging
import os
from pathlib import Path
from subprocess import check_call

from .package_utils import create_package, change_log_generate, extract_breaking_change

logging.basicConfig(
    stream=sys.stdout,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %X",
)
_LOGGER = logging.getLogger(__name__)


def main(generate_input, generate_output):
    with open(generate_input, "r") as reader:
        data = json.load(reader)
        _LOGGER.info(f"auto_package input: {data}")

    sdk_folder = "."
    result = {"packages": []}
    for package in data.values():
        package_name = package["packageName"]
        prefolder = package["path"][0]
        # Changelog
        last_version = ["first release"]
        try:
            md_output = change_log_generate(
                package_name,
                last_version,
                package["tagIsStable"],
                prefolder=prefolder,
                is_multiapi=package["isMultiapi"],
            )
        except:
            md_output = "change log generation failed!!!"
        package["changelog"] = {
            "content": md_output,
            "hasBreakingChange": "Breaking Changes" in md_output,
            "breakingChangeItems": extract_breaking_change(md_output),
        }
        package["version"] = last_version[-1]

        _LOGGER.info(f"[PACKAGE]({package_name})[CHANGELOG]:{md_output}")
        # Built package
        create_package(prefolder, package_name)
        folder_name = package["path"][0]
        dist_path = Path(sdk_folder, folder_name, package_name, "dist")
        package["artifacts"] = [str(dist_path / package_file) for package_file in os.listdir(dist_path)]
        package["result"] = "succeeded"
        # Generate api stub File
        try:
            package_path = Path(sdk_folder, folder_name, package_name)
            check_call(
                [
                    "python",
                    "-m" "pip",
                    "install",
                    "-r",
                    "../../../eng/apiview_reqs.txt",
                    "--index-url=https://pkgs.dev.azure.com/azure-sdk/public/_packaging/azure-sdk-for-python/pypi"
                    "/simple/",
                ],
                cwd=package_path,
                timeout=600,
            )
            check_call(["apistubgen", "--pkg-path", "."], cwd=package_path, timeout=600)
            for file in os.listdir(package_path):
                if "_python.json" in file and package_name in file:
                    package["apiViewArtifact"] = str(Path(package_path, file))
        except Exception as e:
            _LOGGER.info(f"Fail to generate ApiView token file for {package_name}: {e}")
        # Installation package
        package["installInstructions"] = {
            "full": "You can install the use using pip install of the artifacts.",
            "lite": f"pip install {package_name}",
        }
        for artifact in package["artifacts"]:
            if ".whl" in artifact:
                package["language"] = "Python"
                break
        package["packageFolder"] = package["path"][0]
        result["packages"].append(package)

    with open(generate_output, "w") as writer:
        json.dump(result, writer)


def generate_main():
    """Main method"""

    parser = argparse.ArgumentParser(
        description="Build SDK using Autorest, offline version.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("generate_input", help="Generate input file path")
    parser.add_argument("generate_output", help="Generate output file path")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        help="Verbosity in INFO mode",
    )
    parser.add_argument("--debug", dest="debug", action="store_true", help="Verbosity in DEBUG mode")
    parser.add_argument(
        "-c",
        "--codegen",
        dest="debug",
        action="store_true",
        help="Verbosity in DEBUG mode",
    )

    args = parser.parse_args()
    main_logger = logging.getLogger()
    logging.basicConfig()
    main_logger.setLevel(logging.DEBUG if args.verbose or args.debug else logging.INFO)

    main(args.generate_input, args.generate_output)


if __name__ == "__main__":
    generate_main()
