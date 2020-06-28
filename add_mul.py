from cgi import parse_qs
from template import html

def application(environ, start_response):
    p = parse_qs(environ['QUERY_STRING'])
    a = p.get('a',[''])[0]
    b = p.get('b',[''])[0]
    c = p.get('c',[''])[0]
    d = p.get('d',[''])[0]

    if '' not in [a, b, c, d]:
        a, b, c, d = int(a), int(b), int(c), int(d)
        x = a + b
        y = c + d
    
    response_body = html
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        (Content-Length', str(len(response_body)))
    ])

    return [response_body]


