# Copyright (c) 2024 Ashish Sadhwani
# This software is released under the Mozilla Public License Version 2.0.
# See the LICENSE file for details.

import requests
import argparse

import os
from distro import name
import re

# Variables
debug = False
env_shell = os.environ["SHELL"].split("/")[-1]
env_os = name(pretty=True)


def clean_output_text_in(response):
    code_snippet = re.sub(r'```[\w]*\n([\s\S]*?)```', r'\1', response)
    code_snippet = re.sub(r'^\s{4}', '', code_snippet, flags=re.MULTILINE)
    return code_snippet.strip()


def get_response_for(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        # "model": "llama3.2:3b-instruct-q5_K_M",
        "model": "gemma2:2b-instruct-q5_K_M",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    if debug:
        print(response.status_code)
    response_data = response.json()
    return response_data["response"]


def clean_input_text_in(prompt):
    if debug:
        print(
            "In " + env_shell + " in " + env_os + ", what is the command to " + prompt + ". Just return the command without any description or any explanation.")
    return "In " + env_shell + " in " + env_os + ", what is the command to " + prompt + ". Just return the command without any description or any explanation."


def get_prompt_from_args():
    parser = argparse.ArgumentParser(description="Program accepts a single text argument")
    parser.add_argument('text', nargs='+', help="Text argument")
    args = parser.parse_args()
    return ' '.join(args.text)


def main():
    prompt = get_prompt_from_args()
    clean_prompt = clean_input_text_in(prompt)
    response = get_response_for(clean_prompt)
    clean_response = clean_output_text_in(response)
    print(clean_response)


if __name__ == "__main__":
    main()
