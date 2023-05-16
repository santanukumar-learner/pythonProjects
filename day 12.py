'''enemies = 1
def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")
  if enemies < 3:
    enemy = 5
increase_enemies()
print(enemy)'''
i = 50


def foo():
  i = 100
  return i


print(foo())
print(i)