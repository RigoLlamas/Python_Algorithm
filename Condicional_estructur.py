# 1. From the natural numbers A, B and C, print the maximum value
def maximumValue(NumA, NumB, NumC):
    print("\n--- Calculate the Maximun Value ---")
    if NumA >= NumB and NumA >= NumC:
        return NumA
    elif NumB >= NumC:
        return NumB
    else:
        return NumC

# 2. Convert seconds to minutes:
#    - Do not use the % operator
def secondsToMinutes(seconds):
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

def billingWithDetails(prices, quantity):
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
    

# Main menu
option = ""
while option != "S":
    print("\n--- Main Menu ---")
    print("[1] Calculate the maximun value")
    print("[2] Calculate seconds to minutes")
    print("[3] Billing with details")
    print("[S] Exit")

    option = input("Select an option: ").upper()

    if option == "1":
        NumA = int(input("Enter the number A: "))
        NumB = int(input("Enter the number B: "))
        NumC = int(input("Enter the number C: "))
        print("The maximun value is: ", maximumValue(NumA, NumB, NumC))
    elif option == "2":
        secondsToMinutes(int(input("Enter your seconds to convert: ")))
    elif option == "3":
        billingWithDetails(float(input("Enter the cost of the product: ")), int(input("Quantity the products: ")))
    elif option == "S":
        print("Exiting the program...")
    else:
        print("Invalid option, please try again.")
