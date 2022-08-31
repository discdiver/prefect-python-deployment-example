from demo import pipeline
from prefect.deployments import Deployment

deployment = Deployment.build_from_flow(
    flow=pipeline,
    name="Python Deployment Example",
)

if __name__ == "__main__":
    deployment.apply()
