# Use iterator to get the first matched item without "break" statement and flags.
items = ['book','apple','cup','rock']

def is_short(item:str)->bool:
  return len(item)<4

try:
  matched = next(
    item for item in items if is_short(item)
  )

  print('The first matched item is', matched)
except StopIteration:
  raise 'No one matched!'