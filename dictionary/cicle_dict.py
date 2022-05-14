store = [
    {"name":"Яблоки", "price":"100", "available": 40},
    {"name":"Апельсины", "price":"200", "available": 20},
    {"name":"Гранаты", "price":"400", "available": 5},
]

for fruit in store:
  if fruit['available'] > 5:
    print(fruit['name'], fruit['price'])