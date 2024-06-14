# spam = int(input("Enter a number from 1 to 10: "))

# if spam == 1:
#     print("Hello")
# elif spam == 2:
#     print("Howdy")
# else:
#     print("Greetings!1")

# Test cases
# spam = ['apples', 'bananas', 'tofu', 'cats']

# import pprint
# message = 'It was a bright cold day'
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# pprint.pprint(count)

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
'Bob': {'ham sandwiches': 3, 'apples': 2},
'Carol': {'cups': 3, 'apple pies': 1}}

# def totalBrought(guests, item):
numBrought = 0
for k, v in allGuests.items():
     print(k,v)
    #  numBrought = numBrought + v.get(item, 0)
# return numBrought