
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

    _ids = []
    for line in lines:
        _row = row(line)
        _column = column(line)
        _id = (_row * 8) + _column
        _ids.append(_id)

    _ids.sort()
    for i in range(len(_ids)-1):
        if _ids[i] == _ids[i+1]-2:
            print(_ids[i]+1)
    

if __name__ == "__main__":
    start()