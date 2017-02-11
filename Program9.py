maths=input("enter marks of maths")
physics=input("enter marks of physics")
chemistry=input("enter marks of chemistry")
physicaled=input("enter marks of P.E.")
english=input("enter marks of english")
mean=(maths+physics+chemistry+physicaled+english)/5
perc=mean*100
print"mean=",mean
if(perc<=35):
    print"fail"
else:
    print"pass"
