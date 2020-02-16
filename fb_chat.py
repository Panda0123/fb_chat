import fbchat
from fbchat import Client
from accounts import getPass
from accounts import getUserName
from accounts import getSendTo


def main():
    ps = getPass()
    userName = getUserName()
    client = fbchat.Client(userName, ps)

    friends = client.searchForUsers(getSendTo())
    friend = friends[0]
    msg = "Wassup mamen"
    response = client.send(fbchat.models.Message(msg), friend.uid)
    if response:
        print("Sended sucessfully")

def sendMsg(msg):
    ps = getPass()
    userName = getUserName()
    client = fbchat.Client(userName, ps)

    friends = client.searchForUsers(getSendTo())
    friend = friends[0]
    response = client.send(fbchat.models.Message(msg), friend.uid)
    if response:
        print("Sended sucessfully")


if __name__ == "__main__":
    main()
