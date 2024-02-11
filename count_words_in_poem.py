word_count = {}
with open("poem.txt", "r") as f:
    for i in f:
        words = i.split(" ")
        for word in words:
            word = word.replace("\n", " ")
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
print(dict(word_count))
