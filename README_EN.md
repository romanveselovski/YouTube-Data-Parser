
# YouTube Data Parser

## Description
The project includes scripts for parsing data about YouTube channels using the service https://channelcrawler.com. The main script main.py utilizes Selenium for web browser automation and extracting information from the site https://channelcrawler.com. The script youtube_parser.py creates a file with information about the social networks of the channels from an array of data, and text_to_int.py converts textual data about subscribers into a numerical format.

## Installation
For the project to work, you need to deploy it locally and replace the login and password for the service https://channelcrawler.com.

## Usage
To run the main script, execute:
```bash
python main.py
```

After starting main.py, other scripts will be automatically called during the process.

## Additional Information
The script youtube_parser.py can be called independently. For this, create a data.json file in the form of:
```bash
{
    "title": "Grazhina",
    "channel_url": "https://youtube.com/@grazhinka_"
},
```

## Contributing
If you want to contribute to the project, please discuss the changes you want to make through an issue first.


## Contact
`RAMAN VESIALOUSKI` - veselovskiroman@gmail.com

