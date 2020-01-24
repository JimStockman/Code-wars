def dig_pow(n, p):
  total = 0

  for d in str(n):
    total += int(d) ** p
    p+=1

  processed = total / n

  if processed - int(processed) != 0 :
    return -1
  else :
    return int(processed)

print(dig_pow(46288, 3))


def best_dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
    s += pow(int(c),p+i)
  return s/n if s%n==0 else -1