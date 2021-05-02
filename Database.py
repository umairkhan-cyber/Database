import os,sys,time
os.system("clear")
time.sleep(1)
print("\t\033[1;93m WELLCOME TO DATABASE\n")
print("Roll Number:")
b=[]
for a in range(1,5):
 print("\nStudent No :",a)
 c=int(input("Enter Roll Number :"))
 b.append(c)
a=int(input("\n 1)update \t2)remove \t3)add \t\n\n\033[1;96mSelect Option :"))
if a==1:
 os.system("clear")
 print("\033[1;92mupdated Successfully")
 for ll in b:
  print("\033[2;94mStudent Roll Number :",ll)
 time.sleep(3)
 os.system("python3 Database.py")
elif a==2:
 os.system("clear")
 for bb in b:
  print("\nStudent Roll Number :",bb,"\n")
 rm=int(input("Enter Student Roll Number to Remove :"))
 if rm in b:
     b.remove(rm)
     print("\nRoll Number",rm,"Successfuly Removed")
 else:
     print("\nRoll Number not found",rm)
     time.sleep(3)
     os.system("clear")
     os.system("python3 Database.py")

 for aa in b:
  print("\nStudent Roll Number :",aa)
 time.sleep(3)
 os.system("python3 Database.py")
elif a==3:
 os.system("clear")
 print("\tADD NEW Students RollNumbera")
 for n in range(1,5):
  print("\nStudent No :",n)
  new=int(input("Enter Roll Number :"))
  b.append(new)
 os.system("clear")
 for nnn in b:
  print("Student Roll Number :",nnn)
 time.sleep(3)
 os.system("python3 Database.py")
else:
 print("\nPlzz Select the Correct Choice")
 time.sleep(3)
 os.system("clear")
 os.system("python3 database.py")