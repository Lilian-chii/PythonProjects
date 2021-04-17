  
prime_numbers = []
def prime_numbers_generation (lower_limit, n):
    for number in range (n+1):
        if number >1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                prime_numbers.append(number)
    return prime_numbers


result = prime_numbers_generation (lower_limit =1, n = 200)
print(f'Prime numbers: {result}')
