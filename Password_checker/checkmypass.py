import requests
import hashlib
import sys


def request_api_data(query_character):
    url = 'https://api.pwnedpasswords.com/range/' + query_character
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f'Error Fetching: {response.status_code}, check API and try again')
    return response


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:  # what we check are the tails of the hashes that have the same first 5 chars with our hash tail
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # check if password exists in API response
    sha1passwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1passwd[:5], sha1passwd[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f'{password} was found {count} times... you should change your password')
        else:
            print(f'{password} NOT found. Carry on!')
    return 'Done!'


if __name__ == '__main__':
    main(sys.argv[1:])
