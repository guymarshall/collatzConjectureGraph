def collatz_steps(number: int) -> int:
    steps = 0

    while number > 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = (3 * number) + 1
        steps += 1
    
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
    
    return max_number