# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from datetime import datetime
from dateutil.parser import parse
from testcase_async import FarmBeatsAsyncTestCase
from testcase import FarmBeatsPowerShellPreparer
from devtools_testutils.aio import recorded_by_proxy_async


class TestFarmBeatsSmokeAsync(FarmBeatsAsyncTestCase):
    @FarmBeatsPowerShellPreparer()
    @recorded_by_proxy_async
    async def test_party(self, **kwargs):
        agrifood_endpoint = kwargs.pop("agrifood_endpoint")
        client = self.create_client(agrifood_endpoint=agrifood_endpoint)

        party_id = "test-party-3957"

        party_request = {
            "name": "Test Party",
            "description": "Party created during testing.",
            "status": "Sample Status",
            "properties": {
                "foo": "bar",
                "numeric one": 1,
                1: "numeric key"
            }
        }

        # Setup client
        client = self.create_client(agrifood_endpoint=agrifood_endpoint)

        # Create
        party_response = await client.parties.create_or_update(
            party_id=party_id,
            party=party_request
        )

        # Assert on immediate response
        assert party_response["id"] == party_id
        assert party_response["name"] == party_response["name"]
        assert party_response["description"] == party_response["description"]
        assert party_response["status"] == party_response["status"]

        assert len(party_response["properties"]) == 3
        assert party_response["properties"]["foo"] == "bar"
        assert party_response["properties"]["numeric one"] == 1
        assert party_response["properties"]["1"] == "numeric key"

        assert party_response["eTag"]
        assert type(parse(party_response["createdDateTime"])) is datetime
        assert type(parse(party_response["modifiedDateTime"])) is datetime

        await client.parties.delete(party_id=party_id)
        await self.close_client()


    @FarmBeatsPowerShellPreparer()
    @recorded_by_proxy_async
    async def test_boundary(self, **kwargs):
        agrifood_endpoint = kwargs.pop("agrifood_endpoint")
        client = self.create_client(agrifood_endpoint=agrifood_endpoint)

        party_id = "smoke-test-party"
        boundary_id = "smoke-test-boundary"

        party_request = {
            "name": "Test Party",
            "description": "Party created during testing.",
            "status": "Sample Status",
            "properties": {
                "foo": "bar",
                "numeric one": 1,
                1: "numeric key"
            }
        }
        party = await client.parties.create_or_update(
            party_id=party_id,
            party=party_request
        )
        
        boundary = await client.boundaries.create_or_update(
            party_id=party_id,
            boundary_id=boundary_id,
            boundary={
                "geometry":
                {
                    "type": "Polygon",
                    "coordinates":
                        [
                            [
                                [73.70457172393799, 20.545385304358106],
                                [73.70457172393799, 20.545385304358106],
                                [73.70448589324951, 20.542411534243367],
                                [73.70877742767334, 20.541688176010233],
                                [73.71023654937744, 20.545083911372505],
                                [73.70663166046143, 20.546992723579137],
                                [73.70457172393799, 20.545385304358106],
                            ]
                        ]
                },
                "status": "<string>",
                "name": "<string>",
                "description": "<string>"
            }
        )

        assert boundary == await client.boundaries.get(
            party_id=party_id,
            boundary_id=boundary_id
        )
        await client.boundaries.delete(party_id=party_id, boundary_id=boundary_id)
        await client.parties.delete(party_id=party_id)

        await self.close_client()
