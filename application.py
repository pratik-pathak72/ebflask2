from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return 'Hello World!'

@application.route('/<anyname>')
def any_name(anyname):
    return f'Hello {anyname}'

if __name__ == '__main__':
    application.debug = True
    application.run()
