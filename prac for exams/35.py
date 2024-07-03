def print_summation_pattern(N):
    total = 0
    for i in range(1, N + 1):
        total += i
        print(f"Sum of natural numbers up to {i}:", total)

# Read the number N
N = int(input("Enter a number N: "))

# Print the summation pattern
print_summation_pattern(N)
