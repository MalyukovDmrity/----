def prefix(s):
  p = [0] * len(s)
  for i in range(1, len(s)):
    k = p[i - 1]
    while k > 0 and s[k] != s[i]:
      k = p[k - 1]
    if s[k] == s[i]:
      k += 1
    p[i] = k
  return p

text = input()
a = prefix(text)[-1]
n = len(text)
ans = n - a
print(ans)