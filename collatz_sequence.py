def collatz(number):
    if number % 2 == 0:
        even_num = number // 2
        print(even_num)
        return even_num

    elif number % 2 == 1:
        odd_num = 3 * number + 1
        print(odd_num)
        return odd_num

try:    
    user_input = int(input("Enter your number: "))
except ValueError:
    print("Enter a Integer")

def collatz_sequence(user_input):
    if user_input == 1:
        return 1
    else:
        return collatz_sequence(collatz(user_input))

collatz_sequence(collatz(user_input))