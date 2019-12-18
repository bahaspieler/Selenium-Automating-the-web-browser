# Selenium based Web Automation
  The selenium package is used to automate web browser interaction from Python.  In my current workplace, 
  I would need to update some specific works on a common server. But when I need to do that for multiple times at a stretch,
  it consumes much time to do it. So came up with this solution to **_automate the task_**. With this tool,
  just need to insert the inputs into an excel file and configure the web browser in debugging mode. Then run 
  the script and within least time, the job is done. 
  
## Installing Dependencies
* chromedriver.exe
* pandas
* selenium

1. Download the [WebDriver for Chrome - chrome.exe](https://sites.google.com/a/chromium.org/chromedriver/downloads). The version of the chromedriver must be as same as the chrome browser installed in the pc.
1. In the command window execute the following commands. Make sure of that path of **_pip_** is added to system environment variable.

  ` pip install pandas`
  
  `
  pip install selenium
  `

## Getting Started
#### Running chrome in *debugging* mode
To use an existing session of chrome browser, need to initiate a chrome session in debugging mode.
Because you don't always want to open new session of chrome browser while testing the code and so on. Now,
* Add *PATH* of chrome to the system environment variable. Or simply run *cmd/terminal* in the location
where chrome.exe exist. For example, 
>C:\Program Files (x86)\Google\Chrome\Application
* Run this command `chrome.exe -remote-debugging-port=available_port_no --user-data-dir="where\to\initiate\debugger chrome session"`.
For me the command is like this, `chrome.exe -remote-debugging-port=9014 --user-data-dir="C:\selenium\chrome"`
* A Chrome session will be initiated in debugging mode.

## Code Explanation 

#### Importing the required package
```python
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
```

#### Setting up the chrome browser in debugging mode. 
For that we have imported `Options` through writing `from selenium.webdriver.chrome.options import Options` earlier.
```python
chrome_driver = r'C:\chromedriver\chromedriver.exe' # directory of the chromedriver.exe
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9014") #change the port number as 127.0.0.1:port no.
driver= webdriver.Chrome(chrome_driver, chrome_options= chrome_options)
```
Use your port number instead of `9014`. And assign the path of your chromedriver.exe to the `chrome_driver`.

#### Pre-processing the inputs
```python
df = pd.read_excel(r"C:\path\to\inputs.xlsx", sheet_name=0)
lst = df['Header_name']
sites = list(lst)
print(sites)
```
With *pandas*, took the inputs as a list.

