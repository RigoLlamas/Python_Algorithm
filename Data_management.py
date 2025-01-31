# 1. Request the RFC and print its homoclave (Only the last 3 characters)
def print_homoclave():
    print("\n--- Print Homoclave ---")
    RFC = input("Enter your RFC: ")
    if len(RFC) >= 13:
        print("Your homoclave is:", RFC[-3:])  # Extracts the last 3 characters
    else:
        print("Invalid RFC, it must be at least 13 characters long.")

# 2. Request a string "text" and a string "query".
# If the second string appears exactly within the first, display True; otherwise, False.
def find_text():
    print("\n--- Find text within another text ---")
    text = input("Enter the base text: ")
    query = input("Enter the text fragment to search for: ")
    print("Does it exist in the text? :", query in text)  # Checks if the query is in the text

# 3. Request the full name of a person:
#    - Remove unnecessary spaces from the text.
#    - Determine if all entered letters are lowercase.
#    - Determine if the name starts with an unaccented vowel.
#    - Determine how many unaccented vowels exist.
def name_analysis():
    print("\n--- Name Analysis ---")
    name = input("Enter your full name: ").strip()  # Removes unnecessary spaces

    print("Are all letters lowercase?", name.islower())  # Checks if everything is lowercase
    print("Does it start with an unaccented vowel?", name.lower().startswith(("a", "e", "i", "o", "u")))

    # Count unaccented and accented vowels
    unaccented_vowels = sum(name.count(v) for v in "aeiou")
    accented_vowels = sum(name.count(v) for v in "áéíóú")

    print("Total vowels:", unaccented_vowels + accented_vowels)
    print("Accented vowels:", accented_vowels)
    print("Unaccented vowels:", unaccented_vowels)

# 4. The final grade of a student is an integer obtained by averaging the grades
#    of their exams, assignments, projects, and contests. The “.5” rounds up.
def calculate_final_grade():
    print("\n--- Calculate Final Grade ---")
    print("Enter the student's grades")
    exam = int(input("Exam grade: "))
    assignments = int(input("Assignments grade: "))
    projects = int(input("Projects grade: "))
    contests = int(input("Contests grade: "))

    total_score = exam + assignments + projects + contests
    print("Total score obtained:", total_score, "/ 400")

    final_grade = total_score / 4
    print("The student has a final rounded grade of:", int(final_grade + 0.5))  # Rounding

# 5. Number of complete units (without fractional part) of a product that can be purchased
#    if I have X amount of money and the product costs Y. X and Y may include cents.
def calculate_purchasable_products():
    print("\n--- Calculate Purchasable Products ---")
    product_price = float(input("Product price: "))
    available_money = float(input("Current amount of money: "))

    if product_price > 0:
        print("The customer can buy up to", int(available_money / product_price), "products.")
    else:
        print("The product price must be greater than 0.")

# 6. Request the data of a person separately: first name, last name, and middle name.
#    Print their full name in a single line, including the corresponding spaces.
#    Use concatenation.
def print_full_name():
    print("\n--- Print Full Name ---")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    middle_name = input("Enter your middle name: ")

    print("Full name:", first_name + " " + last_name + " " + middle_name)  # Concatenation

# 7. Calculate the length of the hypotenuse of a right triangle, given the lengths of the legs,
#    using the Pythagorean theorem. Use the power operator **.
def calculate_hypotenuse():
    print("\n--- Calculate Hypotenuse ---")
    print("Enter the sides of the triangle to calculate the hypotenuse")
    adjacent_leg = float(input("Value of the adjacent leg (a): "))
    opposite_leg = float(input("Value of the opposite leg (b): "))

    hypotenuse = (adjacent_leg**2 + opposite_leg**2)**(1/2)  # Pythagorean theorem formula
    print("The hypotenuse length is:", hypotenuse)

# 8. An hour has a certain number of seconds.
#    Request the total number of seconds from the user and display the remaining seconds
#    after subtracting the seconds that make up complete hours.
#    Use the modulus operator.
def convert_seconds():
    print("\n--- Convert Seconds to Hours ---")
    total_seconds = int(input("Enter the number of seconds to convert: "))

    hours = total_seconds // 3600  # Calculate complete hours
    remaining_seconds = total_seconds % 3600  # Calculate remaining seconds

    print("Total seconds entered:", total_seconds)
    print("Complete hours:", hours)
    print("Remaining seconds:", remaining_seconds)

# Main menu
option = ""
while option != "S":
    print("\n--- Main Menu ---")
    print("[1] Print homoclave")
    print("[2] Find text in another text")
    print("[3] Name analysis")
    print("[4] Calculate final grade")
    print("[5] Calculate purchasable products")
    print("[6] Print full name")
    print("[7] Calculate triangle hypotenuse")
    print("[8] Convert seconds after complete hours")
    print("[S] Exit")

    option = input("Select an option: ").upper()

    if option == "1":
        print_homoclave()
    elif option == "2":
        find_text()
    elif option == "3":
        name_analysis()
    elif option == "4":
        calculate_final_grade()
    elif option == "5":
        calculate_purchasable_products()
    elif option == "6":
        print_full_name()
    elif option == "7":
        calculate_hypotenuse()
    elif option == "8":
        convert_seconds()
    elif option == "S":
        print("Exiting the program...")
    else:
        print("Invalid option, please try again.")
