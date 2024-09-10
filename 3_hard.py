data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


#res = 0
#for i in range(len(data_structure)):
#  if data_structure[i].isdigit():
#    res += data_structure[i]
#  elif data_structure[i].isalnum():
#    res += len(data_structure[i])

def sum_list(list):
  res = 0

  if len(list) == 0:
    return res
  for i in range(len(data_structure)):
    if type(data_structure[i])== int():
      res += data_structure[i]
    elif type(data_structure[i]) == str():
      res += len(data_structure[i])
    else: return res + sum_list(data_structure[i])

x = sum_list(data_structure)
print(x)
