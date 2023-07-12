#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers

    if length == 0:
        print([])
        return

    if length == 1:
        print(fibonacci_sequence[:1])
        return

    if length == 2:
        print(fibonacci_sequence)
        return

    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    print(fibonacci_sequence)