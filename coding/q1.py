import requests

class Result:
    def __init__(self):
        self.out1 = dict()
        self.out2 = ''

def check_palindrome(strng):
    # reverse the string
    rev_str = reversed(strng)

    # check if the string is equal to its reverse
    if list(strng) == list(rev_str):
        # print("The string is a palindrome.")
        return True
    else:
        # print("The string is not a palindrome.")
        return False

def probe_url(url):
    return requests.get(url, allow_redirects=True)

def validate_response(response):
    if response.status_code == 200:
        return True
    return False

def check_if_text(response):
    if response.text:
        return True
    return False

def parse_response(response):
    if not validate_response(response):
        return "the URL is incorrect", True
    if not check_if_text(response):
        return "file is not a text file", True
    return response.text, False


def process_line(line):
    # remove the spaces
    line.replace(" ", "")
    return line

def main(url):
    output1 = dict()
    output2 = ''
    atleastOnePalindrome = False
    ret = probe_url(url)
    msg, err = parse_response(ret)
    if err:
        output2 = msg
        output1 = {0:0}
    else:
        # The validations are passed
        # now check palindrome
        i = 0
        # print("FLAG: check msg")
        # print(msg)
        for line in msg.splitlines():
            # print("FLAG: check line")
            # print(line)
            i += 1
            # process line
            output1[i] = len(process_line(line))
            if check_palindrome(line):
                atleastOnePalindrome = True
        if not atleastOnePalindrome:
            output1 = {0:0}
        output2 = 'file ok'
    

    # print("CHEKING THE OUTPUT")
    # print("OUTPUT1: " + str(output1))
    # print("OUTPUT2: " + output2)


if __name__ == "__main__":
    url = 'https://mettl-arq.s3-ap-southeast-1.amazonaws.com/questions/iit-kanpur/cyber-security-hackathon/round1/problem1/defaulttestcase.txt'
    main(url)


# Test cases
# assert check_palindrome('aba')
# assert not check_palindrome ("aaab")
# assert check_palindrome ("aaab")