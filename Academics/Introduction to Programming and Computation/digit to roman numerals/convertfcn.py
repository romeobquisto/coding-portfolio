#ME11_3.py

class IntToRom:
    def __init__(self, num):
        self._n = num
        self.roman = ''
        self.symbols = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX",
                        "V", "IV","I"]
    def if1000(self):
        if self._n >= 1000:
            self.roman += self.symbols[0]*(self._n//1000)
            return self._n - (self._n//1000)*1000
        else:
            return self._n
    def if900(self, rem):
        if rem >= 900:
            self.roman += self.symbols[1]
            return rem - 900
        else:
            return rem
    def if500(self, rem):
        if rem >= 500:
            self.roman += self.symbols[2]
            return rem - 500
        else:
            return rem
    def if400(self, rem):
        if rem >= 400:
            self.roman += self.symbols[3]
            return rem - 400
        else:
            return rem
    def if100(self, rem):
        if rem >= 100:
            self.roman += self.symbols[4]*(rem//100)
            return rem - 100*(rem//100)
        else:
            return rem
    def if90(self, rem):
        if rem >= 90:
            self.roman += self.symbols[5]
            return rem - 90
        else:
            return rem
    def if50(self, rem):
        if rem >= 50:
            self.roman += self.symbols[6]
            return rem - 50
        else:
            return rem
    def if40(self, rem):
        if rem >= 40:
            self.roman += self.symbols[7]
            return rem - 40
        else:
            return rem
    def if10(self, rem):
        if rem >= 10:
            self.roman += self.symbols[8]*(rem//10)
            return rem - 10*(rem//10)
        else:
            return rem
    def if9(self, rem):
        if rem >= 9:
            self.roman += self.symbols[9]
            return rem - 9
        else:
            return rem
    def if5(self, rem):
        if rem >= 5:
            self.roman += self.symbols[10]
            return rem - 5
        else:
            return rem
    def if4(self, rem):
        if rem >= 4:
            self.roman += self.symbols[11]
            return rem - 4
        else:
            return rem
    def if1(self, rem):
        if rem >= 1:
            self.roman += self.symbols[12]*rem
            return self.roman
        else:
            return self.roman
    def converter(self):
        return self.if1(self.if4(self.if5(self.if9(self.if10(self.if40(self.if50(self.if90(self.if100(self.if400(self.if500(self.if900(self.if1000()))))))))))))
