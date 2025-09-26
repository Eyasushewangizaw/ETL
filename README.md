## Automated Data Pipeline using Airflow and Cloud Composer
# Project Summary


I built and automated a data pipeline using Google Cloud Composer (Apache Airflow). The objective was to automatically extract raw data, transform, and load it so that the analytics team could leverage it.


# Workflow


I wrote some Python code to connect to the data source, retrieve the data, and save it to Cloud Storage.


The Cloud Data Fusion service processes and transforms the data.


The clean data is then loaded into BigQuery as the main data warehouse.


I connected Looker to BigQuery for the purposes of reporting and dashboards.


I used Cloud Composer (Airflow) to orchestrate the whole workflow and schedule all the extraction, loading, transformation, and dashboard refresh in an automated fashion.


<img width="929" height="512" alt="PJCT drawio" src="https://github.com/user-attachments/assets/01a082fb-c152-4aad-ad07-541394a17079" />

