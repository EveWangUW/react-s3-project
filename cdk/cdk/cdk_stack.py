from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_s3 as s3,
    aws_s3_deployment as s3_deployment
)

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        myBucket = s3.Bucket(
            self,
            id="bucket",
            versioned=True,
            website_index_document="index.html",
            access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL,
            public_read_access=True,
            encryption=s3.BucketEncryption.S3_MANAGED,
        )
        s3_deployment.BucketDeployment(
            self,
            id="bucketdeployment",
            sources=[s3_deployment.Source.asset("../frontend/build")],
            destination_bucket=myBucket
        )