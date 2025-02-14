# input P,C,M marks
# perc = (P+C+M)/3
# perc >= 80 = DISTINCTION
# perc >= 60 = FIRST
# perc >= 50 = SECOND
# perc >= 40 = PASS
# perc < 40 = FAIL
p=int(input("enter the physics Marks"))
c=int(input("enter the chemistry Marks"))
m=int(input("enter the Maths Marks"))
perc=(p+c+m)/3
if perc>=80:
    print("Distinction")
elif perc>=60:
    print("First")
elif perc>=50:
    print("Second")
elif perc>=40:
    print("Pass")
else:
    print("Fail")