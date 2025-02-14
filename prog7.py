med_causes = input("Did you have any Medical Problems Yes or No : ")
atten = int(input("Enter your Attendance Score ou of 100 : "))

if med_causes == "yyeses":
   print("You are Allowed for the Exam")

else :
   if atten >= 75:
      print("You are Allowed for the Exam")
   else :
      print("You are Not Allowed for the Exam")
      
     
