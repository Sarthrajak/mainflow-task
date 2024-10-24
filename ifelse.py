english = int(input("Enter English Marks: "))
math = int(input("Enter Math Marks: ")) 
science = int(input("Enter science Marks: ")) 
Hindi = int(input("Enter hindi Marks: ")) 
total = english+math+science+Hindi
percentage = total * 100 / 400
if percentage > 75:
    print("Passed with First division ")
elif percentage > 60:
    print("Passed with secound division ")
elif percentage > 33:
    print("Passed with third division ")
else:
    print("Failed")            