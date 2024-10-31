import pandas as pd

# Function to display initial rows based on user input
def display_initial_rows(data):
    while True:
        user_input = input("Enter the number of rows to display (or type 'all' to see all rows, press Enter to skip): ").strip().lower()
        
        if user_input == "":
            print("No rows will be displayed.")
            break
        elif user_input == "all":
            print("Displaying all rows:")
            print(data)
            break
        elif user_input.isdigit():
            num_rows = int(user_input)
            if num_rows > 0:
                print(f"Displaying the first {num_rows} rows:")
                print(data.head(num_rows))
                break
            else:
                print("Please enter a positive number.")
        else:
            print("Invalid input. Please enter a positive number, 'all', or press Enter to skip.")

# Function to exit the program
def exit_program(data):
    print("Exiting the program. Goodbye!")
    exit()  # Cleanly exit the program

# Function to create a pivot table showing the number of unique employees by region
def sales_by_region_order_type(data):
    try:
        # Create pivot table for unique employee counts by region
        pivot_table = data.pivot_table(
            index="region",  # Group by region
            values="employee_id",  # Unique employees per region
            aggfunc="nunique"  # Count unique employee IDs
        )
        print("Number of unique employees by region:")
        print(pivot_table)
    except KeyError:
        print("Error: Required columns (region, employee_id) not found in the data.")

# Function to display the menu and get user selection
def display_menu():
    menu_options = (
        ("Show the first n rows of sales data", display_initial_rows),
        ("Show the number of employees by region", sales_by_region_order_type),
        ("Exit the program", exit_program)
    )

    # Display the menu options
    print("\nSelect an option:")
    for i, (description, _) in enumerate(menu_options, start=1):
        print(f"{i}. {description}")

    # Validate and get user selection
    while True:
        try:
            choice = int(input("Enter the number of your selection: "))
            if 1 <= choice <= len(menu_options):
                return menu_options[choice - 1][1]  # Return the selected function
            else:
                print("Invalid choice. Please enter a number from the menu options.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main function to loop and process menu selections
def main():
    # Load a sample DataFrame (or load your actual data here)
    data = pd.DataFrame({
        'region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
        'employee_id': [1, 2, 3, 4, 1, 2, 3, 4, 5, 6],
        'quantity': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
        'unit_price': [100, 200, 150, 300, 250, 400, 350, 500, 450, 550]
    })

    while True:
        # Display menu and get the selected function
        selected_function = display_menu()
        # Call the selected function
        selected_function(data)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
