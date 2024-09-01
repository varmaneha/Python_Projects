import random
friends = [ "Neha", "Pooja", "Kiran" ]

#1 Method
print(random.choice(friends))

#2 Method
random_index = random.randint(0,4)
print(friends[random_index])