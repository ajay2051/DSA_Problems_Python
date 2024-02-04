sample_list = [64, 25, 12]

for i in range(len(sample_list)):
    for j in range(i + 1, len(sample_list)):

        if sample_list[i] > sample_list[j]:
            sample_list[i], sample_list[j] = sample_list[j], sample_list[i]


print(sample_list)
