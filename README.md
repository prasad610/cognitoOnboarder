# Auto import users with groups

A python project which allows the user to onboard multiple user to cognito with all user attribute as oppose to the selective attribute that the import job of cognito provides for mass onboarding.

## Dependencies

- Python 3.8
- boto3

## Installation

run `pip install -r requirements.txt`

## Usage

1. Edit the config.ini file with your values (Serial number is the arn of the mfa created on IAM user)

2. The file `data.json` should contains a list of JSON object with user details similar to mentioned below.

    ```JSON

    [
        {
            "userName":"username",
            "userAttribute":[
                {
                    "Name": "email",
                    "Value": "username@domain.com"
                },
                {
                    "Name": "name",
                    "Value": "user"
                },
                {
                    "Name": "email_verified",
                    "Value": "true"
                }
            ],
            "group":["group"]
        }
    ]

    ```

3. Execute main.py
