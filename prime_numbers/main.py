import timeit

py = timeit.timeit(
    "prime_number.prime_py(5000)", setup="import prime_number", number=100
)
cy = timeit.timeit(
    "prime_number.prime_cy(5000)", setup="import prime_number", number=100
)

print(f"Python- {py} sec and Cython- {cy} sec. Cython is {py/cy} times faster")
