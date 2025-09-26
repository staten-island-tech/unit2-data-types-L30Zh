""" x = 3
y = float(3)
print(x, y) """



""" 
values = [1,2.23,5,7,2,30,15]
print(values)
print (values[0])
print (values[6])

 """

# == is equal to an evaluation
""" 
x = 15

if x == 16:
    print("x is 15")
elif x > 15:
    print("x is greater than 15")
else:
    print("x is less than 15") """


""" values = [1,2.23,5,8,2,30,15]
if values[3] == 7:
    print("The fourth value is 7")
elif values[3] > 7:
    print("The fourth value is greater than 7")
else:
    print("The fourth value is less than 7") """


""" DayWeek = input("What day is it?")

if DayWeek == "Monday" "it is Monday":
    print("Correct")
else: print("Incorrect")

 """


""" x = ["2+2", "3+5", "12-3", "5*6"]

Question = input(f"What is, {x}?")

 """




""" temp = 80
if temp > 70:
    print("It is hot")
elif temp == 70:
    print("It is perfect")
else:
    print("It is cold") """



#Challenge 1:
""" 
x=16

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
 """



#Challenge 2:

""" 
Tip = [1.0, 1.15, 1.20, 1.25]
x = 50
Tip_Amount = input(f"The bill is {x} dollars, how was the servive?")
if Tip_Amount == "bad":
    print(f"Well, The total is {x*Tip[0]} dollars then...")
elif Tip_Amount == "ok":
    print(f"Alright, the total is {x*Tip[1]} dollars with a {Tip[1]*100 - 100} percent tip.")
elif Tip_Amount == "good":
    print(f"That's nice to hear! The total is {x*Tip[2]} dollars with a {Tip[2]*100 - 100} percent tip.")
elif Tip_Amount == "great":
    print(f"That's nice to hear! The total is {x*Tip[3]} dollars with a {Tip[3]*100 - 100} percent tip.")"""




#Challenge 3:
""" 
Num = 250
Input = input(f"The number is: {Num}, correct?")
if Input == "yes":
    print(f"Okay, the divisors of the number are:")
    for i in range(1, Num + 1):
        if Num % i == 0:
            print(i)
else: print("okay then..") """





#Challenge 4:

""" Num1 = 1024
Num2 = 4096

values = []
for i in range(1, Num1 + 1):
    if Num1 % i == 0:
        for j in range(1, Num2 + 1):
            if Num2 % j == 0:
                if i == j:
                    print (j)
 """

Values = []
def gcf (x, y):
    for i in range(1, x+1):
        if x % i == 0 and y % i == 0:
            Values.append(i)
gcf (4952136, 1236912)
GCF = (max(Values))
print (f"The GCF of the two digits is {GCF}")

                
                    
        




