def namelist(names):
  if len(names) ==  0 or names == None:
    return ''

  else: 
    sentence = ''
    for i in range(len(names) - 1):
      if i != len(names) - 2:
        sentence += names[i]['name'] + ', '
      elif i == len(names) - 2:
        sentence += names[i]['name'] + ' & '

  return sentence + names[-1]['name']

# ///////////////////////////////////////////////////////////////////////

def best_namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''


names = [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]

print(best_namelist(names))
