from typing import Dict
class Pass:
    mdict: Dict
    def __init__(self):
        self.mdict = {}
        pass

    def add_line(self, line: str):
        items = line.split(" ")
        for item in items:
            # print(item)
            key,val = item.split(":")
            self.mdict[key] = val

    def is_valid(self) -> bool:
        keys = self.mdict.keys()
        check = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        for i in check:
            if i not in keys:
                return False
        return True

def start():
    lines = []
    with open('input1', 'r') as f:
       lines = [i.strip() for i in f.readlines()]

    passport: Pass = Pass()
    valid = 0
    for line in lines:
        if len(line) == 0:
            valid += 1 if passport.is_valid() else 0
            passport = Pass()
        else:
            passport.add_line(line)

    print("Hello", valid)
    

if __name__ == "__main__":
    start()