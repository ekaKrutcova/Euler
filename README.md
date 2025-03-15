# Project Euler Solutions

A collection of solutions to Project Euler problems implemented in Python.

[Project Euler](https://projecteuler.net) is a series of challenging mathematical/computer programming problems that require more than just mathematical insights to solve.

## 📁 Project Structure

```
Euler/
├── euler_project.py    # Main file containing all problem solutions
├── decorators.py       # Utility decorators for timing function execution
└── README.md          # This file
```

## 🚀 Features

- **Time Execution Tracking**: All solutions use the `@time_execution` decorator to measure and log execution time
- **Well-Documented**: Each problem includes detailed docstrings explaining the problem statement and approach
- **Modular Design**: Helper functions are separated for reusability
- **Type Hints**: Functions include type annotations for better code clarity

## 📋 Solved Problems

The project includes solutions for the following Project Euler problems:

- **Problem 0**: Sum of squares of odd natural numbers
- **Problem 1**: Multiples of 3 or 5
- **Problem 2**: Even Fibonacci numbers
- **Problem 3**: Largest prime factor
- **Problem 4**: Largest palindrome product
- **Problem 5**: Smallest multiple
- **Problem 6**: Sum square difference
- **Problem 7**: 10001st prime number
- **Problem 8**: Largest product in a series
- **Problem 9**: Special Pythagorean triplet
- **Problem 10**: Summation of primes
- **Problem 11**: Largest product in a grid
- **Problem 12**: Highly divisible triangular number
- **Problem 13**: Large sum
- **Problem 14**: Longest Collatz sequence
- **Problem 15**: Lattice paths
- **Problem 16**: Power digit sum
- **Problem 17**: Number letter counts

## 🛠️ Requirements

- Python 3.x
- No external dependencies required (uses only standard library)

## 💻 Usage

### Running All Problems

Execute the main script to run all implemented problems:

```bash
python euler_project.py
```

### Running Individual Problems

You can import and run specific problems:

```python
from euler_project import multiples_of_3_or_5, even_fibonacci_numbers

# Run Problem 1
result = multiples_of_3_or_5(1000)
print(result)

# Run Problem 2
result = even_fibonacci_numbers(4000000)
print(result)
```

### Custom Parameters

Most functions accept parameters to customize the problem:

```python
# Find sum of multiples below 100
result = multiples_of_3_or_5(100)

# Find largest palindrome from product of two 4-digit numbers
result = find_largest_palindrome(4)
```

## 🔧 Helper Functions

The project includes several utility functions:

- `get_factors(x)`: Returns prime factors of a number
- `is_palindrom(candidate)`: Checks if a number/string is a palindrome
- `is_there_div_in_list(applicant, numbers)`: Checks divisibility
- `product(list_for_product)`: Calculates product of a list
- `largest_product_matrix_series()`: Finds largest product in a matrix series

## ⏱️ Performance Tracking

The `@time_execution` decorator automatically logs execution time for each function:

```
multiples_of_3_or_5 with args: (1000,), kwargs: {} execution took 0.00012 sec
```

## 📝 Notes

- Some problems are commented out in the main execution block due to long execution times
- Solutions prioritize correctness and readability
- Performance optimizations are applied where appropriate

## 🔗 Resources

- [Project Euler Website](https://projecteuler.net)
- [Project Euler Archives](https://projecteuler.net/archives)

## 📄 License

This project is for educational purposes. Please respect Project Euler's policy of not sharing solutions publicly for problems beyond #100.
