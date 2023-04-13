total = 0

def num(i):
    global total

    if i <= 10:
        total += i
        print(str(i) + ("+" if i < 10 else ""), end="")
        num(i + 1)
    else:
        print("=", end="")
        return

num(1)
print(total)