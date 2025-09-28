## Automated Data Pipeline using Airflow and Cloud Composer
# Project Summary


I built and automated a data pipeline using Google Cloud Composer (Apache Airflow). The objective was to automatically extract raw data, transform, and load it so that the analytics team could leverage it.


# Workflow


1. I wrote a Python script to extract data and store it in Cloud Storage.


2. The data is processed and transformed in Cloud Data Fusion.

3. Clean data is loaded into BigQuery as the central warehouse.

4. Looker is connected to BigQuery for reporting and dashboards.

5. I used Cloud Composer (Airflow) to orchestrate the whole workflow and schedule all the extraction, loading, transformation, and dashboard refresh in an automated fashion.


<img width="929" height="512" alt="PJCT drawio" src="https://github.com/user-attachments/assets/01a082fb-c152-4aad-ad07-541394a17079" />

