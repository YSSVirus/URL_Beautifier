# URL_Beautifier
This Python script takes a URL as input and outputs a numbered list of parameter names and values. It simplifies the analysis of the URL's parameters, presenting them in a clear and concise breakdown alongside the original URL. This tool saves time and effort in interpreting and extracting URL parameters.


## Installation
To use this script, you can clone the repository using the following command:
git clone https://github.com/your-username/your-repo.git
## Usage
Once you have cloned the repository, navigate to the project directory and run the script with the following command:
python3 url_parameter_breakdown.py --url <URL>
Replace <URL> with the URL you want to analyze. The output will include the original URL, the parameters, and a breakdown of each parameter with its corresponding value.

## Example
### Command:
python3 url_parameter_breakdown.py --url "https://example.com/path?param1=value1&param2=value2&param3=value3"

### Output:
URL:
https://example.com/path?param1=value1&param2=value2&param3=value3

Parameters:
param1=value1&param2=value2&param3=value3

Parameter Break-Down:
Parameters:
1. "param1"
2. "param2"
3. "param3"

Parameter Contents:
1. "value1"
2. "value2"
3. "value3"
