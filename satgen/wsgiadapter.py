# wsgiadapter.py

# not entirely sure if this really needs to be a separate file from serviceapi.py
import serviceapi
import itertools
import traceback


def normalize_path(http_path):
    '''
    >>> normalize_path("//////a////b///d////")
    ['a', 'b', 'd']
    >>> normalize_path("a////b///d////")
    ['a', 'b', 'd']
    >>> normalize_path("")
    []
    >>> normalize_path("/")
    []
    >>> normalize_path("//////")
    []

    remotes duplicate slashes, etc
    :param http_path:
    :return: list of path elements
    '''

    #remove duplicates
    path = ''.join(x for x, _ in itertools.groupby(http_path)).rstrip("/").lstrip("/")
    if path == "":
        return []
    return path.split('/')


def application(env, start_response):
    '''

    :param env:     map with environment info
    :param start_response:   callback for http status headers
    :return:
    '''
    try:
        path = normalize_path(env["PATH_INFO"])
        if len(path) < 1:
            response_body = "hello!!!\n"
        elif "generate" == path[0]:

            #TODO:  better parsing that automatically returns better error message
            #to either http or command line

            varcount = 16
            clausecount = None
            if len(path) > 1:
                varcount = int(path[1])
                if len(path) > 2:
                    clausecount = int(path[2])

            p = serviceapi.generate(varcount, clausecount)

            response_body = p.to_cnf()
        else:
            response_body = "hello!!!!\n"
            response_body += "\npath: " + env["PATH_INFO"]  #does not have query string
            response_body += "\npath: " + env["RAW_URI"] #includes query string
            response_body += "\nQUERY_STRING: " + env["QUERY_STRING"]
            response_body += "\nwsgi.url_scheme: " + env["wsgi.url_scheme"]
            response_body += "\n" + str(env)

        status = '200 OK'
        response_headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(response_body)))
        ]


        start_response(status, response_headers)
        return [response_body]
    except Exception as ex:
        tb = traceback.format_exc()

        response_body = str(ex) + "\n"
        response_body += "\n"
        response_body += str(tb) + "\n"
        response_headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(response_body)))
        ]
        start_response('500 Internal Server Error', response_headers)
        return [response_body]