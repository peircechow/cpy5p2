x=True
while x:

    m=input("Enter month in number here (eg. March is Month 3): Month")
    y=input("Enter year here:")

    def check_input():
        try:
            month=int(m)
            year=int(y)
            return True
        except ValueError:
            return False
    
    if check_input():
        month=int(m)
        year=int(y)
        if year%4==0 or year%400==0 and year%100!=0:
            if month==2:
                print("Feruary has 29 days")
        elif month>12:
            print("A year has only 12 months!")
        else:
            if month==1:
                print("January has 31 days")
            elif month==2:
                print("February has 28 days")
            elif month==3:
                print("March has 31 days")
            elif month==4:
                print("April has 30 days")
            elif month==5:
                print("May has 31 days")
            elif month==6:
                print("June has 30 days")
            elif month==7:
                print("July has 31 days")
            elif month==8:
                print("August has 31 days")
            elif month==9:
                print("September has 30 days")
            elif month==10:
                print("October has 31 days")
            elif month==11:
                print("November has 30 days")
            elif month==12:
                print("December has 31 days")
            x=False

    else:
        print("Invalid input! Please enter an integer!")
