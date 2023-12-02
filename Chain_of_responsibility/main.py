# Abstract handler
class HttpHandler:
    def handle(self, code):
        raise NotImplementedError()


# Handler - contains realized method handle and ref to the next handler
class Http400Handler(HttpHandler):
    def __init__(self, next_handler):
        self._next = next_handler

    def handle(self, code):
        if code == 400:
            print('Response of', code, " code: Bad Request")
        elif self._next is not None:
            self._next.handle(code)
        else:
            print('Code', code, 'is not handled')


# Handler - contains realized method handle and ref to the next handler
class Http401Handler(HttpHandler):
    def __init__(self, next_handler):
        self._next = next_handler

    def handle(self, code):
        if code == 401:
            print('Response of', code, " code: Unauthorized")
        elif self._next is not None:
            self._next.handle(code)
        else:
            print('Code', code, 'is not handled')


# Handler - contains realized method handle and ref to the next handler
class Http500Handler(HttpHandler):
    def __init__(self, next_handler):
        self._next = next_handler

    def handle(self, code):
        if code == 500:
            print('Response of', code, " code: Internal Server Error")
        elif self._next is not None:
            self._next.handle(code)
        else:
            print('Code', code, 'is not handled')


# Client - own the chain of handlers
# active_chain method starts processing along the chain of responsibility
class Client(object):
    def __init__(self):
        handler400 = Http400Handler(None)
        handler500 = Http500Handler(next_handler=handler400)
        handler401 = Http401Handler(next_handler=handler500)
        self._handler = handler401

    def active_chain(self, code):
        self._handler.handle(code)


client = Client()
client.active_chain(401)
client.active_chain(400)
client.active_chain(613)
client.active_chain(500)
client.active_chain(900)