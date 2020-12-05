
def start():
    lines = []
    with open('input1', 'r') as f:
       lines = [i.strip() for i in f.readlines()]

    stepx = 3
    stepy = 1
    x = stepx
    y = stepy
    maxx = len(lines[0])
    maxy = len(lines)
    
    trees = 0
    while y < maxy:
        if lines[y][x] == "#":
            trees += 1

        x = (x + stepx) % maxx
        y += stepy
    
    print("Trees:", trees)
    

if __name__ == "__main__":
    start()