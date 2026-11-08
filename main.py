import pandas as pd

# Читаем эксель
df = pd.read_excel("data.xlsx")

# Выводим первые 5 строк на экран для проверки
print("--- Наша таблица ---")
print(df)

# Фильтруем данные в таблице
adults = df[df["Возраст"] > 24]

print("\n--- Люди, старше 24 лет ---")
print(adults)

# Сохраняем в новый файл экселя
adults.to_excel("result.xlsx", index=False)
print("\nГотово! Результат сохранён в result.xlsx")