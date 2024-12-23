# Download Files from S3 Bucket to Local Folder

This script allows you to download files from an AWS S3 bucket to a local folder, optionally filtering by a prefix. It is useful for downloading a set of files from a specific folder (prefix) in an S3 bucket to your local filesystem.

## Prerequisites

### 1. Install AWS-CLI Tool
To fetch data via the script, you need the AWS CLI Tool, so go get it!

#### AWS OWN DOCUMENATION:
[How to install AWS-CLI Tool](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

#### Basically this...

If you have sudo permissions, you can install the AWS CLI for all users on the computer. We provide the steps in one easy to copy and paste group. See the descriptions of each line in the following steps.

```bash
$ curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
$ sudo installer -pkg AWSCLIV2.pkg -target /
```
#### Guided installation instructions
Download the file using the curl command. The -o option specifies the file name that the downloaded package is written to. In this example, the file is written to AWSCLIV2.pkg in the current folder.

```bash
$ curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
```

```bash
$ sudo installer -pkg ./AWSCLIV2.pkg -target /
```

To verify that the shell can find and run the aws command in your $PATH, use the following commands.

```bash
$ which aws
```
should output /usr/local/bin/aws 

```bash
$ aws --version
```
should output aws-cli/2.19.1 Python/3.11.6 Darwin/23.3.0 botocore/2.4.5

If the aws command cannot be found, you might need to restart your terminal or follow the troubleshooting in Troubleshooting errors for the AWS CLI.

### 2. Install Required Libraries
This script uses the `boto3` library to interact with AWS S3. Install the required library by running:

```bash
pip install boto3
```

### 3. Configure AWS Credentials
To access the S3 bucket, you need to configure AWS credentials on your system. You can do this by setting up the `~/.aws/credentials` file or using environment variables. Use the AWS CLI to configure credentials:

```bash
aws configure
```

Alternatively, set the following environment variables:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

## How to Run the Script
#### Run the Script
Use the command-line interface to run the script. The script requires the following arguments:

- `bucket`: Name of the S3 bucket
- `folder`: Path to the local folder where files will be downloaded
- `--prefix` (optional): Prefix to filter files in the S3 bucket

#### Examples

1. **Download all files from a bucket:**

```bash
python download_from_s3.py my-s3-bucket /path/to/destination/folder
```

2. **Download files with a specific prefix:**

```bash
python download_from_s3.py my-s3-bucket /path/to/destination/folder --prefix my-folder/sub-folder
```

### Step 3: Verify the Download
After the script completes, check the specified local folder to ensure all files have been downloaded correctly.

## Error Handling
The script includes error handling for the following scenarios:

1. **Missing AWS Credentials:**
   If AWS credentials are not found, you will see the error:
   
   ```
   Error: AWS credentials not found.
   ```

2. **Incomplete AWS Credentials:**
   If the credentials are incomplete, you will see the error:

   ```
   Error: Incomplete AWS credentials.
   ```

3. **General Errors:**
   For any other unexpected errors, a message will be displayed with the exception details.
