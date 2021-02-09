import boto3
import configparser

class AddUserToCognito: 
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.variables = config["DEFAULT"]
        if ( self.variables.get("isMFA").lower()=="true" ):
            self.client = boto3.client('sts')
            self.client.get_session_token(
                DurationSeconds=int(self.variables.get("DURATION_SECONDS")),
                SerialNumber=self.variables.get("SERIAL_NUMBER"),
                TokenCode=input("Enter otp : ")
            )
        self.client = boto3.client('cognito-idp',
            region_name=self.variables.get("REGION"))

        availableGroups = self.client.list_groups(
            UserPoolId=self.variables.get("USERPOOL_ID")
        )
        self.availableGroups = [ groups["GroupName"] for groups in availableGroups["Groups"]]

    def addUser(self,user):

        if user["group"] not in self.availableGroups:
            print("Group {group} does not exist".format(group=user["group"]))
            return user

        try:
            self.client.admin_create_user(
                UserPoolId=self.variables.get("USERPOOL_ID"),
                Username=user["userName"],
                UserAttributes=user["userAttribute"]
            )
            self.addUserToGroups(user)
        except Exception as e:
            print(e.response["Error"])

    def addUserToGroups(self, user):       
        try:
            for group in user["group"]:
                self.client.admin_add_user_to_group(
                    UserPoolId=self.variables.get("USERPOOL_ID"),
                    Username=user["userName"],
                    GroupName=group
                )
        except Exception as e:
            print(e.response["Error"])
