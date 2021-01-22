def recursiveRemove(s, t):
  if t not in s:
    return 0
  possibleStartPoint = []
  tLen = len(t)
  for i in range(len(s) - tLen + 1):
    if (s[i: i + tLen] == t):
      possibleStartPoint.append(i)
  res = 0
  for i in possibleStartPoint:
    res = max(res, recursiveRemove(s[:i] + s[i+tLen:], t) + 1)
  return res

print(recursiveRemove("aabcbc","abc"))