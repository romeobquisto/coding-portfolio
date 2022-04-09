#ME07_1_QUISTO

word = input("Input a string(up to 20 characters):")

if 0 < len(word) < 21:
    print("Word entered:", word)
    word = word.lower()
    drow = word[::-1] #reverses word string
    if word == drow:
        print("Palindrome")
    else:
        print("Not a palindrome")
else:
    print("Invalid input")
