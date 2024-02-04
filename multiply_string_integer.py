# Solution to multiply string and integer
def solution(s, i):
    numbers = {"one": 1, "two": 2}
    if s in numbers:
        return int(numbers[s] * i)
    else:
        return ""


a = solution("two", 2)
print(a)
