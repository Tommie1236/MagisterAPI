## REMINDER, This is still WIP, Im not finished with it as it is. But if it is usefull for anyone feel free to use it.
(and mention me or this repo of course)

# MagisterAPI
A simple API I wrote to interface with magister.

For this API to work you will need some things:
- Python 3
- Selenium
- An browser driver

#### Python
I will not go over the install of python, I assume you have python already if you are going to use this.  
Otherwise go to [this](https://www.python.org/downloads/) site

#### Selenium
Selenium is a piece of software to automate and interface with browsers.  
You can download selenium using `pip install selenium` or `pip3 install selenium`.

#### Drivers
Selenium requires a driver to interface with the chosen browser. Make sure it’s in your PATH, e. g., place it in `/usr/bin` or `/usr/local/bin` on linux.  
Links to some of the more popular browser drivers:

* [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads/)
* [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
* [Firefox](https://github.com/mozilla/geckodriver/releases)
* [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

The default browser in de code is Chrome, but you can uncomment the browser you want to use.  
And comment the other ones of course.

For now it can only see the 1st lesson of the 1st day and give you all the lesson info in a list.  
If you know any way to also access the other lessons and days please leave an issue.  
Feel free to also make an issue if you need any help.
