principle=input("enter principle amount")
time=input("enter time")
rate=input("enter interest rate")
def simple_interest(pa,ti,ra):
    si=(principle*rate/100)*time;
    print"the simple interest is",si
simple_interest(pa=principle,ti=time,ra=rate)
