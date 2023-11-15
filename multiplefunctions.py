class multipleFunctions():
    def oddEven():
        num=int(input("Enter the number: "))
        if((num%2)==0):
            print("Number",num,"is an Even Number")
            message="Even Number"
        else:
            print("Number",num,"is an Odd Number")
            message="Odd Number"
        return message
    
    def BMI():
        BMI=int(input("Enter your BMI:"))
        if (BMI<18):
            print("Under Weight")
            message="Under Weight"
        elif (BMI<26):
            print("Healthy Weight")
            message="Healthy Weight"
        elif (BMI<31):
            print("Over Weight")
            message="Over Weight"
        elif (BMI<36):
            print("Obese")
            message="Obese"
        elif (BMI<41):
            print("Severely Obese")
            message="Severely Obese"
        elif (BMI>41):
            print("Morbidly Obese")
            message="Morbidly Obese"
        return message