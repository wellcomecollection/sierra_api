import boto3

from .client import SierraClient


def get_aws_session(*, role_arn):
    sts_client = boto3.client("sts")
    assumed_role_object = sts_client.assume_role(
        RoleArn=role_arn, RoleSessionName="AssumeRoleSession1"
    )
    credentials = assumed_role_object["Credentials"]
    return boto3.Session(
        aws_access_key_id=credentials["AccessKeyId"],
        aws_secret_access_key=credentials["SecretAccessKey"],
        aws_session_token=credentials["SessionToken"],
    )


def catalogue_client():
    sess = get_aws_session(role_arn="arn:aws:iam::760097843905:role/platform-developer")

    secrets_client = sess.client("secretsmanager")

    sierra_api_root = "https://libsys.wellcomelibrary.org/iii/sierra-api/v6"
    sierra_client_key = secrets_client.get_secret_value(
        SecretId="sierra_adapter/sierra_api_key"
    )["SecretString"]
    sierra_client_secret = secrets_client.get_secret_value(
        SecretId="sierra_adapter/sierra_api_client_secret"
    )["SecretString"]

    return SierraClient(
        api_url=sierra_api_root,
        oauth_key=sierra_client_key,
        oauth_secret=sierra_client_secret,
    )


def identity_client():
    sess = get_aws_session(role_arn="arn:aws:iam::770700576653:role/identity-developer")

    secrets_client = sess.client("secretsmanager")

    sierra_api_root = "https://libsys.wellcomelibrary.org/iii/sierra-api/v6"

    credentials = json.loads(
        secrets_client.get_secret_value(SecretId="sierra-api-credentials-prod")[
            "SecretString"
        ]
    )

    sierra_client_key = credentials["SierraAPIKey"]
    sierra_client_secret = credentials["SierraAPISecret"]

    return SierraClient(
        api_url=sierra_api_root,
        oauth_key=sierra_client_key,
        oauth_secret=sierra_client_secret,
    )
