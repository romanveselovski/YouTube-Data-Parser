import pandas as pd


# Функция для преобразования подписчиков в числовой формат
def convert_subscribers(subs_string):
    if pd.isnull(subs_string) or 'не указано' in subs_string.lower():
        return None
    subs_string = subs_string.lower().replace(' подписчиков', '').replace(',', '.')
    number = None
    if 'тыс.' in subs_string:
        number = float(subs_string.replace(' тыс.', '')) * 10**3
    elif 'млн' in subs_string:
        number = float(subs_string.replace(' млн', '')) * 10**6
    return str(number)[:-2] if str(number).endswith('.0') else str(number)


# Загрузим данные из файла CSV
data = pd.read_csv('info.csv')

# Преобразуем столбец "Подписчики"
data['Подписчики'] = data['Подписчики'].apply(convert_subscribers)

# Сохраняем изменения в новый CSV файл
data.to_csv('final_data.csv', index=False)

print('Файл final_data.csv готов')
