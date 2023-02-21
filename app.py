import matplotlib.pyplot as plt
from numba import jit
from multiprocessing import Pool, cpu_count

def plot_graph(x_axis: list, y_axis: list, x_label: str, y_label: str, title: str):
    plt.scatter(x_axis, y_axis, s=1)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


@jit
def collatz_steps(number: int) -> int:
    steps = 0

    while number > 1:
        if number % 2 == 0:
            number = number >> 1
        else:
            number = (3 * number) + 1
        steps += 1

    return steps


def main():
    number = int(input("Enter a whole number greater than 0: "))

    x_axis = list(range(1, number + 1))
    y_axis = []

    with Pool(processes=cpu_count()) as pool:
        y_axis = pool.map(collatz_steps, range(1, number + 1))

    plot_graph(x_axis, y_axis, "Starting Number", "Number of Steps", "A graph to show the relationship between the starting number and the number of steps")


if __name__ == "__main__":
    main()