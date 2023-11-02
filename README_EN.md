
# YouTube Data Parser

## Description
Проект включает в себя скрипты для парсинга данных о каналах YouTube при помощи сервиса https://channelcrawler.com. Основной скрипт `main.py` использует Selenium для автоматизации веб-браузера и извлечения информации с сайта https://channelcrawler.com. Скрипт `youtube_parser.py` создает файл с информацией о соц. сетях каналов из массива данных, а `text_to_int.py` конвертирует текстовые данные о подписчиках в числовой формат.

## Installation
Для работы проекта необходимо развернуть его у себя локально и заменить логин и пароль от сервиса https://channelcrawler.com

## Usage
Для запуска основного скрипта выполните:
```bash
python main.py
```

После запуска `main.py` будут автоматически вызваны другие скрипты в процессе работы.

## Additional Information
Скрипт `youtube_parser.py` может быть вызван самостоятельно, для этого создайте файл `data.json` в виде:
```bash
{
    "title": "Grazhina",
    "channel_url": "https://youtube.com/@grazhinka_"
},
```

## Contributing
Если вы хотите внести свой вклад в проект, пожалуйста, сначала обсудите изменения, которые вы хотите внести, через issue.

## Лицензия
The MIT License (MIT)

Copyright (c) 2023 RAMAN VESIALOUSKI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

ADDITIONAL DISCLAIMER: THE AUTHOR OF THIS SOFTWARE SHALL NOT BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


## Contact
`RAMAN VESIALOUSKI` - veselovskiroman@gmail.com

