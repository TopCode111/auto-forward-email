# automation

A simple script that lets you login to your email from the command line
Auto login on Yahoo.com and auto set up to forward emails into a email address
manage the project by Multi thread 
## Built With

* [Selenium](http://www.seleniumhq.org/) - Python Library for browser automation
* [Beautiful-Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Python Library for web scraping

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development or personal use.

### Installations

Install the following in order to setup the environment

- We will use **pip** to download the python libraries. Download pip from here -

```
https://pip.pypa.io/en/stable/installing/
```

- Install **Beautiful-Soup** python library

```
pip install beautifulsoup4
```
- Install the **lxml parser** 

```
pip install lxml
```
- Install **Selenium**  python library

```
pip install selenium
```
- Download the latest **chrome-driver** here -

```
https://sites.google.com/a/chromium.org/chromedriver/
Unzip the file and copy the chrome-driver to /usr/local/bin
```

## Using the sript

On the command line, simply navigate to the folder **./autoLogin/scripts** and run -> **python runMe.py** 

- Running the script for the first time -

<img width="684" alt="screen shot 2017-12-03 at 11 58 56 pm" src="https://user-images.githubusercontent.com/15865085/33536913-1f10f18c-d886-11e7-8334-75c00f32ebf7.png">

```
The credentials are stored in a text file named credentials.txt
```

- Running the script after initial setup - 

<img width="557" alt="screen shot 2017-12-03 at 11 59 32 pm" src="https://user-images.githubusercontent.com/15865085/33536949-792d0f84-d886-11e7-8aad-a1ff6e0e0c34.png">

```
If at any point you want to reset credentials, simply delete credentials.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
