# aws-allowlister

Automatically compile an AWS Service Control Policy that ONLY allows AWS services that are compliant with your selected frameworks. Supports SOC, PCI, HIPAA, and ISO.

## Installation

* This command sets up the virtual environment, builds the python package and installs the package so you can run it from command line.

```bash
make install
```

### Usage

* Generate an AllowList Policy using this command:

```bash
aws-allowlister generate
```

By default, it allows policies at the intersection of PCI, HIPAA, SOC, ISO.

The resulting policy will look like this:

```json
{
    "Version": "2012-10-17",
    "Statement": {
        "Sid": "AllowList",
        "Effect": "Deny",
        "NotAction": [
            "account:*",
            "acm:*",
            "amplify:*",
            "amplifybackend:*",
            "apigateway:*",
            "application-autoscaling:*",
            "appstream:*",
            "appsync:*",
            "athena:*",
            "autoscaling:*",
            "aws-portal:*",
            "backup:*",
            "batch:*",
            "clouddirectory:*",
            "cloudformation:*",
            "cloudfront:*",
            "cloudhsm:*",
            "cloudtrail:*",
            "cloudwatch:*",
            "codebuild:*",
            "codecommit:*",
            "codedeploy:*",
            "codepipeline:*",
            "cognito-identity:*",
            "cognito-idp:*",
            "comprehend:*",
            "comprehendmedical:*",
            "config:*",
            "connect:*",
            "dataexchange:*",
            "datasync:*",
            "directconnect:*",
            "dms:*",
            "ds:*",
            "dynamodb:*",
            "ebs:*",
            "ec2:*",
            "ecr:*",
            "ecs:*",
            "eks:*",
            "elasticache:*",
            "elasticbeanstalk:*",
            "elasticfilesystem:*",
            "elasticmapreduce:*",
            "es:*",
            "events:*",
            "execute-api:*",
            "firehose:*",
            "fms:*",
            "forecast:*",
            "freertos:*",
            "fsx:*",
            "glacier:*",
            "globalaccelerator:*",
            "glue:*",
            "greengrass:*",
            "guardduty:*",
            "health:*",
            "iam:*",
            "inspector:*",
            "iot:*",
            "iot-device-tester:*",
            "iotdeviceadvisor:*",
            "iotevents:*",
            "iotwireless:*",
            "kafka:*",
            "kinesis:*",
            "kinesisanalytics:*",
            "kinesisvideo:*",
            "kms:*",
            "lambda:*",
            "lex:*",
            "logs:*",
            "macie2:*",
            "mediaconnect:*",
            "mediaconvert:*",
            "medialive:*",
            "mq:*",
            "neptune-db:*",
            "opsworks-cm:*",
            "organizations:*",
            "outposts:*",
            "personalize:*",
            "polly:*",
            "qldb:*",
            "quicksight:*",
            "rds:*",
            "rds-data:*",
            "rds-db:*",
            "redshift:*",
            "rekognition:*",
            "robomaker:*",
            "route53:*",
            "route53domains:*",
            "s3:*",
            "sagemaker:*",
            "secretsmanager:*",
            "securityhub:*",
            "serverlessrepo:*",
            "servicecatalog:*",
            "shield:*",
            "sms:*",
            "sms-voice:*",
            "snowball:*",
            "sns:*",
            "sqs:*",
            "ssm:*",
            "sso:*",
            "sso-directory:*",
            "states:*",
            "storagegateway:*",
            "sts:*",
            "support:*",
            "swf:*",
            "textract:*",
            "transcribe:*",
            "transfer:*",
            "translate:*",
            "waf:*",
            "waf-regional:*",
            "wafv2:*",
            "workdocs:*",
            "worklink:*",
            "workspaces:*",
            "xray:*"
        ],
        "Resource": "*"
    }
}
```
### Arguments

`aws-allowlister` supports different arguments to generate fine-grained compliance focused Service Control Policy (SCP) AllowLists.

- `--soc`
- `--pci`
- `--hipaa`
- `--iso`

For example, to generate a PCI only Service Control Policy:

```
aws-allowlister generate --pci
```

## Contributing


### Setup

* Set up the virtual environment

```bash
# Set up the virtual environment
python3 -m venv ./venv && source venv/bin/activate
pip3 install -r requirements.txt
```

* Build the package

```bash
# To build only
make build

# To build and install
make install

# To run tests
make test

# To clean local dev environment
make clean
```


## TODO

* **Quality control of the SQLite database**: LGTM but need someone to do a quality check
* Documentation on building custom scrapers
* It covers ISO, PCI, HIPAA, SOC - but doesn't cover FedRAMP yet. Just needs a custom scraper for that.

## Disclaimer
The policies generated by `aws-allowlister` do not guarantee that your AWS accounts will be compliant or that you will become accredited with the supported compliance frameworks. These policies are intended to be a useful tool to assist with restricting which service can or cannot be leveraged.