student=int(input("enter the number of the student: "))
avg=0
sum1=0
for i in range(1,student+1):
    print("Enter the markes of studen")
    subject1=int(input("enter the markes of subject1:"))
    subject2=int(input("enter the markes of subject2:"))
    subject3=int(input("enter the markes of subject3:"))
    subject4=int(input("enter the markes of subject4:"))
    subject5=int(input("enter the markes of subject5:"))
    sum=subject1+subject2+subject3+subject4+subject5
    persent=(sum/500)*100
    print(f"persten of student is:{persent}")
    sum1+=sum
avg+=(sum1/(500*student))*100
print(f"avarage persent of student is:{avg}")
