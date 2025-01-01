import boto3
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def download_from_s3(bucket_name, local_folder, s3_prefix=""):
    """
    Download files from an S3 bucket to a local folder.

    :param bucket_name: Name of the source S3 bucket.
    :param local_folder: Path to the local folder where files will be downloaded.
    :param s3_prefix: Prefix to filter files in the S3 bucket (optional).
    :return: True if all files were downloaded successfully, False otherwise.
    """
    s3_client = boto3.client('s3')

    try:
        # Ensure the local folder exists
        if not os.path.exists(local_folder):
            os.makedirs(local_folder)

        # List all objects in the bucket under the specified prefix
        paginator = s3_client.get_paginator('list_objects_v2')
        operation_parameters = {'Bucket': bucket_name, 'Prefix': s3_prefix}
        for page in paginator.paginate(**operation_parameters):
            if 'Contents' not in page:
                print("No files found with the given prefix.")
                return False

            for obj in page['Contents']:
                s3_key = obj['Key']
                relative_path = os.path.relpath(s3_key, s3_prefix)
                local_path = os.path.join(local_folder, relative_path)

                # Create subdirectories if necessary
                local_dir = os.path.dirname(local_path)
                if not os.path.exists(local_dir):
                    os.makedirs(local_dir)

                # Download the file
                print(f"Downloading {s3_key} to {local_path}...")
                s3_client.download_file(bucket_name, s3_key, local_path)

        print("All files downloaded successfully.")
        return True
    except NoCredentialsError:
        print("Error: AWS credentials not found.")
        return False
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False


if __name__ == "__main__":
    import argparse

    # Set up command-line arguments
    parser = argparse.ArgumentParser(description="Download files from an S3 bucket to a local folder.")
    parser.add_argument("bucket", help="Name of the S3 bucket")
    parser.add_argument("folder", help="Path to the local folder where files will be downloaded")
    parser.add_argument("--prefix", help="Prefix to filter files in the S3 bucket (optional)", default="")

    args = parser.parse_args()

    # Download files
    success = download_from_s3(args.bucket, args.folder, args.prefix)
    if success:
        print("Download completed successfully.")
    else:
        print("Download failed.")
