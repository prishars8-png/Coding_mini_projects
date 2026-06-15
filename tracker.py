# creating a daily expense tracker to keep track of one's expenses in a day, a basic model
# By: Prisha Raja Sudhasini 
# Date: May 23rd, 2026

print("Welcome to Daily Expense Tracker\n")

print("Menu options")
print("1. Add your expenses")
print("2. View all expenses")
print("3. Calculate total and average of your expenses")
print("4. Clear all expenses")
print("5. Exit\n")

print("Enter an input from 1 to 5, according to the task that you want to do:")

expenses = []
tot = 0
average = 0
while True:
    num = int(input())
    if (num == 5):
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    elif (num == 1):
        new_num = float(input())
        expenses.append(new_num)
        print("Successfully added it to the list.")
    elif (num == 2):
        if (len(expenses) == 0):
            print("There is nothing in the expenses list.")
        else:
            print("Expenses:")
            for i in range(len(expenses)):
                print(f"{i + 1}. {expenses[i]}")
    elif (num == 3):
        if (len(expenses) == 0):
            print("Cannot calculate the sum and average because the expense list is empty.")
        else:
            tot = 0     #resets everytime

            for i in range(len(expenses)):
                tot += expenses[i]
            average = tot / len(expenses)
            print(f"Sum: {tot:.2f}")
            print(f"Average: {average:.2f}")
    elif (num == 4):
        expenses.clear()
        print("Expenses cleared!")
    else:
        print("Invalid number, press any number from 1 to 5.")



# FOR FUTURE UPGRADES:

# 1. Remove only one expense
# 2. Accept letters as input