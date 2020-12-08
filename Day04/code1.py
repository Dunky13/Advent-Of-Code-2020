from typing import Dict, List
class Pass:
    mdict: Dict
    check: List[str]
    def __init__(self):
        self.mdict = {}
        self.check = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        pass

    def add_line(self, line: str):
        items = line.split(" ")
        for item in items:
            # print(item)
            key,val = item.split(":")
            self.mdict[key] = val

    def is_valid(self) -> bool:
        keys = self.mdict.keys()
        
        for i in self.check:
            if i not in keys:
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