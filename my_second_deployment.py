from demo import pipeline2
from prefect.deployments import Deployment
from prefect.filesystems import S3
from prefect.orion.schemas.schedules import IntervalSchedule

deployment2 = Deployment.build_from_flow(
    flow=pipeline2,
    name="Second Python Deployment Example",
    schedule=(IntervalSchedule(interval=60)),
    tags=["extract"],
    storage=S3.load("dev"),
)

if __name__ == "__main__":
    deployment2.apply()
