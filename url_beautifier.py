#!/usr/bin/python3
import sys
import argparse
import requests
import json

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Breakdown a url to make it more readable')
    parser.add_argument('-url', '--url', '-u', '--u', type=str, help='The URL to breakdown')
    parser.add_argument('-output', '--output', '-o', '--o', type=str, help='A file to output the url breakdown to')
    parser.add_argument('-verbose', '--verbose', '-v', '--v', action='store_true', help='This verbose option lets you see the output and also lets you output it to a file')
    args = parser.parse_args()
    
    # Extract URL and parameters from command line arguments
    url = args.url
    params = url.split('?', 1)[1]
    output = "URL:\n" + args.url + "\n\nParameters:\n" + params + "\n\nParameter Break-Down:\nParameters:\n"

    # Convert parameters string to a dictionary
    params_dict = {}
    Output_1 = ""
    Output_2 = "\nParameter Contents:\n"
    count = 0
    for param_pair in params.split('&'):
        try:
            key, value = param_pair.split('=', 1)  # Split by the first '=' character only
            params_dict = [key, value]
        except ValueError:
            # Ignore parameters that don't contain '=' character
            pass
        count = count + 1
        param_dict_0 = json.dumps(params_dict[0])
        param_dict_1 = json.dumps(params_dict[1])
        Output_1 += str(count) + ". " + param_dict_0
        Output_2 += str(count) + ". " + param_dict_1
    output += Output_1
    output += "\n" + Output_2
    if args.output and args.verbose:
        # Open the output file in write mode (create if not exists)
        with open(args.output, 'x') as f:
            sys.stdout = f # Redirect stdout to the output file

    
            # Your code here...
            print(output)
    
            # Restore stdout
            sys.stdout = sys.__stdout__
        print(output)
    elif args.output:
        # Open the output file in write mode (create if not exists)
        with open(args.output, 'x') as f:
            # Redirect stdout to the output file
            sys.stdout = f
    
            # Your code here...
            print(output)
    
            # Restore stdout
            sys.stdout = sys.__stdout__
    else:
        print(output)

if __name__ == '__main__':
    main()
