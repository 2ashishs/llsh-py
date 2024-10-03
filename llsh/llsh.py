# Copyright (c) 2024 Ashish Sadhwani
# This software is released under the Mozilla Public License Version 2.0.
# See the LICENSE file for details.

import requests
import argparse

debug = True

def get_response_from_api_for(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "llama3.2:3b-instruct-q5_K_M",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    if debug:
        print(response.status_code)
    response_data = response.json() # Assuming the response is in JSON format
    return response_data["response"]

def receive_text_prompt():
    parser = argparse.ArgumentParser(description="Program accepts a single text argument")
    parser.add_argument('text', nargs='+', help="Text argument")
    args = parser.parse_args()
    return ' '.join(args.text)

def main():
    # Receive the text prompt from argument
    prompt = receive_text_prompt()
    if debug:
        print("Linux shell command to " + prompt + ". Just return the command.")
    # ToDo: Clean the prompt
    # Send the prompt to API & receive response
    response = get_response_from_api_for(prompt)
    print(response)
    # ToDo: Clean the response


if __name__ == "__main__":
    main()
