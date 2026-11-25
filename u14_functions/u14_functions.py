def count_target (values, target):
    count = 0

    for i in range(0, len(values)):
        if values[i] == target:
            count = count + 1

    return count

valuenums = [7, 3, 5, 7, 7, 3, 2]
target_value = 7

output = count_target(valuenums, target_value)
print(output)