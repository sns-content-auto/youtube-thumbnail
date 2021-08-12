# youtube-thumbnail

# How to run this app?
## First please check if Docker is installed on your PC
For Windows users:
Please first install [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install-win10) if you don't have it installed.

## Initial Running
1. `docker-compose up --build -d`
1. `bash django_setup.sh`
1. There should now be three servers running:
  - [http://127.0.0.1:8000](http://127.0.0.1:8000) is the Django app
  - [http://127.0.0.1:3000](http://127.0.0.1:3000) is the React app
  - [http://127.0.0.1:3306](http://127.0.0.1:3306) is the MySQL Database

## Checking working containers
  - `docker-compose ps`

## Closing(must include -v)
  - `docker-compose down -v`

## Rerunning(without build/rerun django setup file)
  - `docker-compose up -d`
  - `bash django_setup.sh`