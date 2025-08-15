
def even(n):
    e = []
    for i in range(1,n):
        if i % 2 == 0: e.append(i)
    
    print("The Even Numbers Are:",e)            

def odd(n):
    e = []
    for i in range(1,n):
        if i % 2 == 1: e.append(i)
    
    print("The Odd Numbers Are:",e)            

num = int(input("Enter Upto: "))

print("Do You Want:\n1. Even\n2. Odd")

op = int(input())

if op == 1: even(num)
else: odd(num)