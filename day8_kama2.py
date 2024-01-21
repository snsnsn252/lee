# kama
# https://kamacoder.com/problempage.php?pid=1065

n = int(input())
s = input()

def reverse(s, left, right):
    s = list(s)
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1 
        right -= 1
    return ''.join(s)

s = reverse(s, 0, len(s) - 1)
sub1 = reverse(s[:n], 0, len(s[:n]) - 1)
sub2 = reverse(s[n:], 0, len(s[n:]) - 1)
print(sub1 + sub2)