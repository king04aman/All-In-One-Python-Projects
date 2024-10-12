def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:
    if number_of_people < 1:
        raise ValueError('Number of people should be at least one.')

    # Calculate the share per person
    share_per_person: float = total_amount / number_of_people

    # Print the results
    print(f'Total expenses: {currency}{total_amount:,.2f}')
    print(f'Number of people: {number_of_people}')
    print(f'Each person should pay: {currency}{share_per_person:,.2f}')


def main() -> None:
    try:
        # Input for total amount
        total_amount: float = float(input('Enter the total amount of the expense: '))
        
        # Input for number of people
        number_of_people: int = int(input('Enter the number of people sharing the expense: '))
        
        # Call the function to calculate the split with currency set to rupees
        calculate_split(total_amount, number_of_people, currency="₹")
        
    except ValueError as e:
        print(f'Error: {e}')


# Run the main function
if __name__ == "__main__":
    main()
