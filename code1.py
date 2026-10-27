import subprocess
import sys


def analyze_code(file_path, timeout_seconds=10):
  """Виконує переданий файл Python з обмеженням за часом (таймаутом)."""
  print(f"Аналіз файлу: {file_path} (ліміт: {timeout_seconds} сек)...")
  try:
    # Запускаємо процес виконання іншого скрипта
    result = subprocess.run(
        [sys.executable, file_path],
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
    )
    print("Програма успішно завершила роботу.")
    print("Вивід програми:\n", result.stdout)
    if result.stderr:
      print("Помилки виконання:\n", result.stderr)
    return True

  except subprocess.TimeoutExpired:
    print(
        f"[УВАГА] Перевищено ліміт часу ({timeout_seconds} сек). Програма"
        " ймовірно зависла або виконує нескінченний цикл."
    )
    return False

  except Exception as e:
    print(f"Сталася помилка при запуску: {e}")
    return None


# Приклад виклику (потрібно підставити шлях до тестового файлу)
if __name__ == "__main__":
  # analyze_code("test_script.py", 10)
  pass