#multiplication table in format '123  x  6  =  738'


a=int(input("enter the no of which you want multiplication table : "))
for x in range(10):
 print(a," x ",(x+1)," = ",a*(x+1))
