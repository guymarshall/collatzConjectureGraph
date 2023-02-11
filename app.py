def collatz_steps(number: int) -> int:
    steps = []

    while number > 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = (3 * number) + 1
        steps.append(number)
    
    return steps

def collatz_max(number: int) -> int:
    max_number = number

    while number > 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = (3 * number) + 1
        if number > max_number:
            max_number = number
    
    return int(max_number)

def main():
    number = int(input("Enter a whole number greater than 0: "))
    decision = input("Would you like to calculate 'steps' or 'max'? ").lower()

    if decision == "steps":
        result = collatz_steps(number)
        print(f"Steps for {number} is {result}")
    elif decision == "max":
        result = collatz_max(number)
        print(f"Max for {number} is {result}")
    else:
        print("Invalid input. Please enter either 'steps' or 'max'.")
        quit()
    

if __name__ == "__main__":
    main()