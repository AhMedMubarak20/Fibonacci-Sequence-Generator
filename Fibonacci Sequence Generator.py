def generate_fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_term = sequence[i-1] + sequence[i-2]
        sequence.append(next_term)
    return sequence

num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))
fib_sequence = generate_fibonacci(num_terms)
print("Fibonacci Sequence:", fib_sequence)
