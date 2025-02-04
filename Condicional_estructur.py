# 1. From the natural numbers A, B and C, print the maximum value
def MaximumValue(numA, numB, numC):
    print("\n--- Calculate the Maximun Value ---")
    if numA >= numB and numA >= numC:
        return numA
    elif numB >= numC:
        return numB
    else:
        return numC

# 2. Convert seconds to minutes:
#    - Do not use the % operator
#    - Print the minutes and seconds left
def SecondsToMinutes(seconds):
    print("\n--- Calculate Seconds to Minutes ---")
    minutes = seconds // 60
    secondsLeft = seconds - minutes * 60
    print(minutes , "minutes whith" , secondsLeft , "seconds left")

# 3. Billing with details:
#    - Validate that the numbers are greater than or equal to 10, if not 10
#    - Quantity of units acquired mauor equal to 1, otherwise assign 1
#    - Initial subtotal = unit price * quantity
#    - If the number of units to be compared is greater than 10, a wholesale discount of 20% will be applied to the subtotal.
#    - If the subtotal exceeds 100,000 pesos, 10% discount
#    - Discounted subtotal (subtotal after applicable discounts)
#    - VAT or IVA is 16% of the discounted subtotal
#    - Total: Discounted subtotal + VAT

def BillingWithDetails(prices, quantity):
    print("\n--- Billing with details ---")
    if prices <= 10:
        prices = 10

    print("Item price: " , prices)

    if quantity <= 1:
        quantity = 1

    print("Quantity: " , quantity)

    subtotal = prices * quantity
    discountSubtotal = subtotal

    print("Subtotal: " , subtotal)

    if quantity > 10:
        wholesale = subtotal * 0.20
        discountSubtotal -= wholesale
    else:
        wholesale = "Not applicable"
    print("Wholesale discount: ", wholesale)
        
    
    if  subtotal > 100000:
        quantityDiscont = subtotal * 0.10
        discountSubtotal -= quantityDiscont
    else:
        quantityDiscont = "Not applicable"
    print("Discount for quantity", quantityDiscont)
    
    print("Discounted subtotal: ", discountSubtotal)

    #VAT or IVA in Mexico
    vat= discountSubtotal * 0.16
    print("VAT: ", vat)
    print("Total: ", discountSubtotal + vat)
    
# 4. ISR
def ISR(salary):

    fixedQuota = 0
    percentageSuplus = 0
    loweLimit = 0

    if salary >= 0.01 and salary < 496.07:
        fixedQuota = 0.00
        percentageSuplus = 1.92
        loweLimit = 0.01

    elif salary >= 496.08 and salary < 4210.41:
        fixedQuota = 9.52
        percentageSuplus = 6.40
        loweLimit = 496.08

    elif salary >= 4210.42 and salary < 7399.42:
        fixedQuota = 247.23
        percentageSuplus = 10.88
        loweLimit = 4210.42

    elif salary >= 7399.43 and salary < 8601.50:
        fixedQuota = 594.24
        percentageSuplus = 16.00
        loweLimit =  7399.43

    elif salary >= 8601.51 and salary < 10298.35:
        fixedQuota = 786.55
        percentageSuplus = 17.92
        loweLimit =  8601.51

    elif salary >= 10298.36 and salary < 20770.29:
        fixedQuota = 1090.62
        percentageSuplus = 21.36
        loweLimit =  10298.36

    elif salary >= 20770.30 and salary < 32736.83:
        fixedQuota = 3327.42
        percentageSuplus = 23.52
        loweLimit =  20770.30

    elif salary >= 32736.84:
        fixedQuota = 6141.95
        percentageSuplus = 30.00
        loweLimit =  32736.84


    ISR = fixedQuota + (salary - loweLimit) * (percentageSuplus) /100
    return ISR

# 5. Operations with text
def OperationWhitText(num1, num2):
    result = 0
    operation = input("Chosse your operation \n - Add\n - Subtract\n - Multiply\n - Split\nOperation: ")
    if operation == "Add" or operation == "add":
        result = num1 + num2
    elif operation == "Subtract" or operation == "subtract":
        result = num1 - num2
    elif operation == "Multiply" or operation == "multiply":
        result = num1 * num2
    elif operation == "Split" or operation == "split":
        result = num1 / num2
    
    print("The operation that you selected is: ", operation)
    print("Your result is: ", result)

# 6. BMI
def BMI(height, weight):
    height = float(input("Enter your height on m: "))
    weight = float(input("Enter your weight on kg: "))

    if height == 0 or weight == 0:
        return "No data can be zero."

    bmi = weight / height**2
    print ("Your BMI is ", bmi)
    print("Your BMI category is: ")
    if bmi < 16:
        print("Hospital admission criteria.")
    elif 16 <= bmi < 17:
        return "Underweight."
    elif 17 <= bmi < 18:
        return "Low weight."
    elif 18 <= bmi < 25:
        return "Normal weight (“healthy”)."
    elif 25 <= bmi < 30:
        return "Overweight (Grade I obesity)."
    elif 30 <= bmi < 35:
        return "Chronic overweight (Grade II obesity)."
    elif 35 <= bmi < 40:
        return "Premorbid obesity (Grade III obesity)."
    else:
        return "Morbid obesity (Grade IV obesity)."

# 7. Solved second degree equation
def SolvedSecondDegreeEquation():
    a = float(input("Enter the value of 'a': "))
    b = float(input("Enter the value of 'b': "))
    c = float(input("Enter the value of 'c': "))
    if a == 0 or b == 0 or c == 0:
        print("No number can be zero.")

    d = b**2 - 4*a*c

    if d < 0:
        print("The result of de equation, are not real numbers.")
    
    if d == 0:
        print("The solutions are equals, X = ", ((-b + d) / (2 * a)))
    else:
        print("The solution is: \nX1 = ", (-b + d**0.5) / (2 * a) , "\nX2 = " , (-b - d**0.5) / (2 * a))

# 8. Determine if the year is leap
def DetermineIfIsLeap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("The year is a leap year." )
    else:
        print( "The year is not a leap year.")

# 9. Detemine the type of polygon
def TypePolygon():
    l1 = input("First side value: ")
    l2 = input("Second side value: ")
    l3 = input("Third side value: ")
    l4 = input("Fourth side value: ")

    if l1 == 0 or l2 == 0 or l3 == 0 or l4 == 0:
        print("No side can be zero")
        return None
    else:
        if l1 == l2 and l2 == l3 and l3 == l4:
            print("The polygon is a aquare")
            return None
        elif l1 == l3 and l2 == l4 :
            print("The polygon is a rectangle")
            return None
        else:
            print("The polygon is other type of ring")

# 10. Grade of efficiency
def Efficiency():
    production = int(input("Production parts: "))
    defective = int(input("Defective parts: "))

    if defective <= 0 and production <= 0:
        print("No values can be zero")
    else:
        grade = "5"
        if production > 10000 and defective < 200 :
            grade = "8" 
        elif  production > 10000:
            grade = "7"
        elif defective < 200:
            grade = "6"

        print("The grade of production is: Grade", grade)

# Main menu
option = ""
while option != "S":
    print("\n--- Main Menu ---")
    print("[1] Calculate the maximun value")
    print("[2] Calculate seconds to minutes")
    print("[3] Billing with details")
    print("[4] Calculate ISR")
    print("[5] Operations with text")
    print("[6] BMI category")
    print("[7] Sover second grade degree equation")
    print("[8] The year is leap?")
    print("[9] What type of polygon is this?")
    print("[10] Grade of efficiency")
    print("[S] Exit")

    option = input("Select an option: ").upper()

    if option == "1":
        numA = int(input("Enter the number A: "))
        numB = int(input("Enter the number B: "))
        numC = int(input("Enter the number C: "))
        print("The maximun value is: ", MaximumValue(numA, numB, numC))
    elif option == "2":
        SecondsToMinutes(int(input("Enter your seconds to convert: ")))
    elif option == "3":
        BillingWithDetails(float(input("Enter the cost of the product: ")), int(input("Quantity the products: ")))
    elif option == "4":
        isr = ISR(float(input("Enter your salary: ")))
        print("Your ISR is: ", isr )
    elif option == "5":
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        OperationWhitText(num1, num2)
    elif option == "6":
        print(BMI())
    elif option == "7":
        SolvedSecondDegreeEquation()
    elif option == "8":
        DetermineIfIsLeap(float(input("Enter the year to analyze: ")))
    elif option == "9":
        TypePolygon()
    elif option == "10":
        Efficiency()
    elif option == "S":
        print("Exiting the program...")
    else:
        print("Invalid option, please try again.")
