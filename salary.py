salary=float(input("enter salary:"))
yos=float(input("eneter year of service:"))
if yos>10:
  print("bonus is: ",0.01*salary)
elif yos>=6 and yos<=10:
  print("bonus is: ",0.08*salary)
else:
  print("bonus is: ",0.05*salary)
  
  