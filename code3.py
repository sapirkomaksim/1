class SimpleTuringMachine:

  def __init__(self, tape, blank_symbol="_"):
    self.tape = list(tape)
    self.head_position = 0
    self.state = "q0"
    self.blank_symbol = blank_symbol

  def step(self):
    """Один крок машини Тюринга."""
    if self.head_position < 0:
      self.tape.insert(0, self.blank_symbol)
      self.head_position = 0
    elif self.head_position >= len(self.tape):
      self.tape.append(self.blank_symbol)

    current_symbol = self.tape[self.head_position]

    # Приклад правила: якщо у стані q0 бачимо '0', змінюємо на '1', рухаємось праворуч
    if self.state == "q0":
      if current_symbol == "0":
        self.tape[self.head_position] = "1"
        self.head_position += 1
        self.state = "q1"
      elif current_symbol == "1":
        # Створюємо спеціальний нескінченний цикл для демонстрації проблеми
        self.head_position -= 1  # Повертаємось назад, створюючи зациклення
        self.state = "q0"
      elif current_symbol == self.blank_symbol:
        self.state = "q_accept"  # Зупинка

  def run(self, max_steps=100):
    steps = 0
    while self.state not in ("q_accept", "q_reject") and steps < max_steps:
      self.step()
      steps += 1
    if steps >= max_steps:
      print(
          "[Симуляція] Досягнуто ліміт кроків — машина потрапила у нескінченний"
          " цикл."
      )
    else:
      print(f"[Симуляція] Машина зупинилася у стані '{self.state}' за кроків.")


# Тестування моделі
tm = SimpleTuringMachine(list("101"))
tm.run(max_steps=20)