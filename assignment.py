class assignments():
    def subfields():
        print("Sub-fiedls in AI are:")
        list = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        list1=[]
        for i in list:
            print(i)
            r=list1.append(i)

    def oddeven():
        num=int(input("Enter your number:"))
        if num%2==0:
            print(num,"is Even number")
        else:
            print(num,"is Odd number")

    def eligible():
        gender=input("Your Gender: ")
        age=int(input("Your Age: "))
        a=gender.casefold()
        b=age
        if  a=="male" and b==21:
            print("ELIGIBLE")
        elif a=="female" and b==18:
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE") 

    def percentage():
        sub1=int(input("Subject1= "))
        sub2=int(input("Subject2= "))
        sub3=int(input("Subject3= "))
        sub4=int(input("Subject4= "))
        sub5=int(input("Subject5= "))
        total=sub1+sub2+sub3+sub4+sub5
        print("Total :",total)
        percent=total/5
        print("Percentage :",percent)  

    def triangle():
        h=int(input("Height:"))
        b=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        a=(h*b)/2
        print("Area of Triangle: ",a)
        h1=int(input("Height1:"))
        h2=int(input("Height2:"))
        b=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        p=h1+h2+b
        print("Perimeter of Triangle: ",p)