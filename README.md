# Selenium based Web Automation
  The selenium package is used to automate web browser interaction from Python.  In my current workplace, 
  I would need to update some specific works on a common server. But when I need to do that for multiple times at a stretch,
  it consumes much time to do it. So came up with this solution to **_automate the task_**. With this tool,
  just need to insert the inputs into an excel file and configure the web browser in debugging mode. Then run 
  the script and within least time, the job is done. 
  
  Have a look at the *Quick Overview* section to get a glance the *automation*.
## Quick Overview
![overview gif](quick_overview.gif)
  
  *A quick GIF of the Automated Task.*

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
