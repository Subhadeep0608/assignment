def palindrome_primes(prime_numbers):
    p_p = []
    for prime in prime_numbers:
        if str(prime) == str(prime)[::-1]:  
            p_p.append(prime)
    return p_p
    
def first_n_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_list = []
    num = 2
    while len(prime_list) < n:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list


n=int(input("enter a number :"))
l=[]
l=first_n_primes(n)
print(palindrome_primes(l))