import urlparse
import json

def _postdata(env):
    body = ''
    try:
        length = int(env.get('CONTENT_LENGTH', '0'))
    except ValueError:
        length = 0
    if length != 0:
        #print env['wsgi.input'].read(length)
        body = env['wsgi.input'].read(length)
    try: return json.loads(body)
    except: return {}

def _getdata(env):
    qs = urlparse.parse_qs(env['QUERY_STRING'])
    return {i: qs[i][0] for i in qs.keys()}

def application(env, start_response):


    # start_response('200 OK', [('Content-Type','text/html')])
    #
    # Content goes here
    #

    print 'POST %s' % _postdata(env)
    print 'GET %s' % _getdata(env)

    start_response('200 OK', [('Content-Type','text/html')])

    start_response('400 Bad request', [('Content-Type','text/html')])



    return [b"Hello World"]

