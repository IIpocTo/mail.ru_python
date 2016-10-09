import webbrowser
from random import randint
from time import sleep
from wsgiref.simple_server import make_server
from wsgiref.validate import validator


def events(max_delay, limit):
    while True:
        delay = randint(1, max_delay)
        if delay >= limit:
            sleep(limit)
            yield None
        else:
            sleep(delay)
            yield 'Event generated, awaiting %d s' % delay


EVENT_GENERATOR = events(5, 4)
PORT = 8083


class WSGIApplication:
    def __init__(self, environment, start_response):
        print('Get request')
        self.environment = environment
        self.start_response = start_response
        self.headers = []

    def __iter__(self):
        print('Wait for response')
        if self.environment.get('PATH_INFO', '/') == '/':
            event = next(EVENT_GENERATOR, None)
            print("Event: " + str(event))
            if event is None:
                self.no_content_response()
            else:
                yield from self.ok_response(event)
        else:
            yield from self.not_found_response()
        print('Done')

    def not_found_response(self):
        print('Create response')
        print('Send headers')
        error_message = "Wrong page. Go to http://localhost:" + str(PORT) + "/"
        self.headers += [('Content-type', 'text/plain; charset=utf-8')]
        self.start_response('404 Not Found', self.headers)
        yield (error_message).encode('utf-8')
        print('Headers in sent')

    def no_content_response(self):
        print('Create response')
        self.start_response('204 No Content', self.headers)

    def ok_response(self, message):
        print('Create response')
        print('Send headers')
        self.headers += [('Content-type', 'text/plain; charset=utf-8')]
        self.start_response('200 OK', self.headers)
        print('Headers is sent')
        yield ('%s\n' % message).encode('utf-8')
        print('Body is sent')


if __name__ == '__main__':
    validate_app = validator(WSGIApplication)
    webbrowser.open('http://localhost:' + str(PORT) + '/')
    server = make_server('127.0.0.1', PORT, validate_app)
    server.serve_forever()
