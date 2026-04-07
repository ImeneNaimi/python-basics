def fibonacci(n):
    #Return Fibonacci sequence up to n terms.
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]


if __name__ == "__main__":
    terms = int(input("Enter number of terms: "))
    print(fibonacci(terms))
