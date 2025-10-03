## Automated Data Pipeline using Airflow and Cloud Composer
## Project Summary


I built and automated a data pipeline using Google Cloud Composer (Apache Airflow). The objective was to automatically extract raw data, transform, and load it so that the analytics team could leverage it.


# Workflow

**A)** I wrote a Python script to generate and extract dummy employee data, which I then stored in Google Cloud Storage as the raw landing zone.


**B)** I used Cloud Data Fusion to clean and transform the employee dataset. This step involved standardizing fields, handling missing values, and preparing the data for downstream analysis.



**C)** After transformation, I loaded the clean employee data into BigQuery, which served as the central warehouse for analytics.


**D)** I connected Looker Studio to BigQuery and created a dashboard. One of the key reports I built was a pie chart showing the distribution of employees by department.


**E)** Finally, I automated the entire pipeline — from extraction to visualization — using Cloud Composer (Apache Airflow), ensuring the process runs seamlessly without manual intervention.



## Architecture Diagram

<img width="929" height="512" alt="PJCT drawio" src="https://github.com/user-attachments/assets/01a082fb-c152-4aad-ad07-541394a17079" />





## Cloud Data Fusion ETL pipeline




<img width="1920" height="976" alt="Screenshot 2025-09-28 145438" src="https://github.com/user-attachments/assets/8a7c7736-552d-463a-9818-d0a40e77edbf" />


## Airflow Automation 


<img width="1700" height="756" alt="Screenshot 2025-09-29 024134" src="https://github.com/user-attachments/assets/8d1d4dd0-0e13-46a8-93b0-3682aa38e511" />



## Visualization Report

<img width="1175" height="706" alt="Screenshot 2025-09-28 153033" src="https://github.com/user-attachments/assets/95e3a713-a417-4664-8131-b098befb5533" />

