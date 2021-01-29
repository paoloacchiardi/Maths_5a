import math

def main():
    while True:
        a = float(input("Insert value of a: "))
        b = float(input("Insert value of b: "))
        c = float(input("Insert value of c: "))
        if(a == 0 or b == 0 or c == 0):
            print("Input not valid, a-b-c mustn't be 0.")
        elif((float(math.pow(b,2)))-(4*a*c) >= 0): #delta 
            print("Input not valid, delta is not < 0.")
        else:
            break
    if a > 0:
        k = math.sqrt(a) #k = a^(1/2)
        q = b/(2*k)
        m = c - math.pow(q,2)
        print("k = a^(1/2),\tq = b/(2*a^(1/2)),\tm = c - (b/(2*a^(1/2)))^2")
        print(f"k = {format(k, '.2f')}\tq = {format(q, '.2f')}\tm = {format(m, '.2f')}")
        print("result -> (kx+q)^2 + m")
    else: # a < 0
        

if __name__ == "__main__":
    main()
