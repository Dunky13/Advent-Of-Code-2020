
def start():
    lines = []
    with open('input1', 'r') as f:
       lines = [i for i in f.readlines()]

    print("Hello", lines)
    

if __name__ == "__main__":
    start()