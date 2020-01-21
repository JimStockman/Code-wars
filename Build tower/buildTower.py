def tower_builder(n_floors):
  tower = []

  if n_floors == 0: return []

  for i in range(n_floors):
    # 2n - 1
    tower.append( ((i*2*'*') + '*').center( (n_floors * 2) - 1))

  return tower

for floor in tower_builder(10) : print(floor) 
