def check_fermat(a,b,c,n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, fermat was wrong!")
    else:
        print("No, that doesn't work. You are a LOSER.")


def user_inputs_fermat():
    a = int(input("Pick a number for a\n"))
    b = int(input("Pick a number for b\n"))
    c = int(input("Pick a number for c\n"))
    n = int(input("Pick a number for n\n"))
    check_fermat(a,b,c,n)


check_fermat(1,2,3,3)
user_inputs_fermat()