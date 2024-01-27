sample = [20, 12, 45, 20]

duplicates = []

for i in range(0, len(sample)):
    for j in range(i + 1, len(sample)):
        if sample[i] == sample[j]:
            duplicates.append(sample[i])
print(duplicates)

duplicates = [sample[i] for i in range(len(sample)) for j in range(i + 1, len(sample)) if sample[i] == sample[j]]
print(duplicates)
