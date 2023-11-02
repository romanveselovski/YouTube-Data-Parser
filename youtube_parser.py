import json
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Указываем явно версию ChromeDriver
driver_path = ChromeDriverManager().install()


def get_social_media_type(url):
    if 'instagram' in url:
        return 'Instagram'
    elif 'vk.com' in url or 'vkontakte' in url:
        return 'ВКонтакте'
    elif 't.me' in url:
        return 'Telegram'
    elif 'facebook' in url or 'fb.com' in url:
        return 'Facebook'
    else:
        return 'Другие'


# Открываем JSON файл и загружаем данные
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Создаем пустой список для хранения данных
parsed_data = []

# Запускаем браузер
options = Options()
options.add_argument("--headless")  # Запуск браузера в фоновом режиме
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Перебираем каждый объект в JSON файле
for index, item in enumerate(data, start=1):
    title = item['title']
    channel_url = item['channel_url']

    # Инициализируем списки для каждого типа социальной сети
    instagram_links = []
    vk_links = []
    telegram_links = []
    facebook_links = []
    other_links = []

    # Получаем информацию о соц. медиа, если она доступна
    links = item.get('links', {})
    if 'social_media_links' in links:
        for link in links['social_media_links']:
            social_media_type = get_social_media_type(link['url'])
            formatted_link = f"{link['url']} ({link['title']})"
            if social_media_type == 'Instagram':
                instagram_links.append(formatted_link)
            elif social_media_type == 'ВКонтакте':
                vk_links.append(formatted_link)
            elif social_media_type == 'Telegram':
                telegram_links.append(formatted_link)
            elif social_media_type == 'Facebook':
                facebook_links.append(formatted_link)
            else:
                other_links.append(formatted_link)

    # Проверяем, есть ли у пользователя какие-либо ссылки
    if not any([instagram_links, vk_links, telegram_links, facebook_links, other_links]):
        # Используем Selenium для получения ссылок, если они отсутствуют
        driver.get(channel_url + '/about')
        links = driver.find_elements(By.XPATH, "//a[@class='yt-core-attributed-string__link "
                                               "yt-core-attributed-string__link--display-type "
                                               "yt-core-attributed-string__link--call-to-action-color "
                                               "yt-core-attributed-string--link-inherit-color']")

        contact_info = [link.text for link in links if 'и ещё' not in link.text]

        for contact in contact_info:
            social_media_type = get_social_media_type(contact)
            formatted_link = f"{contact}"
            if social_media_type == 'Instagram':
                instagram_links.append(formatted_link)
            elif social_media_type == 'ВКонтакте':
                vk_links.append(formatted_link)
            elif social_media_type == 'Telegram':
                telegram_links.append(formatted_link)
            elif social_media_type == 'Facebook':
                facebook_links.append(formatted_link)
            else:
                other_links.append(formatted_link)

    # Получаем информацию о стране канала
    country_elements = driver.find_elements(By.CSS_SELECTOR, "#details-container > table > tbody > tr:nth-child(2) > td:nth-child(2)")
    country = country_elements[0].text if country_elements else 'Не указано'

    # Получаем информацию о количестве подписчиков
    subscriber_elements = driver.find_elements(By.CSS_SELECTOR, "#subscriber-count")
    subscribers = subscriber_elements[0].text if subscriber_elements else 'Не указано'

    # Добавляем информацию о стране и количестве подписчиков в список

    parsed_data.append([title, channel_url, country, subscribers] +
                       ['; '.join(instagram_links), '; '.join(vk_links),
                        '; '.join(telegram_links), '; '.join(facebook_links),
                        '; '.join(other_links)])

    # Выводим количество уже обработанных объектов
    print(f"Обработано {index} из {len(data)} объектов")

# Закрываем браузер после использования
driver.quit()

# Создаем DataFrame из списка данных
df = pd.DataFrame(parsed_data, columns=['Наименование канала', 'Ссылка на канал', 'Страна', 'Подписчики', 'Instagram', 'ВКонтакте',
                                        'Telegram', 'Facebook', 'Другие контакты'])


# Сохраняем основной DataFrame в файл test.csv
df.to_csv('info.csv', index=False)

subprocess.run(['python', 'text_to_int.py'], check=True)
