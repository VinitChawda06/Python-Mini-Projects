# spam = int(input("Enter a number from 1 to 10: "))

# if spam == 1:
#     print("Hello")
# elif spam == 2:
#     print("Howdy")
# else:
#     print("Greetings!1")

# Test cases
# spam = ['apples', 'bananas', 'tofu', 'cats']


birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == "":
#         break

#     if name in birthdays:
#         print(birthdays[name] + ' is the birthdate of ' + name)
#     else:
#         print('I do not have birthday information for' + name)
#         print('Enter Birthdate to add the birthday')
#         bdate = input()
#         birthdays[name] = bdate
#         print('Birthday database updated')
keys = list(birthdays.keys())
print(keys)