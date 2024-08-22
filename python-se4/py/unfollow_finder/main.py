import instaloader
import getpass

from orca.settings import profile

file_old_followers = open("followers.txt", "r") # finding old followers
old_followers = []

for line in file_old_followers:
    old_followers.append(line)


file_old_followers.close()



l = instaloader.Instaloader() # login to instagram
username = input("Enter Your username:")
password = getpass.getpass("Enter your password:")
l.login(username, password)
print("we are login hooraaa!!!")
myProfile = instaloader.profile.from_username(l.context,"moein_fadakar")

new_followers = [] # getting new followers
for follower in  profile.get_follower():
    new_followers.append(follower)
for old_follower in old_followers:
    if old_follower not in new_followers:
        print(old_follower)


file = open("follwer.txt","w") # update followers list
for follower in new_followers:
    file.write(follower)

