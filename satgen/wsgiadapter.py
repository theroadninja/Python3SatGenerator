# wsgiadapter.py

# not entirely sure if this really needs to be a separate file from serviceapi.py


def application(env, start_response):
    '''

    :param env:     map with environment info
    :param start_response:   callback for http status headers
    :return:
    '''

    response_body = "hello!!!!"

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)
    return [response_body]