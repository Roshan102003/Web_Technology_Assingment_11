class ExceptionMiddleware:
    """The middleware we use."""
    def __inti__(self,app):
        self.app = app
    def __call__(self,environ,start_response):
        """Call the application can catch exceptions."""
        appiter = None #just call The application and send the output back
        # unchanged but catch expressions
        try:
            appiter=self.app(environ,start_response)
            for item in appiter:
                yield item # if an exception occurs we get the exception information 
        # and prepare a traceback we can render
        except:
            e_type,e_value,tb=exc_info()
            traceback =['Traceback(most recent call last):']
            traceback+=format_tb(tb)
            traceback.append('%s: %s' %(e_type.__name__,e_value)) #we might have not started a response by now.try to start one with the status code 
            # 500 or ignore an raised exception if the application already started one.
            try:
                start_response ('500 INTERNAL SERVER ERROR',[('Content-Type','text/plain')])
            except:
                pass
            yield '\n'.join(traceback) # wsgi applications might have a close function. If it exists it*must* br called
            if hasattr(appiter,'close'):
                appiter.close()
                