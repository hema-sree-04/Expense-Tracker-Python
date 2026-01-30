FILE_NAME = "expenses.txt"

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    note = input("Enter note: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{amount},{category},{note}\n")

    print("Expense added!")

def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            print("\nAll Expenses:")
            for line in file:
                amount, category, note = line.strip().split(",")
                print(f"{amount} | {category} | {note}")
    except FileNotFoundError:
        print("No expenses found.")

def total_expense():
    total = 0
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                total += float(line.strip().split(",")[0])
        print(f"Total Expense: {total}")
    except FileNotFoundError:
        print("No expenses found.")

def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

main()
