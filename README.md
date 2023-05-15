# Python ConfigParser Tutorial

Use Case 1: Storing URL and Login Credentials
The project demonstrates how to store the URL and login credentials in a configuration file using configparser. This allows for easy modification and maintenance of these sensitive data without directly modifying the test code.

Use Case 2: Managing Testing on Different Environments
Configparser is utilized to manage testing on different environments. By storing environment-specific settings, such as database connections, API endpoints, or browser configurations, in the configuration file, the project enables seamless switching between different testing environments.

Use Case 3: Browser Management through Configuration
The project exemplifies how to manage the browser configuration for tests using configparser. Browser preferences, such as the browser type, version, and additional options, can be conveniently stored in the configuration file. This empowers testers to easily modify the browser settings without changing the codebase.

Use Case 4: Parallel Testing on LambdaTest
By leveraging the power of configparser, the project demonstrates parallel testing on the LambdaTest cloud platform. The configuration file can store different browser and operating system combinations, allowing the tests to be executed simultaneously on multiple configurations. This significantly reduces the overall test execution time.

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

## License

This project is licensed under the MIT License
