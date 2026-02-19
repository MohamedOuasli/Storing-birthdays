friends = {}

for i in range(5):
    name = input("Enter friend's name: ")
    birthday = input("Enter their birthday: ")
    friends[name] = birthday

print("\nBirthdays:")
for name, birthday in friends.items():
    print(name, ":", birthday)