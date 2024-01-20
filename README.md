# Airflow-project

In this project, we extracted the data from a csv file and then did trasformation (removing null and duplicate values) on the dataframe using Pandas. We then, created a DAG using Airflow and scheduled our ETL task through it. At the result stage, our Airflow DAG will write the data into Amazon S3 server.
