#ME10_1_QUISTO

def gcf(a, b):
    if a < 0 or b < 0:
        return "Number must be positive"
    if a > b: # if a greater than b
        r = a%b
        if r == 0:
            return b
        elif r == 1:
            return 1
        return gcf(b, r)
    if b > a: #if b greater than a
        
        r = b%a
        if r == 0:
            return a
        elif r == 1:
            return 1
        return gcf(a, r)
    if a == b: #if equal then gcf is the same number
        return a

num1 = int(input("Enter a positive integer: "))
num2 = int(input("Enter a positive integer: "))
ans = gcf(num1, num2)
print(ans)
