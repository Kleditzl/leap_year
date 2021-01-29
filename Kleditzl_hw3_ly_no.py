#To run, just use python3
def open_st():
    x = input("Enter a year in the form of an integer: ")
    x = int(x)
    check(x)

def check(x):
    a = 0
    if (x % 4) == 0:
        a += 1
        if (x % 100) == 0:
            if (x % 400) == 0:
                a += 1
            else:
                a -= 1
    if a > 0:
        print("{} was a leap year". format(x))
    else:
        print("{} wasn't a leap year". format(x))

if __name__ == '__main__':
    open_st()
