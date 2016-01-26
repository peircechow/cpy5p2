#q04_determine_leap_year.py
print("LEAP YEAR CALCULATOR Ver 1.3")

boolean=True
while boolean:
    year=input("Enter year here:")
    def check():#to check whetehr this is valine numer
        try:
            int(year)
            return True
        except ValueError:
            return False
    if check():
        if float(year)%1!=0:
            print("Please enter a whole number")
        else:
            boolean=False
            if int(year)%4==0 and int(year)%100!=0:
                print(year,"is a leap year")
            elif int(year)%400==0:
                print(year,"is a leap year")
            else:
                print(year,"is a non-leap year")
    else:
        print("You did not enter a valid number. Please try again!")
