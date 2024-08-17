def abbreviate(s):
    if len(s) <= 10:
        return s
    return f"{s[0]}{len(s)-2}{s[-1]}"

n = int(input())

for i in range(n):
    s = str(input())
    print(abbreviate(s))