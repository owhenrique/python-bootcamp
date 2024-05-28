import sys
from user import User

def main():
    user = User("Paulo", "paulo@mail.com")
    #print(f"ID: {user.getId()}, NAME: {user.getName()}, EMAIL: {user.getEmail()}")
    print(vars(user))
    user.updateName("Paulo Henrique")
    #print(f"ID: {user.getId()}, NAME: {user.getName()}, EMAIL: {user.getEmail()}")
    print(vars(user))
if __name__ == '__main__':
    sys.exit(main())