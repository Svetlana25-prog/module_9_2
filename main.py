first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']

second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = []
for f in first_strings:
    if len(f) >= 5:
        first_result.append(len(f))

print(first_result)

second_result = []
for f in first_strings:
    for s in second_strings:
        if len(f) == len(s):
            second_result.append((f, s))

print(second_result)

third_result = {}
for i in first_strings + second_strings:
    if len(i) % 2 == 0:
        third_result[i] = len(i)

print(third_result)