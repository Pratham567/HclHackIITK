# -*- coding: utf-8 -*-
import requests
import time


def check_palindrome(strng):

    # reverse the string
    rev_str = reversed(strng)

    # check if the string is equal to its reverse
    # list will preserve the order
    if list(strng) == list(rev_str):
        # It is palindrome
        return True
    else:
        # It is not palindrome
        return False

def probe_url(url):
    i = 5
    while i>0:
        try:
            r = requests.get(url, allow_redirects=True)
            return r
        except:
            return None

        time.sleep(0.5)


def validate_response(response):
    if response and response.status_code == 200:
        return True
    return False

def check_if_there_is_response(response):
    if response.text:
        return True
    return False

def parse_response(response):
    if not check_if_there_is_response(response):
        return "file is not a text file", True
    return response.text, False

def process_line(line):
    # remove the spaces, convert all the letters to lowercase
    line = line.replace(" ", "").lower()
    return line

def check_text_file(response):
    # check if the response received is of type text/plain

    if response.headers.get('content-type') == 'text/plain':
        return True
    return False

def main(url):
    output1 = dict()
    output2 = ''
    atleastOnePalindrome = False
    response = probe_url(url)
    # if response:
    # check response
    if not validate_response(response):
        output1 = {0:0}
        output2 = "the URL is incorrect"
    else:
        # We have response so URL is correct
        # Check if it is text file
        if check_text_file(response):
            # It is a text/plain file
            # Time to parse it
            msg, err = parse_response(response)
            if err:
                output2 = msg
                output1 = {0:0}
            else:
                # The validations are passed
                # now check palindrome
                i = 0
                for line in msg.splitlines():
                    i += 1
                    line = process_line(line)
                    if line and check_palindrome(line):
                        output1[i] = len(line)
                        atleastOnePalindrome = True
                if not atleastOnePalindrome:
                    output1 = {0:0}
                output2 = 'file ok'
        else:
            output1 = {0:0}
            output2 = "file is not a text file"
        # the url is not text file
    # else:
    #     # URL is wrong
    #     output1 = {0:0}
    #     output2 = "the URL is incorrect"
    # "the URL is incorrect"

    print("CHEKING THE OUTPUT")
    print("OUTPUT1: " + str(output1))
    print("OUTPUT2: " + output2)


if __name__ == "__main__":
    url = 'https://mettl-arq.s3-ap-southeast-1.amazonaws.com/questions/iit-kanpur/cyber-security-hackathon/round1/problem1/defaulttestcase.txt'
    # url = 'https://www.google.com'
    # url = 'https://sjmulder.nl/en/textonly.html'
    main(url)
