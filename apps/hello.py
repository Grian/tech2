#!/usr/bin/python3

def app(env, start_response):
    data = b"Hello, World!\n"
    start_response("200 Ok",(("Content-type", "text/plain"),))
    
    out = []
    for param in env["QUERY_STRING"].split('&'):
        out.append(param)
        out.append("\n")
    return out
