'''WAP for function returns the array of factorial of the element'''

def factorial_array(arr):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1)

    return [factorial(num) for num in arr]

input_array = [1,2,3,4,5,6,7]
result_array = factorial_array(input_array)

print(f"Input Array: {input_array}")
print(f"Factorial Array: {result_array}")
