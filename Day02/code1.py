
def is_valid(inp: str) -> bool:
    pre, post = inp.split(":")
    nums, chr = pre.split(" ")
    mn, mx = nums.split("-")
    cnt = post.count(chr)
    return cnt >= int(mn) and cnt <= int(mx)

def start():
    lines = []
    with open('input1', 'r') as f:
       lines = f.readlines() #[int(i) for i in f.readlines()]

    count = 0
    for line in lines:
        if(is_valid(line)):
            count += 1
        # break
    print("Valid passwords: ", count)
        
    

if __name__ == "__main__":
    start()