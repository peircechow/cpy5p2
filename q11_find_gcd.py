##q11_find_gcd.py
boolean=True
while boolean:
    first_integer=input("Enter the first integer here:")
    second_integer=input("Enter second integer here:")
    def check_input():
        try:
            n=int(first_integer)
            m=int(second_integer)
            return True
        except ValueError:
            return False

    if check_input():
        
        n=int(first_integer)
        m=int(second_integer)
        i=n
        if m==0 or n==0:
            print("Please enter a non-zero integer!")
        elif m<0 or n<0:
            print("Integer must be positive!")
        else:
            while n%i!=0 or m%i!=0:
                i=i-1  
            print("GCD is",i)
            boolean=False
    else:
        print("Invalid input. Please enter an integer!")
        

