# API Tech Demo

This is a repo of Fletcher's recommended API setup.

- FastAPI
- Django ORM
- PostgreSQL
- Redis

Feel free to download and mess around with this. Stuff in the `scripts` directory should make it easy to mess around with this locally.

This repo was designed to run on GCP's Cloud Run. Deploying to Cloud Build is fairly straightforward, but not documented here.

## Pre-Setup

The first two steps only apply if you're using this repo with GCP's Cloud Source Repositories.

1. Install [Cloud SDK](https://cloud.google.com/sdk/docs/quickstart)
    - Install cloud-sql-proxy with `gcloud components install cloud_sql_proxy`
    - Login with `gcloud init`
    - Check your config with `gcloud config list`
2. Set up the local repository
    - Clone the repository with `gcloud source repos clone api_tech_demo --project=${project id}`
    - Enter the repository with `cd api_tech_demo`
3. Set up virtual environment
    - Create the environment with `conda env create -f environment.yml`
    - Enter the environment with `conda activate API-Tech-Demo`
    - In PyCharm, open the project and set the project interpreter

## Other Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Local Development

Various scripts are provided for you to use for common operations. These scripts are located in the `scripts` directory, and includes...

- Linting and type-checking the codebase (`lint.sh`)
- Initial setup of your containers (`setup_containers.sh`)
- Final teardown of your containers (`teardown_containers.sh`)
    - WARNING - This will remove any volumes associated with your containerized database(s), so you'll lose any local test data you've put into the database
- Starting your containers (`start_containers.sh`)
- Stopping your containers (`stop_containers.sh`)
- Running database migrations (`run_migrations.sh`)
- Running tests (`test.sh`)

While these scripts cover enough functionality to get started, you'll likely want to create your own scripts for automating any common operations. Feel free to ask @Fletcher Easton  for assistance with this, or if you want an opinion on how your script should look and/or operate.

### PyCharm Setup

- Install the Pydantic plugin for PyCharm
- Enable Django Support (**Settings | Languages & Frameworks | Django**)
    - Select `/api_tech_demo/app` as the project root