###q03_determine_grade.py

print("GRADING SYSTEM Ver 5.0")

boolean=True
while boolean:
    s=input("Enter score from 0-100 here:")
    def check():
        try:
            score=float(s)
            return True
        except ValueError:
            return False
                ##print("Invalid input. Please enter a number!")
            
    if check():
        score=float(s)
        boolean=False
        if 70<=score<=100:
            print("A")
        elif 60<=score<70:
            print("B")
        elif 55<=score<60:
            print("C")
        elif 50<=score<55:
            print("D")
        elif 45<=score<50:
            print("E")
        elif 35<=score<44:
            print("S")
        elif 0<=score<35:
            print("U")
        else:
            print("Invalid! Score must be within 0-100")
            boolean=True
    else:
        print("Invalid input. Please enter a number!")

            
                

        
            

