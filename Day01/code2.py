
def start():
    lines = []
    with open('input1', 'r') as f:
       lines = [int(i) for i in f.readlines()]

    lines.sort()

    for i in range(len(lines)):
        val_a = lines[i]
        for j in range(i, len(lines)):
            val_b = lines[j]
            for k in range(j, len(lines)):
                val_c = lines[k]
                if val_a + val_b + val_c == 2020:
                    print(val_a, val_b, val_c, val_a * val_b * val_c)
    

if __name__ == "__main__":
    start()