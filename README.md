# Airflow 101

This is a repository that includes the files used for a 101 talk on a PyAr
meetup, 21/03/2019.

The slides used can be found on [this folder](https://www.github.com/gonzalezzfelipe/airflow_101/tree/master/slides).

### Requirements

This code was made to run on `python3.6`, it is recommended to build it on a
virtualenv. If you wish to do so, do the following:

```shell
pip3.6 install virtualenv
virtualenv ~/airflow_101_venv -p python3.6
source ~/airflow_101_venv/bin/activate
sh airflow_101.sh
```

---
### Running the examples

To run the local examples, execute the following on your shell:

```shell
sh airflow_101.sh
```
To run the docker examples, make sure you have `docker` and `docker-compose`
installed and the daemon up, then execute:

```shell
cd docker_test
sh docker_test.sh
```
---
