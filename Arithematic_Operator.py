
op = input("OPTIONS:\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n 5. Modulus\n Enter Arithematic Opeation You Want To Perform: ")
f_num = int(input("Enter First Number : "))
s_num = int(input("Enter Second Number : "))

def A_Operation(a, b):
    if op == "1":
        print("The Sum Is: ",a + b)
    elif op == "2":
        print("The Differnce Is: ",a - b)
    elif op == "3":
        print("The Product Is: ",a * b)
    elif op == "4":
        print("The Quotient Is: ", a / b)
    elif op == "5":
        print("The Modulus Is: ",a % b)
    else:
        print("Invalid Selection: ")


A_Operation(f_num, s_num)