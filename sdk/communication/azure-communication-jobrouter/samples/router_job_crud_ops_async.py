# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: router_job_crud_ops_async.py
DESCRIPTION:
    These samples demonstrates how to create Job used in ACS JobRouter.
    You need a valid connection string to an Azure Communication Service to execute the sample

USAGE:
    python router_job_crud_ops_async.py
    Set the environment variables with your own values before running the sample:
    1) AZURE_COMMUNICATION_SERVICE_CONNECTION_STRING - Communication Service connection string
"""

import os
import asyncio


class RouterJobSamplesAsync(object):
    connection_string = os.environ["AZURE_COMMUNICATION_SERVICE_CONNECTION_STRING"]

    _job_id = "sample_job"
    _job_w_cp_id = "sample_job_w_cp"
    _job_scheduled_id = "sample_scheduled_job"
    _assignment_id = "sample_assignment"
    _distribution_policy_id = "sample_distribution_policy"
    _classification_policy_id = "sample_classification_policy"
    _queue_id = "sample_queue"
    _worker_id = "sample_worker"

    async def setup_distribution_policy(self):
        connection_string = self.connection_string
        distribution_policy_id = self._distribution_policy_id

        from azure.communication.jobrouter.aio import JobRouterAdministrationClient
        from azure.communication.jobrouter.models import LongestIdleMode, DistributionPolicy

        router_admin_client = JobRouterAdministrationClient.from_connection_string(conn_str=connection_string)
        print("JobRouterAdministrationClient created successfully!")

        async with router_admin_client:
            dist_policy = await router_admin_client.upsert_distribution_policy(
                distribution_policy_id,
                DistributionPolicy(
                    offer_expires_after_seconds=10 * 60,
                    mode=LongestIdleMode(min_concurrent_offers=1, max_concurrent_offers=1),
                ),
            )

    async def setup_queue(self):
        connection_string = self.connection_string
        queue_id = self._queue_id
        from azure.communication.jobrouter.aio import JobRouterAdministrationClient
        from azure.communication.jobrouter.models import RouterQueue

        router_admin_client = JobRouterAdministrationClient.from_connection_string(conn_str=connection_string)

        async with router_admin_client:
            job_queue: RouterQueue = await router_admin_client.upsert_queue(
                queue_id, RouterQueue(distribution_policy_id=self._distribution_policy_id)
            )

    async def setup_classification_policy(self):
        connection_string = self.connection_string
        classification_policy_id = self._classification_policy_id

        from azure.communication.jobrouter.aio import JobRouterAdministrationClient
        from azure.communication.jobrouter.models import (
            StaticRouterRule,
            StaticQueueSelectorAttachment,
            RouterQueueSelector,
            LabelOperator,
            ClassificationPolicy,
        )

        router_admin_client = JobRouterAdministrationClient.from_connection_string(conn_str=connection_string)
        print("JobRouterAdministrationClient created successfully!")

        async with router_admin_client:
            classification_policy = await router_admin_client.upsert_classification_policy(
                classification_policy_id,
                ClassificationPolicy(
                    prioritization_rule=StaticRouterRule(value=10),
                    queue_selector_attachments=[
                        StaticQueueSelectorAttachment(
                            queue_selector=RouterQueueSelector(
                                key="Id", label_operator=LabelOperator.EQUAL, value=self._queue_id
                            )
                        )
                    ],
                ),
            )

    async def setup_worker(self):
        connection_string = self.connection_string
        worker_id = self._worker_id
        queue_id = self._queue_id

        from azure.communication.jobrouter.aio import JobRouterClient
        from azure.communication.jobrouter.models import RouterChannel, RouterWorker

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        async with router_client:
            router_worker = await router_client.upsert_worker(
                worker_id,
                RouterWorker(
                    capacity=100,
                    available_for_offers=True,
                    channels=[RouterChannel(channel_id="general", capacity_cost_per_job=1)],
                    queues=[queue_id],
                ),
            )

    async def create_job(self):
        connection_string = self.connection_string
        job_id = self._job_id
        job_w_cp_id = self._job_w_cp_id
        scheduled_job_id = self._job_scheduled_id
        queue_id = self._queue_id
        classification_policy_id = self._classification_policy_id

        # [START create_job_async]
        from datetime import datetime, timedelta
        from azure.communication.jobrouter.models import RouterJob, ScheduleAndSuspendMode
        from azure.communication.jobrouter.aio import (
            JobRouterClient,
        )

        # set `connection_string` to an existing ACS endpoint
        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)
        print("JobRouterAdministrationClient created successfully!")

        async with router_client:
            # We need to create a distribution policy + queue as a pre-requisite to start creating job
            router_job = await router_client.upsert_job(
                job_id,
                RouterJob(channel_id="general", queue_id=queue_id, priority=10, channel_reference="12345"),
            )

            print(f"Job has been successfully created with status: {router_job.status}")

            # Alternatively, a job can also be created while specifying a classification policy
            # As a pre-requisite, we would need to create a classification policy first
            router_job_with_cp = await router_client.upsert_job(
                job_w_cp_id,
                RouterJob(
                    channel_id="general", classification_policy_id=classification_policy_id, channel_reference="12345"
                ),
            )
            print(f"Job has been successfully created with status: {router_job_with_cp.status}")

            # Additionally, any job can be created as a scheduled job
            # by simply specifying a scheduled_time_utc and setting unavailable_for_matching to true
            router_scheduled_job = await router_client.upsert_job(
                scheduled_job_id,
                RouterJob(
                    channel_id="general",
                    queue_id=queue_id,
                    priority=10,
                    channel_reference="12345",
                    matching_mode=ScheduleAndSuspendMode(schedule_at=datetime.utcnow() + timedelta(0, 30)),
                ),
            )
            print(f"Scheduled job has been successfully created with status: {router_scheduled_job.status}")

        # [END create_job_async]

    async def update_job(self):
        connection_string = self.connection_string
        job_id = self._job_id
        # [START update_job_async]
        from azure.communication.jobrouter.aio import (
            JobRouterClient,
        )

        # set `connection_string` to an existing ACS endpoint
        router_client: JobRouterClient = JobRouterClient.from_connection_string(conn_str=connection_string)
        print("JobRouterAdministrationClient created successfully!")

        async with router_client:
            update_job = await router_client.upsert_job(job_id, channel_reference="45678")

            print(f"Job has been successfully update with channel reference: {update_job.channel_reference}")
        # [END update_job_async]

    async def get_job(self):
        connection_string = self.connection_string
        job_id = self._job_id
        # [START get_job_async]
        from azure.communication.jobrouter.aio import JobRouterClient

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        async with router_client:
            router_job = await router_client.get_job(job_id)

            print(f"Successfully fetched router worker with id: {router_job.id}")
        # [END get_job_async]

    async def get_job_position(self):
        connection_string = self.connection_string
        job_id = self._job_id
        # [START get_job_position_async]
        from azure.communication.jobrouter.aio import JobRouterClient

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        async with router_client:
            router_job_position = await router_client.get_queue_position(job_id)

            print(f"Successfully fetched router job position: {router_job_position.position}")
        # [END get_job_position_async]

    async def reclassify_job(self):
        connection_string = self.connection_string
        job_id = self._job_w_cp_id
        # [START reclassify_job_async]
        from azure.communication.jobrouter.aio import JobRouterClient

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        async with router_client:
            await router_client.reclassify_job(job_id)

            print(f"Successfully re-classified router")
        # [END reclassify_job_async]

    async def unassign_job(self):
        connection_string = self.connection_string
        job_id = self._job_w_cp_id
        assignment_id = self._assignment_id
        # [START unassign_job_async]
        from azure.communication.jobrouter.aio import JobRouterClient

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        unassign_job_result = await router_client.unassign_job(job_id, assignment_id)

        print(f"Successfully unassigned job")
        # [END unassign_job_async]

    async def accept_job_offer(self):
        connection_string = self.connection_string
        job_id = self._job_id
        worker_id = self._worker_id

        from azure.communication.jobrouter.aio import JobRouterClient
        from azure.communication.jobrouter.models import RouterJobOffer

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        async with router_client:

            offer_found = False
            while not offer_found:
                worker = await router_client.get_worker(worker_id=worker_id)
                if worker.offers and any(worker.offers):
                    for offer in worker.offers:
                        offer_found = True if offer.job_id == job_id else False

                if offer_found is False:
                    await asyncio.sleep(1)

            queried_worker = await router_client.get_worker(worker_id=worker_id)
            issued_offer: RouterJobOffer = [offer for offer in queried_worker.offers if offer.job_id == job_id][0]
            offer_id = issued_offer.offer_id

            # [START accept_job_offer_async]
            from azure.communication.jobrouter.models import RouterJob, AcceptJobOfferResult

            accept_job_offer_result: AcceptJobOfferResult = await router_client.accept_job_offer(
                worker_id=worker_id, offer_id=offer_id
            )

            queried_job: RouterJob = await router_client.get_job(job_id)

            print(f"Job has been successfully assigned to worker. Current job status: {queried_job.status}")
            print(
                f"Job has been successfully assigned with a worker with assignment "
                f"id: {accept_job_offer_result.assignment_id}"
            )
            # [END accept_job_offer_async]

            try:
                # [START decline_job_offer_async]
                from datetime import datetime, timedelta
                from azure.communication.jobrouter.models import DeclineJobOfferOptions

                await router_client.decline_job_offer(
                    worker_id,
                    offer_id,
                    DeclineJobOfferOptions(
                        retry_offer_at=datetime.utcnow() + timedelta(0, 30),  # re-offer after 30 secs
                    ),
                )

                # [END decline_job_offer_async]
            except Exception:
                print(f"Error encountered")

    async def complete_and_close_job(self):
        connection_string = self.connection_string
        job_id = self._job_id

        # [START complete_job_async]
        from azure.communication.jobrouter.aio import JobRouterClient
        from azure.communication.jobrouter.models import (
            RouterJob,
            CompleteJobOptions,
        )

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        async with router_client:
            queried_job: RouterJob = await router_client.get_job(job_id)

            assignment_id = [k for k, v in queried_job.assignments.items()][0]

            await router_client.complete_job(job_id, assignment_id, CompleteJobOptions(note="Complete job"))

            queried_job: RouterJob = await router_client.get_job(job_id)

            print(f"Job has been successfully completed. Current status: {queried_job.status}")
            # [END complete_job_async]

            # [START close_job_async]
            from azure.communication.jobrouter.models import (
                RouterJob,
                CloseJobOptions,
            )

            await router_client.close_job(job_id, assignment_id, CloseJobOptions(note="Close job"))

            queried_job: RouterJob = await router_client.get_job(job_id)

            print(f"Job has been successfully closed. Current status: {queried_job.status}")

        # [END close_job_async]

    async def list_jobs(self):
        connection_string = self.connection_string
        # [START list_jobs_async]
        from azure.communication.jobrouter.aio import JobRouterClient

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        async with router_client:
            router_job_iterator = router_client.list_jobs()

            async for j in router_job_iterator:
                print(f"Retrieved job with id: {j.id}")

            print(f"Successfully completed fetching jobs")
        # [END list_jobs_async]

    async def list_jobs_batched(self):
        connection_string = self.connection_string
        # [START list_jobs_batched_async]
        from azure.communication.jobrouter.aio import JobRouterClient

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        async with router_client:
            router_job_iterator = router_client.list_jobs(results_per_page=10)

            async for job_page in router_job_iterator.by_page():
                jobs_in_page = [i async for i in job_page]
                print(f"Retrieved {len(jobs_in_page)} jobs in current page")

                for j in jobs_in_page:
                    print(f"Retrieved job with id: {j.id}")

            print(f"Successfully completed fetching jobs")
        # [END list_jobs_batched_async]

    async def list_scheduled_jobs(self):
        connection_string = self.connection_string
        # [START list_scheduled_jobs_async]
        from datetime import datetime
        from azure.communication.jobrouter.aio import JobRouterClient

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        scheduled_before = datetime.utcnow()

        async with router_client:
            router_job_iterator = router_client.list_jobs(scheduled_before=scheduled_before, results_per_page=10)

            async for job_page in router_job_iterator.by_page():
                jobs_in_page = [i async for i in job_page]
                print(f"Retrieved {len(jobs_in_page)} jobs in current page")

                for j in jobs_in_page:
                    print(f"Retrieved job with id: {j.id}")

            print(f"Successfully completed fetching scheduled jobs")
        # [END list_scheduled_jobs_async]

    async def cancel_job(self):
        connection_string = self.connection_string
        job_id = self._job_w_cp_id

        # [START cancel_job_async]
        from azure.communication.jobrouter.aio import JobRouterClient

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        async with router_client:
            await router_client.cancel_job(id=job_id)

        # [END cancel_job_async]

    async def clean_up(self):
        connection_string = self.connection_string
        job_id = self._job_id

        # [START delete_job_async]
        from azure.communication.jobrouter.aio import JobRouterClient

        router_client = JobRouterClient.from_connection_string(conn_str=connection_string)

        async with router_client:
            await router_client.delete_job(job_id)

            # [END delete_job_async]

            await router_client.cancel_job(self._job_w_cp_id)
            await router_client.delete_job(self._job_w_cp_id)
            await router_client.cancel_job(self._job_scheduled_id)
            await router_client.delete_job(self._job_scheduled_id)
            await router_client.delete_worker(self._worker_id)

        from azure.communication.jobrouter.aio import JobRouterAdministrationClient

        router_admin_client = JobRouterAdministrationClient.from_connection_string(conn_str=connection_string)
        async with router_admin_client:
            await router_admin_client.delete_classification_policy(self._classification_policy_id)
            await router_admin_client.delete_queue(self._queue_id)
            await router_admin_client.delete_distribution_policy(self._distribution_policy_id)


async def main():
    sample = RouterJobSamplesAsync()
    await sample.setup_distribution_policy()
    await sample.setup_queue()
    await sample.setup_classification_policy()
    await sample.setup_worker()
    await sample.create_job()
    await sample.get_job()
    await sample.update_job()
    await sample.reclassify_job()
    await sample.get_job_position()
    await sample.accept_job_offer()
    await sample.complete_and_close_job()
    await sample.list_jobs()
    await sample.list_jobs_batched()
    await sample.list_scheduled_jobs()
    await sample.clean_up()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
