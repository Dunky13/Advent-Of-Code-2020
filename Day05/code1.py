
def binary(line: str, lower: str, upper: str) -> int:
    _min = 0
    _max = 2**len(line) - 1
    for _char in line:
        if _char is lower:
            _max = (_min + _max ) / 2
        elif _char is upper:
            _min = (_min + _max ) / 2
    return round((_min+_max)/2)

def row(line: str) -> int:
    aline = line[:7]
    return binary(aline, "F", "B")

def column(line: str) -> int:
    aline = line[7:]
    return binary(aline, "L", "R")

def start():
    lines = []
    with open('input1', 'r') as f:
       lines = [i.strip() for i in f.readlines()]

    maxid = 0
    for line in lines:
        _row = row(line)
        _column = column(line)
        _id = (_row * 8) + _column
        if _id > maxid:
            maxid = _id

    print("Hello", maxid)
    

if __name__ == "__main__":
    start()