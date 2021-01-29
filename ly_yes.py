#to run use python3 
def open_st():
    while True:
        x = input("Enter a year in the form of an integer, or type exit to exit: ")
        if x == "exit":
            return
        try:
            y = int(x)
            check(y)
        except ValueError:
            print("That is not an integer, try again")
            open_st()

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