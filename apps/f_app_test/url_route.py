from apps.f_app_test.views.hello import *


def register_url(app_obj):
    @app_obj.route('/')
    def url_hello_world():
        return hello_world()

    @app_obj.route('/hello_new/')
    def url_hello_new_world():
        return hello_new_world()

    @app_obj.route('/hello_new/<username>', methods=['POST'])
    def url_hello_world_who(username):
        return hello_world_who(username)

    # int:today 之间不能有空格
    @app_obj.route('/hello_new/<int:today>')
    def url_hello_world_when(today):
        return hello_world_when(today)

    @app_obj.route('/hello_new/<path:hello_path>', methods=['POST'])
    def url_hello_world_where(hello_path):
        return hello_world_where(hello_path)
