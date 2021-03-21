from urllib.parse import urlsplit, parse_qsl


def parse(query: str) -> dict:
    my_query = urlsplit(query).query
    params = parse_qsl(my_query)
    return dict(params)


if __name__ == '__main__':
    # parse
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


