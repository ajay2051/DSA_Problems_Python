# Length of last word
def len_of_last(input_word):
    capital_letter = []
    for i in input_word:
        if i.isupper():
            capital_letter.append(i)
    r = input_word.split(capital_letter[-1])
    return len(r[-1]) + 1


print(len_of_last("ElephantLionmnAb"))
