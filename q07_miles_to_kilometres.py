##q07_miles_to_kilometres.py
##1 mile=1.609kilometres

print("Miles Kilometers Kilometres Miles")
miles=1
kilometres=20
while miles<11:
    km=1.609*miles
    m=0.6213*kilometres
    print("{0:<6}{1:<11}{2:<11}{3:.3f}".format(miles,km,kilometres,m))
    miles+=1
    kilometres+=5
    
