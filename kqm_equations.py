import math

def main():
    while True:
        a = float(input("Insert value of a: "))
        b = float(input("Insert value of b: "))
        c = float(input("Insert value of c: "))
        if((float(math.pow(b,2)))-(4*a*c) >= 0): #delta 
            print("Input not valid, delta is not < 0.")
        else:
            break
    k = float(math.sqrt(-a)) if (a < 0) else float(math.sqrt(a)) #k = a^(1/2)
    q = b / 2
    m = c - float(math.pow((b/2),2))
    print("k = a^(1/2),\tq = b/2,\tm = c - (b/2)^2")
    print(f"k = {format(k, '.2f')}\tq = {format(q, '.2f')}\tm = {format(m, '.2f')}")

if __name__ == "__main__":
    main()