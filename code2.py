def fibonacci_generator():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b


# Пошук першого числа Фібоначчі, яке закінчується на певну цифру (наприклад, 8)
fib = fibonacci_generator()
count = 0
for num in fib:
  if num % 10 == 8 and num > 0:
    print(
        f"Знайдено число з патерном (закінчується на 8): {num} (після"
        f" перевірки {count} елементів)"
    )
    break
  count += 1