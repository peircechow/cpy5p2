names = []
scores = []
while True:
    try:
        students = int(input("No. of students: "))
        break
    except ValueError:
        print("Please Enter an integer!")
        #continue
    #break

for i in range(1,students+1):
    #x=True
    while True:
        try:
            names.insert(i,str(input("Name of student {0}:".format(i))))
            scores.insert(i,int(input("Score: ")))
            #x=False   
        except ValueError as v:
            print("Invalid Input:")
            print("Error: ",v)
            continue
        break
        
highest = scores.index(max(scores))

print ("Highest score by student: ",names[highest])
print ("Highest score: ",max(scores))

if students != 1:
    names.remove(names[highest])
    scores.remove(max(scores))

    highest = int(scores.index(max(scores)))

    print ("Second score by student: ",names[highest])
    print ("Second highest score: ",max(scores))
