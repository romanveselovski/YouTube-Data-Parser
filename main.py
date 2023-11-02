import json
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Список для хранения данных каналов
channel_data = []

try:
    # Открытие страницы логина и вход в систему
    driver.get("https://channelcrawler.com/users/login")

    # Ожидание и ввод данных в поле логина
    email_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "UserUsername"))
    )
    email_input.clear()
    email_input.send_keys("YOU_LOGIN")

    # Ввод данных в поле пароля
    password_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "UserPassword"))
    )
    password_input.clear()
    password_input.send_keys("YOU_PASSWORD")

    # Нажатие кнопки логина
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    login_button.click()

    # Ожидание загрузки следующей страницы после логина
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Переход на указанную страницу
    driver.get(
        "https://channelcrawler.com/rus/results2/c1182e3e2604fc759d3df9808a280fdcf58693e6bb2af25880b705d6ba5e5c1c")

    while True:
        # Ожидание загрузки содержимого страницы
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "channel"))
        )

        # Поиск всех блоков каналов
        channels = driver.find_elements(By.CLASS_NAME, "channel")

        # Итерация по элементам каналов и сбор информации
        for channel in channels:
            title_element = channel.find_element(By.TAG_NAME, "h4").find_element(By.TAG_NAME, "a")
            title = title_element.text
            channel_url = title_element.get_attribute("href")

            # Добавление информации о канале в список
            channel_data.append({
                "title": title,
                "channel_url": channel_url
            })

        # Запись собранных данных в файл JSON
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(channel_data, file, ensure_ascii=False, indent=4)

        # Попытка перейти на следующую страницу
        try:
            # Поиск кнопки "Следующая" внутри определенного блока
            next_button = driver.find_element(By.CSS_SELECTOR, ".col-xs-12.text-center li.next:not(.disabled) a")
            next_button.click()
        except Exception as e:
            # Если кнопка "Следующая" отсутствует или неактивна, завершаем цикл
            break

except Exception as e:
    print(e)
finally:
    # Закрыть браузер после завершения работы
    driver.quit()

subprocess.run(['python', 'youtube_parser.py'], check=True)
