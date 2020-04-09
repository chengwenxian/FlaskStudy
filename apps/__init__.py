from flask import Flask

# from apps.f_app_test.url_route import register_url


def create_app():
    app_obj = Flask(__name__)
    # register_url(app_obj)
    from apps.f_app_bp_test import test_bp
    app_obj.register_blueprint(test_bp)

    return app_obj
