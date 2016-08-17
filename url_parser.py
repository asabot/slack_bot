import re


def is_url(possible_url):
    regex = re.compile(r'[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
    if re.search(regex, possible_url):
        return True
    else:
        return False


def message_to_upper(message):
    words = message.split()
    rage_message = ''

    for word in words:
        if is_url(word):
            rage_message = rage_message + word + " "
        else:
            rage_message = rage_message + word.upper() + " "

    return rage_message


if __name__ == '__main__':

    message = 'Check out google.com'

    print(message_to_upper(message))
