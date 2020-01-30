def unique_in_order(iterable):
  if len(iterable) >= 2:
    newList = [iterable[0]]
    for d in iterable:
      if d != newList[-1]:
        newList.append(d)
    return newList
  elif len(iterable) == 1:
    return [iterable]
  else:
    return []