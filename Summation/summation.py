def summation(num):
  return sum(d for d in range(num + 1))

# Range will generate an array populated by ordered integers
def best_summation(num):
  return sum(range(num+1))

print(best_summation(10))
