#(writing information to file.)
f = open("C:\\MyPython\\ch8\\bio.txt","a") # a means keep appending
#f = open("F:\\MyPython\\ch8\\bio.txt","w") # it is one time and it will keep overwrite once u enter new data
name = input("Enter your name:")
age = int(input("Enter your age:"))
salary = float(input("Enter salary:"))
f.write("Name:" + name +"\n")
f.write("Age:" + str(age) + "\n")
f.write("Salary:" + str(salary) + "\n")