import sympy as sp
import fractions as fr

def main():

    change_sign = False

    while True:
        #a,b,c can be mathematical expressions
        a = sp.parse_expr(input("Insert value of a: "))
        b = sp.parse_expr(input("Insert value of b: "))
        c = sp.parse_expr(input("Insert value of c: "))

        if(a == 0 or b == 0 or c == 0):
            print("Input not valid, a-b-c mustn't be 0.")
        elif((float(math.pow(b,2)))-(4*a*c) >= 0): #delta 
            print("Input not valid, delta is not < 0.")
        else:
            break

    if a < 0:
        a = -a
        b = -b
        c = -c
        change_sign = True
        print("Change sign of a,b,c.")

    #calculate k,q,m
    k = sp.sqrt(a) #k = a^(1/2)
    q = b/(2*k)
    m = c - sp.Pow(q,2)

    #change "sqrt" to "√" in k,q,m
    k_string = str(sp.sqrt(a)).replace("s","√")
    k_string = change_sqrt(k_string)
    q1_string = str(sp.Rational(b,2)/sp.sqrt(a)).replace("s","√")
    q1_string = change_sqrt(q1_string)
    q2_string = str(sp.simplify(sp.Rational(b,2*k))).replace("s","√")
    q2_string = change_sqrt(q2_string)
    
    #print k,q,m
    print(f"k = √a = {k_string}")
    if len(str(q)) > 5:
        print(f"q = b/(2*√a) = {q1_string}")
    else:
        print(f"q = b/(2*√a) = {int(q)}" if (q % 1 == 0) else f"q = b/(2*√a) = {q2_string}")
    if len(str(m)) > 5:
        print(f"m = c - (b/(2*√a))^2 = {sp.simplify(fr.Fraction(str(c)) - sp.simplify(sp.Rational(b*b,4*a)))}")
    else:
        print(f"m = c - (b/(2*√a))^2 = {int(m)}" if (m % 1 == 0) else f"m = c - (b/(2*√a))^2 = {fr.Fraction(str(c - sp.Rational(b*b,4*a)))}") 

    #mathematical sign control
    if(change_sign): 
        print("result -> -[(kx+q)^2 + m]")
    else:
        print("result -> (kx+q)^2 + m")
        
def change_sqrt(string):
    for ch in ['q','r','t']:
        string = string.replace(ch,"")
    return string

if __name__ == "__main__":
    main()
