from addUser import AddUserToCognito
import json

def main():
    cognitoObject = AddUserToCognito()

    with open("data.json","r+") as file:
        data = file.read()

    if(data is None or data == ''):
        print("data.json is empty.")
        exit(0)

    data = json.loads(data)
    
    for user in data:
        cognitoObject.addUser(user)

if __name__ == '__main__':
    main()