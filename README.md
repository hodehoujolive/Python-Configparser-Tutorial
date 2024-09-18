# Python ConfigParser Tutorial

- Use Case 1: Store the URL and login credentials in a configuration file using configparser.

- Use Case 2: Manage testing on different environments with Configparser.

- Use Case 3: Manage the browser configuration for tests using configparser

- Use Case 4: Parallel testing on the LambdaTest cloud platform with configparser.

With these use cases, this project serves as a comprehensive guide for utilizing configparser to manage configurations in a Selenium testing framework. The modular and flexible approach presented here ensures efficient test maintenance and scalability, empowering testers to focus on developing robust test scripts with minimal configuration overhead.

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Configuration](#configuration)
* [Contributing](#contributing)
* [License](#license)

## Installation

Clone the repository to your local machine:
```
git clone https://github.com/hodehoujolive/python-configparser-sample
```

Make sure you have python installed. If not, install python
```
brew install Python
```

install Selenium on our machine
```
pip install selenium
```

Install the latest version of WebDriver for the browser you want to use. You can download the WebDriver for the following commonly used browsers:

    - Firefox: GeckoDriver
    - Chrome: ChromeDriver
    - Opera: OperaDriver
    - Edge: Microsoft Edge WebDriver
    
    Make sure you have the correct version for your browser, otherwise it won't work.

## Usage

1. Edit the ```test_config.ini``` file with your website URL, email, and password.
2. Run the script using the following command:

```
python3 -m unittest
```

## Configuration

The ```test_config.ini``` file contains the configuration parameters for the script. You can edit this file to provide the following parameters:

    - url: The URL of the website to log into.
    - email: The email address to use for login.
    - password: The password to use for login.

## Contributing

If you find any issues or have suggestions for improvements, feel free to submit a pull request or create an issue in the repository.
