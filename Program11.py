principle=input("enter the principle amount")
rate=input("enter the interest rate")
time=input("enter the time in years")
def compound_interest(pr,rt,ti):
    i=1
    final =0
    while(i<=ti):
        ci=pr*rt/100
        pr=pr+ci
        final=final+ci
        i =i+1
    print"the compound interest is",final
compound_interest(pr=principle,rt=rate,ti=time)
