#ME06_4_QUISTO

digits = int(input("Input a number from 1 to 999999999:"))
if digits >= 1 and digits <= 999999999:
    digits=list(str(digits))

    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tenths1 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eightteen', 'nineteen']
    tenthsx = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    def numtoword(num):
        for i in range(0, len(num)):
            if len(num)-i == 9 or len(num)-i == 6 or len(num)-i == 3:
                if int(num[i]) == 0:
                    print(end = '')
                else:
                    print(ones[int(num[i])], "hundred", end = ' ')
            elif len(num)-i == 8 or len(num)-i == 5 or len(num)-i == 2:
                if int(num[i]) == 1:
                    print(tenths1[int(num[i+1])], end=' ')
                    if len(num)-i == 2:
                        print('\n')
                        break
                    else:
                        i += 1
                elif int(num[i]) == 0:
                    print(tenthsx[int(num[i])], end='')
                else:
                    print(tenthsx[int(num[i])], end=' ')
            elif len(num)-i == 7:
                if int(num[i-1]) == 1 and len(num) > 7:
                    print("million", end =' ')
                elif int(num[i]) == 0:
                    print(' ', end = '')
                else:
                    print(ones[int(num[i])], "million", end=' ')
            elif len(num)-i == 4:
                if int(num[i-1]) == 1 and len(num) > 4:
                    print("thousand", end =' ')
                elif int(num[i]) == 0:
                    print(' ', end ='')
                else:
                    print(ones[int(num[i])], "thousand", end=' ')
            else:
                print(ones[int(num[i])], end = '')

    numtoword(digits)
else:
    print("Invalid input")



