from urllib.parse import urlparse, parse_qs
import re
from http.cookies import SimpleCookie

PHONE_RGX = re.compile(r"(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}")


def check_values(values):
    if len(values) == 1:
        return check_value(values[0])

    output = []
    for value in values:
        output.append(check_value(value))
    return output


def check_value(value):
    if re.match(PHONE_RGX, value):
        return value

    if value.isdigit():
        return int(value)

    if value.lower() in ('yes', 'true', 'on', 'True'):
        return True

    if value.lower() in ('no', 'false', 'off', 'False'):
        return False

    return value


def parse(query: str) -> dict:
    url = urlparse(query)

    output = {}
    for key, values in parse_qs(url.query).items():
        output[key] = check_values(values)
    return output


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    assert parse(
        'https://example.com/path/to/page?name=Jack&name=Maria&age=25&age=21') == {
        'name': ['Jack', 'Maria'], 'age': [25, 21]
    }
    assert parse('http://example.com/?age') == {}
    assert parse('http://example.com/?name=&age=20') == {'age': 20}
    assert parse('?user-name=Alex&root=on&age=25') == {
        'user-name': 'Alex',
        'root': True,
        'age': 25
    }
    assert parse('?phone=380501111100&phone-type=1') == {
        'phone': '380501111100',
        'phone-type': 1
    }


def parse_cookie(query: str) -> dict:
    cookie = SimpleCookie(query)
    cookie.load(query)

    output = {}
    for key, chunk in cookie.items():
        output[key] = check_value(chunk.value)
    return output


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': 28}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': 28}

    assert parse_cookie('user-name=Alex=admin;root=true;age=25') == {
        'user-name': 'Alex=admin',
        'root': True,
        'age': 25
    }
    assert parse_cookie('phone=380501111100;;;') == {'phone': '380501111100'}
    assert parse_cookie('user=;;;') == {'user': ''}
    assert parse_cookie('user;;;') == {}
    assert parse_cookie('user=Alex=admin,root;') == {'user': 'Alex=admin,root'}
