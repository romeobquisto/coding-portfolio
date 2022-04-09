#ME11_2_QUISTO.py

from convertfcn import IntToRom

bilang = int(input("Enter a number from 1 to 1000: "))

if bilang < 1 or bilang > 1000:
    print("Invalid Input")
else:
    print("Decimal number:", bilang)
    numero = IntToRom(bilang)
    print("Converted roman numeral:", numero.converter())
