import pandas as pd

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

def exit_program(data):
    print("Exiting the program. Goodbye!")
    exit()

def sales_by_region_order_type(data):
    try:
        pivot_table = data.pivot_table(
            index="region",
            values="employee_id",
            aggfunc="nunique"
        )
        print("Number of unique employees by region:")
        print(pivot_table)
    except KeyError:
        print("Error: Required columns (region, employee_id) not found in the data.")

def get_user_selection(options, prompt): 
    print(prompt)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    choice = input("Enter the number(s) of your choice(s), separated by commas: ")
    selected = [options[int(i) - 1] for i in choice.split(',') if i.strip().isdigit() and int(i) - 1 < len(options)]
    
    return selected

def generate_custom_pivot_table(data):
    row_options = list(data.columns)
    rows = get_user_selection(row_options, "Select rows:")
    if not rows:
        print("Row selection is required. Please try again.")
        return

    col_options = [col for col in row_options if col not in rows]
    cols = get_user_selection(col_options, "Select columns (optional):")

    value_options = list(data.select_dtypes(include=['number']).columns)
    values = get_user_selection(value_options, "Select values:")
    if not values:
        print("Value selection is required. Please try again.")
        return

    agg_options = ['sum', 'mean', 'count']
    agg_func = get_user_selection(agg_options, "Select an aggregation function:")
    if not agg_func:
        print("Aggregation function selection is required. Please try again.")
        return
    agg_func = agg_func[0]

    pivot_table = pd.pivot_table(
        data, 
        index=rows, 
        columns=cols if cols else None, 
        values=values, 
        aggfunc=agg_func
    )
    print("Generated Custom Pivot Table:")
    print(pivot_table)

def total_sales_by_region(data):
    data['sales'] = data['quantity'] * data['unit_price']
    total_sales = data.groupby('region')['sales'].sum()
    print("Total Sales by Region:")
    print(total_sales)

def avg_order_quantity_by_employee(data):
    avg_quantity = data.groupby('employee_id')['quantity'].mean()
    print("Average Order Quantity by Employee:")
    print(avg_quantity)

menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Show the number of employees by region", sales_by_region_order_type),
    ("Generate a custom pivot table", generate_custom_pivot_table),
    ("Total sales by region", total_sales_by_region),
    ("Average order quantity by employee", avg_order_quantity_by_employee),
    ("Exit the program", exit_program)
)

def display_menu():
    print("\nSelect an option:")
    for i, (description, _) in enumerate(menu_options, start=1):
        print(f"{i}. {description}")
    
    while True:
        try:
            choice = int(input("Enter the number of your selection: "))
            if 1 <= choice <= len(menu_options):
                return menu_options[choice - 1][1]
            else:
                print("Invalid choice. Please enter a number from the menu options.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    data = pd.DataFrame({
        'region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
        'employee_id': [1, 2, 3, 4, 1, 2, 3, 4, 5, 6],
        'quantity': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
        'unit_price': [100, 200, 150, 300, 250, 400, 350, 500, 450, 550]
    })

    while True:
        selected_function = display_menu()
        selected_function(data)

if __name__ == "__main__":
    main()
