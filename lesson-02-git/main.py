from urllib.parse import urlparse, parse_qs
import re

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
