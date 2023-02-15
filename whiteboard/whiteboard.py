# Write a function that returns the number of occurrences of an element in an array.
# Examples
# sample = [0, 1, 2, 2, 3]
# number_of_occurrences(0, sample) == 1
# number_of_occurrences(4, sample) == 0
# number_of_occurrences(2, sample) == 2
# number_of_occurrences(3, sample) == 1


def number_of_occurrences(int, sample):
    count = 0
    for n in sample:
        if n == int:
            count += 1
    return count

sample = [0, 1, 2, 2, 3]

print(number_of_occurrences(0, sample))

print(number_of_occurrences(4, sample))

print(number_of_occurrences(2, sample))

print(number_of_occurrences(3, sample))


def number_of_occurrences(target, alist):
    hash_map = {target:0}
    for num in alist:
        hash_map[num] = hash_map.get(num,0)+1
    return hash_map[target]

sample = [0, 1, 2, 2, 3]

print(number_of_occurrences(0, sample))

print(number_of_occurrences(4, sample))

print(number_of_occurrences(2, sample))

print(number_of_occurrences(3, sample))


def number_of_occurrences(int, sample):
    count = 0
    return sum(1 for n in sample if n == int)
sample = [0, 1, 2, 2, 3]

print(number_of_occurrences(0, sample))

print(number_of_occurrences(4, sample))

print(number_of_occurrences(2, sample))

print(number_of_occurrences(3, sample))