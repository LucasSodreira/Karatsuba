import timeit
import random
import os

def generate_large_number(num_digits):
    # Gera um número aleatório com o número especificado de dígitos
    return random.randint(10 ** (num_digits - 1), 10 ** num_digits - 1)

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    # Encontrar o menor número de dígitos
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Dividir os números em partes
    a = x // 10**m
    b = x % 10**m
    c = y // 10**m
    d = y % 10**m

    # Recursivamente calcular as três multiplicações requeridas
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    # Calcular o resultado usando as três multiplicações
    result = ac * 10**(2*m) + ad_bc * 10**m + bd
    return result

def test_karatsuba(x, y):
    start_time_karatsuba = timeit.default_timer()
    karatsuba_result = karatsuba(x, y)
    end_time_karatsuba = timeit.default_timer()

    start_time_traditional = timeit.default_timer()
    traditional_result = x * y
    end_time_traditional = timeit.default_timer()

    karatsuba_time = end_time_karatsuba - start_time_karatsuba
    traditional_time = end_time_traditional - start_time_traditional

    # Escrever os resultados para um arquivo de texto
    with open('karatsuba_test_results.txt', 'a') as f:
        f.write(f"{'-' * 100}\n")
        f.write(f"| Karatsuba result: {karatsuba_result} | Traditional result: {traditional_result} | x: {x} | y: {y}\n")
        f.write(f"| Karatsuba time: {karatsuba_time:.6f} ms | Traditional time: {traditional_time:.6f} ms | \n ")
        f.write(f"{'-' * 100}\n")
        f.write("\n")

# Testes com números grandes
num1_10_digits = generate_large_number(10)
num2_10_digits = generate_large_number(10)

num1_50_digits = generate_large_number(50)
num2_50_digits = generate_large_number(50)

num1_100_digits = generate_large_number(100)
num2_100_digits = generate_large_number(100)

# Test cases
test_karatsuba(1234, 5678)
test_karatsuba(11111111, 22222222)
test_karatsuba(12345678, 87654321)

test_karatsuba(1234, 456789)
test_karatsuba(12345, 678)
test_karatsuba(12345, 78901234)

test_karatsuba(num1_10_digits, num2_10_digits)
test_karatsuba(num1_50_digits, num2_50_digits)
test_karatsuba(num1_100_digits, num2_100_digits)
