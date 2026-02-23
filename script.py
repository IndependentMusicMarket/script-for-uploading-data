from google.cloud import storage
import os

def upload_to_bucket(bucket_name, source_file_path, destination_blob_name, credentials_path):
    """Uploads a file to the bucket using a specific JSON key file."""
    try:
        storage_client = storage.Client.from_service_account_json(credentials_path)
        
        bucket = storage_client.bucket(bucket_name)
        
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_path)

        print(f"Success: {source_file_path} uploaded to {bucket_name}/{destination_blob_name}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Configuration ---
KEY_FILE = './creddentials.json'
MY_BUCKET = 'subiekt-sales-data'
FILE_TO_UPLOAD = 'LOKALNY_PLIK_CSV.csv'
CLOUD_NAME = 'NAZWA_PLIKU_W_CHMURZE.csv'

if __name__ == "__main__":
    upload_to_bucket(MY_BUCKET, FILE_TO_UPLOAD, CLOUD_NAME, KEY_FILE)