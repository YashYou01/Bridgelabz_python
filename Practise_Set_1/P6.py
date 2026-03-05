a = int(input("Enter start number: "))
b = int(input("Enter end number: "))

count = 0

for num in range(a, b + 1):
    if num > 1:
        is_prime = True
        
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            count += 1

print("Number of primes =", count)