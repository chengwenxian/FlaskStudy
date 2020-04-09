from flask import make_response


def hello_world():
    return 'Hello world!!!'


def hello_new_world():
    return 'Hello new world!!!'


def hello_world_who(username):
    resp = make_response('Hello world!!!I`m {}'.format(username))
    resp.set_cookie('first_cookie', 'test_cookie_1')
    return resp


def hello_world_when(today):
    return 'Hello world!!!Today is {}'.format(today)


def hello_world_where(hello_path):
    return 'Hello world!!!Hello world path is {}'.format(hello_path)

