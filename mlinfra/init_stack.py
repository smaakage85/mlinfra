import aws_cdk as cdk
from aws_cdk import (
    aws_ecr as ecr,
    aws_s3 as s3,
    aws_iam as iam,
    aws_ec2 as ec2,
)
            
class InitStack(cdk.Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        artifact_bucket = s3.Bucket(
            self,
            "ArtifactBucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            bucket_name="smaakage-artifacts",
        )

        fireworks_repository = ecr.Repository(
            self, 
            "ImageRepository", 
            repository_name="smaakage",
        )