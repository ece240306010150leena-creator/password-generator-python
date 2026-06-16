import random
print("Welcome to the Password Generator!")

letters=int(input("How many letters you want in your password?\n"))
symbols=int(input("How many symbols you want in your password?\n"))
numbers=int(input("How many numbers you want in your password?\n"))

if((letters<0) or (symbols<0) or (numbers<0)):
    print("Invalid input.")

else:
    list = []

    for i in range(0,letters):
        random_letters = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        list.append(random_letters)

    for i in range(0,symbols):
        random_symbols = random.choice(['!', '#', '$', '%', '&', '(', ')', '*', '+'])
        list.append(random_symbols)

    for i in range(0,numbers):
        random_numbers = random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        list.append(random_numbers)

    print(f"List before shuffling : {list}")

    random.shuffle(list)

    print(f"List after shuffling : {list}")

    if(len(list)==0):
        print("No password generated.")

    else:
        password = ''
        for i in list:
            password = password + i

        print(f"Your password is : {password}")
