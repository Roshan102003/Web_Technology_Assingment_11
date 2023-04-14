from urllib import response
from urllib.parse import parse_qs
class WSGIRequestHandler:
    def __inti__(self):
        print("Within init")
        self.request={}
        self.response={'Content-Type':'text/plain'}
    def __call__(self,environ,start_response):
        print("Within call")
        appiter= None
        self.request['args'] = parse_qs(environ['QUERY_STRING'])
        appiter=self.get()
        start_response('200 OK',list(self.response.items()))
        for item in appiter:
            yield item
        # wsgi application might have a close function. If it exists 
        # it 'must' be called
        if hasattr(appiter,'close'):
            appiter.close()
        
class Hello(WSGIRequestHandler):
    def get(self):
        print("Within get")
        name = self.request['args'].get('subject','world')
        response_body = 'Hello {0}'.format(name)
        return [response_body.encode()]
    
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost',8080,Hello())
    print("Now going to serve")
    srv.serve_forever()