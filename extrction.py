from faker import Faker
import pandas as pd
import random
from google.cloud import storage
from google.oauth2 import service_account

# -------------------------------
# Configuration
# -------------------------------
CREDENTIALS_PATH = r"C:\ETL2\eyasuproject-e8cac136bbf0.json"  # Path to your GCP service account JSON
BUCKET_NAME = "originalbuck"
DESTINATION_BLOB_NAME = "dummy_employees1.csv"  # Name in GCS

# Initialize Faker
fake = Faker()

# Number of dummy records to generate
NUM_RECORDS = 40

# -------------------------------
# Generate dummy employee data
# -------------------------------
def generate_employee():
    return {
        "EmployeeID": fake.unique.random_int(min=1000, max=9999),
        "FirstName": fake.first_name(),
        "LastName": fake.last_name(),
        "Email": fake.email(),
        "Nationality": fake.country(),
        "address": fake.city(),
        "PhoneNumber": fake.phone_number(),
        "DateOfBirth": fake.date_of_birth(minimum_age=18, maximum_age=65),
        "Department": random.choice(["HR", "IT", "Finance", "Marketing", "Sales"]),
        "Salary": round(random.uniform(40000, 120000), 2),
    }

employees = [generate_employee() for _ in range(NUM_RECORDS)]
df = pd.DataFrame(employees)

# Save locally
local_file = "dummy_employees1.csv"
df.to_csv(local_file, index=False)
print(f"Dummy employee data saved locally to '{local_file}'")

# -------------------------------
# Upload to GCS
# -------------------------------
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    # Authenticate
    credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH)
    client = storage.Client(credentials=credentials)
    
    # Get bucket and blob
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    
    # Upload file
    blob.upload_from_filename(source_file_name)
    print(f"File uploaded to gs://{bucket_name}/{destination_blob_name}")

# Call upload
upload_to_gcs(BUCKET_NAME, local_file, DESTINATION_BLOB_NAME)
