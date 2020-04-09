"""
要特别注意的是：
   蓝图的实例化要和使用在同一个文件夹下面
"""
from apps.f_app_bp_test.views.hello import *
from flask import Blueprint

test_bp = Blueprint('f_app_bp_test', 'apps.f_app_bp_test.url_route', url_prefix='/test_bp')


@test_bp.route('/', methods=('GET', 'POST'))
def url_hello_world():
    return hello_world()


@test_bp.route('/hello_new/')
def url_hello_new_world():
    return hello_new_world()


@test_bp.route('/hello_new/<username>', methods=['POST'])
def url_hello_world_who(username):
    return hello_world_who(username)


# int:today 之间不能有空格
@test_bp.route('/hello_new/<int:today>')
def url_hello_world_when(today):
    return hello_world_when(today)


@test_bp.route('/hello_new/<path:hello_path>', methods=['POST'])
def url_hello_world_where(hello_path):
    return hello_world_where(hello_path)
