import pandas as pd

def display_initial_rows(data):
    """
    Prompts the user to specify how many initial rows of the DataFrame they want to view.
    Validates user input and handles invalid entries.
    """
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
                print("Enter a positive number.")
        else:
            print("Invalid input. Enter a positive number, 'all', or press Enter to skip.")

def main():
    data = pd.DataFrame({
        'column1': range(1, 11),
        'quantity': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
        'unit_price': [100, 200, 150, 300, 250, 400, 350, 500, 450, 550]
    })

    while True:
        display_initial_rows(data)

if __name__ == "__main__":
    main()
