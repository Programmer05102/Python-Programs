
print("OPTIONS:\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n 5. Modulus\n 6. Calculate Percentage\n 7. Percentage Of")
f_num = int(input("Enter First Number : "))
s_num = int(input("Enter Second Number : "))
op = input("Enter Arithematic Opeation You Want To Perform: ")

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

def per(a, b):
    if op == "6":
        print("The Percentage Is: ",(a / b) * 100,"%")
    elif op == "7":
        print(a,"% of",b,"is",(a / 100) * b)
    else:
        print("Invalid Selection: ")

if op >= "1" and op <= "5":
    A_Operation(f_num, s_num)
else:
    per(f_num, s_num)