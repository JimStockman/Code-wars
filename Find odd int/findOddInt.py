
# Count exists :)

def find_it(seq):
  if len(seq) == 1 : return seq[0]
  
  odds = []

  for i in range(len(seq)):
    if seq[i] not in odds:
      odds.append(seq[i])
    else :
      odds.pop(odds.index(seq[i]))
  
  return odds[0]

def best_find_it(seq):
  for n in seq:
    if seq.count(n) % 2 != 0 : return n


lists = [
  [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5],
  [1,1,2,-2,5,2,4,4,-1,-2,5],
  [20,1,1,2,2,3,3,5,5,4,20,4,5],
  [10],
  [1,1,1,1,1,1,10,1,1,1,1],
  [5,4,3,2,1,5,4,3,2,10,10]
]

for list in lists:
  print(best_find_it(list))