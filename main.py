from addUser import AddUserToCognito
from excel2JSON import Excel2JSON
import json
import getopt
import sys
class Main:
    def __init__(self,arguments):
        self.options = {"useJSON":None}

        try:
            option, args = getopt.getopt(args=arguments[1:], shortopts="j", longopts=["json"])
            for name,value in option:
                if name in ["-j","--json"]:
                    self.options["useJSON"] = True

        except Exception as e: 
            with open("error.log","w+") as file:
                file.write(e.__str__())
            print("Error Occured {e}. For more detail read error.log".format(e=e.__cause__()))
        pass

    def addUserFromJSON(self):
        cognitoObject = AddUserToCognito()

        with open("data.json","r+") as file:
            data = file.read()

        if(data is None or data == ''):
            print("data.json is empty.")
            exit(0)

        data = json.loads(data)
        failedUser = []
        for user in data:
            failedUser.append(cognitoObject.addUser(user))
        with open("failedUser","w+") as file:
            json.dump(failedUser,fp=file)

    def excel2JSON(self):
        Excel2JSON()
        self.addUserFromJSON()

    def main(self):
        if self.options["useJSON"]:
            self.addUserFromJSON()
        else:
            self.excel2JSON()
        pass

if __name__ == '__main__':
    main = Main(sys.argv)
    main.main()
