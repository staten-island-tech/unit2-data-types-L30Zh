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


Tip = [1.0, 1.15, 1.20, 1.25]
x = 50
Tip_Amount = input(f"The bill is {x} dollars, how was the servive?")
if Tip_Amount == "bad":
    print(f"Well, The total is {x*Tip[0]} dollars then...")
elif Tip_Amount == "ok":
    print(f"Alright, the total is {x*Tip[1]} dollars.")
elif Tip_Amount == "good":
    print(f"That's nice to hear! The total is {x*Tip[2]} dollars.")
elif Tip_Amount == "great":
    print(f"That's nice to hear! The total is {x*Tip[3]} dollars.")

