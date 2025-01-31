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



# Main menu
option = ""
while option != "S":
    print("\n--- Main Menu ---")
    print("[1] Calculate the maximun value")
    print("[2] Calculate seconds to minutes")
    print("[S] Exit")

    option = input("Select an option: ").upper()

    if option == "1":
        NumA = int(input("Enter the number A: "))
        NumB = int(input("Enter the number B: "))
        NumC = int(input("Enter the number C: "))
        print("The maximun value is: ", maximumValue(NumA, NumB, NumC))
    elif option == "2":
        secondsToMinutes(int(input("Enter your seconds to convert: ")))
    elif option == "S":
        print("Exiting the program...")
    else:
        print("Invalid option, please try again.")
