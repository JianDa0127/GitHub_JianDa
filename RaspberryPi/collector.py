from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    name = request.args.get('name')
    return 'My name is {}'.format(name)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)