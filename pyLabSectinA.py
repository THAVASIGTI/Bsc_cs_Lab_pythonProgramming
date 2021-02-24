import os


def main():
    print("=================== MAIN MENU ========================")
    print("any enter the choice in menu box:")
    print("1.fahrenheit and celius\n2.Studen Mark List\n3.shop\n4.Fibonacci Seriace\n5.Factorial Nmuber\n6.Matrix(multiplcation/addtion)\n7.exit")
    ch = int(input("=> "))
    if ch == 1:
        celsius()
    elif ch == 2:
        markList()
    elif ch == 3:
        shep()
    elif ch == 4:
        fibonaci()
    elif ch == 5:
        factorial()
    elif ch == 6:
        matrix()
    elif ch == 7:
        exit()
    elif ch == 0:
        code()
    else:
        print("enter the choice menu box:\n")

def celsius():
    while(i<j):
        print("__________conveter___________")
        print("enter the choice:")
        print("1.fahrenheit to celius\n2.celius to fahrenheit\n3.exit\n")
        ch = input("=>")
        if ch == "1":
            fah = float(input("enter the value of fahrenheit:\n"))
            cel = (fah-32)/1.8
            print("celius value of :"+str(cel))
        elif ch == "2":
            cel = float(input("enter the value of celius:\n"))
            fah = (cel*1.8)+32
            print("fahrenheit value of :"+str(fah))
        elif ch == "3":
            main()
        else:
            print("plazz enter the choice menu!!!")

def markList():
    while i<j:
        print("________markList___________")
        s1 = int(input("enter the mark subject 1:\n =>"))
        s2 = int(input("enter the mark subject 2:\n =>"))
        s3 = int(input("enter the mark subject 3:\n =>"))
        s4 = int(input("enter the mark subject 4:\n =>"))
        s5 = int(input("enter the mark subject 5:\n =>"))
        total = s1+s2+s3+s4+s5
        avrage = total/5
        print("----------Final Rebort-----------------")
        print("subject 1 : "+str(s1))
        print("subject 2 : "+str(s2))
        print("subject 3 : "+str(s3))
        print("subject 4 : "+str(s4))
        print("subject 5 : "+str(s5))
        print("total     : "+str(total))
        print("avrage    : "+str(avrage))
        print("\n")
        ch=str(input("...contiune type the "'y'" enter to main menu :\n"))
        if ch != "y":
            main()

def shep():
    while i<j:
        print("1.Rectangel\n2.square\n3.circle\n4.triangle\n5.exit")
        ch=input("enter the choice box:\n=>")
        if ch == "1":
            l = float(input("enter the lenth:\n"))
            b = float(input("enter the birth:\n"))
            print("\n")
            print("area of Rectangel is:"+str(l*b))
            print("\n")
        elif ch == "2":
            l = float(input("enter the value:\n"))
            print("\n")
            print("area of square is :"+str(l*l))
            print("\n")
        elif ch == "3":
            pi = 3.14
            r = float(input("enter the value:\n"))
            print("\n")
            print("area of circle is:"+str(pi*r*r))
            print("\n")
        elif ch == "4":
            h = float(input("enter the hieght:\n"))
            b = float(input("enter the brith:\n"))
            print("\n")
            print("area of triangle is :"+str((h*b)/2))
            print("\n")
        elif ch == "5":
            main()
        else:
            print("enter the choice menu....\n")
            print("\n")

def fibonaci():
    while i<j: 
        print("__________Fibonaci seriace____________")
        f = int(input("Enter the fist number :\n=>"))
        l = int(input("Enter the last number :\n=>"))
        li = int(input("Enter the limit number :\n=>"))
        for x in range(li):
            temp = f + l
            f = l
            l = temp
            print(temp)
        print("\n")
        ch=str(input("...contiune type the "'y'" enter to main menu :\n"))
        if ch != "y":
            main()

def factorial():
    while i<j:
        print("________Factorial________")
        n=int(input("Enter number:\n=>"))
        fact=1
        while(n>0):
            fact=fact*n
            n=n-1
        print("Factorial of the number is: "+str(fact))
        print("\n")
        ch=str(input("...contiune type the "'y'" enter to main menu :\n"))
        if ch != "y":
            main()

def matrix():
    while i<j:
        print("__________Matrix______________")
        print("1.multiplication\n2.addtion\n3.exit")
        ch = int(input("enter the choice:\n=>"))
        if ch == 1:
            A=[]
            n=int(input("Enter N for N x N matrix: "))         
            print("Enter the element ::>")
            for x in range(n): 
                row=[]                                      
                for y in range(n): 
                    row.append(int(input()))           
                A.append(row)                      
            print(A)                                   
            B=[]
            n=int(input("Enter N for N x N matrix : "))           
            print("Enter the element ::>")
            for x in range (n): 
                row=[]                                      
                for y in range(n): 
                    row.append(int(input()))        
                B.append(row)                      
            print(B)                     
            result = [[0,0,0], [0,0,0], [0,0,0]] 
            for x in range(len(A)): 
                for y in range(len(B[0])): 
                    for k in range(len(B)): 
                        result[x][y] += A[x][k] * B[k][y] 
            print("The Resultant Matrix Is ::>")
            for r in result: 
                print(r) 
        elif ch == 2:
            A=[]
            n=int(input("Enter N for N x N matrix : "))        
            print("Enter the element ::>")
            for x in range(n): 
                row=[]                                      
                for y in range(n): 
                    row.append(int(input()))               
                A.append(row)                               
            print(A) 
            B=[]
            n=int(input("Enter N for N x N matrix : "))       
            print("Enter the element ::>")
            for x in range(n): 
               row=[]                                       
               for y in range(n): 
                  row.append(int(input()))            
               B.append(row)                           
            print(B)                                           
            result = [[0,0,0], [0,0,0], [0,0,0]] 
            for x in range(n):    
                for y in range(len(A[0])): 
                    result[x][y] = A[x][y] + B[x][y] 
            print("Resultant Matrix is ::>")
            for r in result: 
               print(r)
        elif ch == 3:
            main() 
        else:
            print("enter the choice menu...")

def code():
    print("copyright code secure")
    u = input("enter the user name :\n[*]>")
    u1 = "gti"
    p1 = "gti123"
    if u == u1:
        print("userName,Ok")
        p = input("enter the password :\n[*]>")
        if p == p1:
            print("1.fahrenheit and celius\n2.Studen Mark List\n3.shop\n4.Fibonacci Seriace\n5.Factorial Nmuber\n6.Matrix(multiplcation/addtion)\n[*]>")
            ch = int(input())
            if ch == 1:
                print("\n")
                print("\n")
                print("@source code:")
                print("\n")
                print("\n")
                print("""print("enter the choice:")
print("1.fahrenheit to celius 2.celius to fahrenheit 3.exit")
ch = input("=>")
if ch == "1":
    fah = float(input("enter the value of fahrenheit:"))
    cel = (fah-32)/1.8
    print("celius value of :"+str(cel))
elif ch == "2":
    cel = float(input("enter the value of celius:"))
    fah = (cel*1.8)+32
    print("fahrenheit value of :"+str(fah))
elif ch == "3":
    exit()
else:
    print("plazz enter the choice menu!!!")""")
                main()      
            elif ch == 2:
                print("\n")
                print("\n")
                print("@source code:")
                print("\n")
                print("\n")
                print("""print("________markList___________")
s1 = int(input("enter the mark subject 1: =>"))
s2 = int(input("enter the mark subject 2: =>"))
s3 = int(input("enter the mark subject 3: =>"))
s4 = int(input("enter the mark subject 4: =>"))
s5 = int(input("enter the mark subject 5: =>"))
total = s1+s2+s3+s4+s5
avrage = total/5
print("----------Final Rebort-----------------")
print("subject 1 : "+str(s1))
print("subject 2 : "+str(s2))
print("subject 3 : "+str(s3))
print("subject 4 : "+str(s4))
print("subject 5 : "+str(s5))
print("total     : "+str(total))
print("avrage    : "+str(avrage))""")
                main()
            elif ch == 3:
                print("\n")
                print("\n")
                print("@source code:")
                print("\n")
                print("\n")
                print("""print("1.Rectangel/n2.square/n3.circle/n4.triangle/n5.exit")
ch=input("enter the choice box:=>")
if ch == "1":
    l = float(input("enter the lenth:"))
    b = float(input("enter the birth:"))
    print("area of Rectangel is:"+str(l*b))
elif ch == "2":
    l = float(input("enter the value:"))
    print("area of square is :"+str(l*l))
elif ch == "3":
    pi = 3.14
    r = float(input("enter the value:"))
    print("area of circle is:"+str(pi*r*r))
elif ch == "4":
    h = float(input("enter the hieght:"))
    b = float(input("enter the brith:"))
    print("area of triangle is :"+str((h*b)/2))
elif ch == "5":
    exit()""")
                main()
            elif ch == 4:
                print("\n")
                print("\n")
                print("@source code:")
                print("\n")
                print("\n")
                print("""print("__________Fibonaci seriace____________")
f = int(input("Enter the fist number :=>"))
l = int(input("Enter the last number :=>"))
li = int(input("Enter the limit number :=>"))
for x in range(li):
    temp = f + l
    f = l
    l = temp
    print(temp)""")
                main()

            elif ch == 5:
                print("\n")
                print("\n")
                print("@source code:")
                print("\n")
                print("\n")
                print("""print("________Factorial________")
n=int(input("Enter number:\n=>"))
fact=1
while(n>0):
fact=fact*n
n=n-1
print("Factorial of the number is: "+str(fact))""")
                main()
            elif ch == 6:
                ch=int(input("1.multiply\n2.addtion\n3.exit"))
                if ch == 1:
                    print("\n")
                    print("\n")
                    print("@source code:")
                    print("\n")
                    print("\n")
                    print("""ch = int(input("enter the choice:/n=>"))
if ch == 1:
    A=[]
    n=int(input("Enter N for N x N matrix: "))         
    print("Enter the element ::>")
    for x in range(n): 
        row=[]                                      
        for y in range(n): 
            row.append(int(input()))           
        A.append(row)                      
    print(A)                                   
    B=[]
    n=int(input("Enter N for N x N matrix : "))           
    print("Enter the element ::>")
    for x in range (n): 
        row=[]                                      
        for y in range(n): 
            row.append(int(input()))        
        B.append(row)                      
    print(B)                     
    result = [[0,0,0], [0,0,0], [0,0,0]] 
    for x in range(len(A)): 
        for y in range(len(B[0])): 
            for k in range(len(B)): 
                result[x][y] += A[x][k] * B[k][y] 
    print("The Resultant Matrix Is ::>")
    for r in result: 
        print(r)""")
                    main()
                elif ch == 2:
                    print("\n")
                    print("\n")
                    print("@source code:")
                    print("\n")
                    print("\n")
                    print("""A=[]
n=int(input("Enter N for N x N matrix : "))        
print("Enter the element ::>")
for x in range(n): 
    row=[]                                      
    for y in range(n): 
        row.append(int(input()))               
    A.append(row)                               
print(A) 
B=[]
n=int(input("Enter N for N x N matrix : "))       
print("Enter the element ::>")
for x in range(n): 
   row=[]                                       
   for y in range(n): 
      row.append(int(input()))            
   B.append(row)                           
print(B)                                           
result = [[0,0,0], [0,0,0], [0,0,0]] 
for x in range(n):    
    for y in range(len(A[0])): 
        result[x][y] = A[x][y] + B[x][y] 
print("Resultant Matrix is ::>")
for r in result: 
   print(r)""")
                    main()
                elif ch == 3:
                    main()
                else:
                    print("choice the menu box")
                main()

        else:
            print("tri agin")
            main()
    else:
        print("tri agin")
        main()

    




i,j=0,99
if __name__=="__main__":
    main()