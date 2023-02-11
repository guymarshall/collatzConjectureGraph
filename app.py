import matplotlib.pyplot as plt

def plot_graph(x_axis: list, y_axis: list, x_label: str, y_label: str, title: str):
    plt.plot(x_axis, y_axis, linewidth=0.2)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


def collatz_steps(number: int) -> int:
    steps = 0

    while number > 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = (3 * number) + 1
        steps += 1
    
    return int(steps)


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
        x_axis = list(range(1, number + 1))
        y_axis = []

        for i in range(1, number + 1):
            y_axis.append(collatz_steps(i))
        
        plot_graph(x_axis, y_axis, "Starting Number", "Number of Steps", "A graph to show the relationship between the starting number and the number of steps")
    elif decision == "max":
        x_axis = list(range(1, number + 1))
        y_axis = []

        for i in range(1, number + 1):
            y_axis.append(collatz_max(i))
        
        plot_graph(x_axis, y_axis, "Starting Number", "Maximum Number Reached", "A graph to show the relationship between the starting number and max number reached")
    else:
        print("Invalid input. Please enter either 'steps' or 'max'.")
        quit()
    

if __name__ == "__main__":
    main()