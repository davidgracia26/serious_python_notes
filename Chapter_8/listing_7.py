from first import first

print(first([0, False, None, [], (), 42]))
print(first([-1, 0, 1, 2]))
print(first([-1, 0, 1, 2], key=lambda x: x > 0))