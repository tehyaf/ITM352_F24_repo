import pandas as pd

def display_initial_rows(data):
    pass

def exit_program(data):
    print("Exiting the program. Goodbye!")
    exit()

def sales_by_region_order_type(data):
    pass

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

menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Show the number of employees by region", sales_by_region_order_type),
    ("Generate a custom pivot table", generate_custom_pivot_table),
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
