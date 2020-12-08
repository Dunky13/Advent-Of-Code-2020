from typing import Dict, List
import re
class Pass:
    mdict: Dict
    check: Dict
    def __init__(self):
        self.mdict = {}
        # self.check = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        self.check = {
            "byr": (lambda inp: 1920 <= int(inp) <= 2002),
            "iyr": (lambda inp: 2010 <= int(inp) <= 2020),
            "eyr": (lambda inp: 2020 <= int(inp) <= 2030),
            "ecl": (lambda inp: inp in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),
            "pid": (lambda inp: bool(re.match("^[0-9]{9}$", inp))),
            "hgt": (lambda inp: bool(re.match("^(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$", inp))),
            "hcl": (lambda inp: bool(re.match("^#[0-9a-f]{6}$", inp)))
        }
        pass

    def add_line(self, line: str):
        items = line.split(" ")
        for item in items:
            # print(item)
            key,val = item.split(":")
            self.mdict[key] = val.strip()

    def is_valid(self) -> bool:
        keys = self.mdict.keys()
        checkkey = self.check.keys()
        for i in checkkey:
            if i not in keys:
                return False
            elif not self.check[i](self.mdict[i]):
                # print(i, self.mdict[i])
                return False
        return True

    def key(self, key:str) -> str:
        return f"{key}: {self.mdict[key]}"

    def __str__(self) -> str:
        retstr = ""
        
        for key in self.check:
            retstr += self.key(key)
            retstr += ",\t"
        
        return retstr

def start():
    lines = []
    with open('input1', 'r') as f:
       lines = [i.strip() for i in f.readlines()]

    passport: Pass = Pass()
    valid = 0
    for line in lines:
        if len(line) == 0:
            if passport.is_valid():
                valid += 1
                # print(passport)
            passport = Pass()
        else:
            passport.add_line(line)
    valid += 1 if passport.is_valid() else 0

    print("Hello", valid)
    

if __name__ == "__main__":
    start()