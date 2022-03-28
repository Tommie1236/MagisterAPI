# MagisterAPI
A simple API I wrote to interface with magister.

### This is still WIP!

For this API to work you will need some things:
- Python 3
- Selenium
- An browser driver

#### Python
I will not go over the install of python, I assume you have python already if you are going to use this.

#### Selenium
Selenium is a piece of software to automate and interface with browsers.  
You can download selenium using `pip install selenium` or `pip3 install selenium`.

#### Drivers
Selenium requires a driver to interface with the chosen browser. Make sure it’s in your PATH, e. g., place it in `/usr/bin` or `/usr/local/bin` on linux.
Links to some of the more popular browser drivers:

* [Chrome](https://sites.google.com/chromium.org/driver/)
* [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
* [Firefox](https://github.com/mozilla/geckodriver/releases)
* [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

The default browser in de code is Chrome, but you can uncomment the browser you want to use.
