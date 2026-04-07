def is_prime(n):
    #Returns True if n is a prime number, else False 
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Prime" if is_prime(num) else "Not prime")
