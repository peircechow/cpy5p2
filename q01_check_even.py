##q01_check_even.py

##n=input("Enter number:")
##def check_input(n):
##    try:
##        int(n)
##        return True
##    except ValueError:
##        return False
##    
##if check_input(n):
##    if x%2==1:
##        print(("{0} is an odd number.").format(x))
##
##    else:
##        print(("{0} is an even number.").format(x))
##    
##    
##

a=True
while a:

    try:
        x=int(input("Enter number:"))
        if x%2==1:
            print("{0} is an odd number.".format(x))
        else:
            print("{0} is an even number.".format(x))
        a=False
            
    except ValueError:
        print("Invalid number!Please try again")

