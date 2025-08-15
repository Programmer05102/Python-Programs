import math

print("Area Of Shapes To Calculate\n1. Circle\n2. Triangle\n3. Sphere")
op = int(input("Enter Your Choice: "))

def area_C():
    r = float(input("Enter The Radius Of A Circle: "))
    a = math.pi * r ** 2
    print(f"Area Of Circle Is: {a:.2f}")

def area_T():
    alt = float(input("Enter Altitude Of A Triangle: "))
    base = float(input("Enter Base Of A Triangle: "))
    t = (0.5) * (alt * base)
    print(f"Area Of Triangle Is: {t:.2f}")

def area_S():
    r = float(input("Enter Radius of A Sphere: "))
    sphr = (4/3) * math.pi * r ** 3
    print(f"Area Of A Sphere Is: {sphr:.2f}")

if op == 1: area_C()

elif op == 2: area_T()

elif op == 3: area_S()