##q02_triangle.py



x=True
while x:
    a=input("Enter side 1:")
    b=input("Enter side 2:")
    c=input("Enter side 3:")
    def check():
        try:
            d=float(a)
            e=float(b)
            f=float(c)
            return True
        except ValueError:
            return False
            #print("Invalid input. Please try again!")

    if check():
        d=float(a)
        e=float(b)
        f=float(c)
        if d<=0 or e<=0 or f<=0:
            print("Please enter a positive number!")

        elif d+e>f and e+f>d and f+d>e:
            perimeter=d+e+f
            print("Perimeter of triangle is",perimeter)
            x=False

        else:
            print("Invalid input")
    else:
        print("Invalid input! PLease try again!")

            
        
