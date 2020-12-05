
def steps(lines, stepx: int, stepy: int) -> int:
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
    return trees

def start():
    lines = []
    with open('input1', 'r') as f:
       lines = [i.strip() for i in f.readlines()]

    allsteps = []
    allsteps.append(steps(lines, 1,1))
    allsteps.append(steps(lines, 3,1))
    allsteps.append(steps(lines, 5,1))
    allsteps.append(steps(lines, 7,1))
    allsteps.append(steps(lines, 1,2))

    trees = 1
    print(allsteps)
    for i in allsteps:
        trees *= i
    
    
    print("Trees:", trees)
    

if __name__ == "__main__":
    start()