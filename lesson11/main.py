from classes import VkUser
from config import token


user1 = VkUser(token)
user2 = VkUser(token, owner_id=171681064)
user1.get_friends()
user2.get_friends()
user2.friends.append(21444050)
user_mutual = user1 & user2

for friend in user_mutual:
    print(friend.last_name, friend.first_name)
    print(friend)
