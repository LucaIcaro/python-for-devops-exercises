# Write a generator that alternates between returning Even and Odd.

def evenodd():
    results = ["Even", "Odd"]
    i = 0
    while True:
        yield results[i%2]
        i += 1

results = evenodd()

print(next(results))
print(next(results))
print(next(results))
print(next(results))
print(next(results))