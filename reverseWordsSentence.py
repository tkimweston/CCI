def reverseWordsSentence(str):
    s = list(str)
    left = 0
    right = len(s) - 1
    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    left = 0
    for i in range(len(s)):
        if s[i] == ' ':
            right = i - 1
            while left <= right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            left = i + 1

    right = len(s) - 1
    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return "".join(s)

s = "Hello World"
print(s)
print(reverseWordsSentence(s))

s = "This is the best algorithm for Facebook phone interview"
print(s)
print(reverseWordsSentence(s))

