
# Single log generator code
# Author: Chaney Finkeldei
# Created: 9/30/2026
# Last updated: 9/30/2026

# This code crates a log of files that have been uploaded to the azure blob 

# Import packages
import csv
import os
from azure.storage.blob import BlobServiceClient

# connect to the blob

# Login details for blob
connection_string = ${{ secrets.AZURE_CONNECTION_STRING}}

container_name = "field-data"

# Directory where files are located
log_file_path = "D:/Data/data_log"

# write a function to create the log

def create_log():

    # Connect to Blob
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

     # Load existing paths
    existing_paths = set()
    file_exists = os.path.exists(log_file_path) and os.path.getsize(log_file_path) > 0
    
    if file_exists(log_file_path):
        with open(log_file_path, mode = "r", newline = "", encoding = "utf-8") as f:
            reader = csv.reader(f)

            #skip header
            header = next(reader, None)
            for row in reader:
                if row:
                    existing_paths.add(row[0])

    new_enteries_count = 0

    #
    with open(log_file_path, mode = "a", newline = "", encoding = "utf-8") as f:
        writer = csv.writer(f)

        # Write header if creating a new file
        if not file_exists:
            writer.writerow(["relative_path","current_time"])

         # Grab all the blob names
        blob_list = container_client.list_blobs()

        for blob in blob_list:

            # Set relative path
            relative_path = blob.name.replace("\\" , "/")

            # Log blob path
            if relative_path not in existing_paths:
                timestamp = blob.creation_time.strftime("%Y-%m-%d %H:%M:%S")

                writer.writerow([relative_path, timestamp])
                existing_paths.add(relative_path)
                new_enteries_count += 1

    
    print(f"{new_enteries_count} existing files were added to the log ")


if __name__ == "__maine__":
    create_log()