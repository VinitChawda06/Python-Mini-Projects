# spam = int(input("Enter a number from 1 to 10: "))

# if spam == 1:
#     print("Hello")
# elif spam == 2:
#     print("Howdy")
# else:
#     print("Greetings!1")

# Test cases
# spam = ['apples', 'bananas', 'tofu', 'cats']

import pprint
message = 'It was a bright cold day'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)