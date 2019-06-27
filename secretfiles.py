#You need to find the secret username and password in order to access these secret

from usernameandpassword import username1
from usernameandpassword import password1

print("You need to vim this file and edit the code in order for it to execute")
username = input("username: ")
password = input("password: ")



#uncomment the lines below to execute the commad
if username == username1 and password == password1:
    import subprocess
    import os

    os.system('"C:/Users/jlvel/Desktop/username.txt"')


# from secretusername import secretpassword2
#   print(secretpassword2)
else:
   print("Unsuccesful login")


