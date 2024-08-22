old_followers_list = []
new_followers_list = []



old_followers = open("old_follower.txt","r")

read_old_followers_list = old_followers.readlines()

old_followers_list.append(read_old_followers_list)

old_followers.close()



new_followers = open("new_follower.txt","r")

read_new_followers_list = new_followers.readlines()

new_followers_list.append(read_new_followers_list)

new_followers.close()



for new_follwr in new_followers_list:
    if new_follwr not in old_followers_list:
        print(f" new followers are: {new_follwr}")





