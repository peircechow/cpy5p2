##q12_find_factors.py
boolean=True
while boolean:
    try:
        i=int(input("Enter integer here to find factors of the integer:"))
        if i<=0:
            print("Please enter a positive integer!")
        else:
            n=2
            a=i #do not allow value of i in n<i to change, so sub with a instead
            while n<=i:    
                if a%n==0:
                    print(n)
                    a=a/n
                else:
                    n+=1
            boolean=False
    except ValueError:
        print("Please enter an integer!")



##i=int(input("Enter integer here to find factors of the integer:"))
##
##n=2
##a=i #do not allow value of i in n<i to change, so sub with a instead
##while n<=i:    
##    if a%n==0:
##        print(n)
##        a=a/n
##    else:
##        n+=1
