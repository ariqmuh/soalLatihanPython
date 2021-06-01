numbers = [41, 5, 1, 3, 89, 32]
print("Numbers = {}".format(numbers))

for num in numbers:
    numbers.sort()
    print("Minimum Value = {}".format(numbers[0]))
    print("Maximum Value = {}".format(numbers[-1]))
    break
    
