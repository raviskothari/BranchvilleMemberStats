import boto3
import botocore

S3_BUCKET_NAME = "branchville-ems-stats"
S3_REGION = "us-east-2"


class S3:
    @staticmethod
    def download_from_s3(file_to_download, local_file_to_save_as):
        s3 = boto3.resource("s3")
        try:
            s3.Bucket(S3_BUCKET_NAME).download_file(file_to_download, local_file_to_save_as)
        except botocore.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("The object does not exist.")
            else:
                return
