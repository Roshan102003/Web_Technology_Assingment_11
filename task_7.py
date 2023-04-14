from urllib.parse import parse_qs

def hello_world(environ,start_response):
    print(environ)
    parameters = parse_qs(environ.get("QUERY_STRING",""))
    if ' subject' in parameters:
        subject = parameters['subject'][0]
    else:
        subject = "World"
    start_response('200 OK', [('Content Type', 'text/html')])
    response_body = '''Hello {subject} Hello {subject}'''.format(subject = subject)
    return [response_body.encode()]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('',8000,hello_world)
    srv.serve_forever()