import flask
from flask import request

buttons = {str(num): False for num in range(9)}

# Amazon Elastic Beanstalk looks for an 'application' callable by default.
application = flask.Flask(__name__)


@application.route("/button/<number>/", methods=['GET', 'PUT'])
def show_button(number):
    if request.method == 'PUT':
        buttons[number] = not buttons[number]

    return flask.jsonify(buttons[number])


@application.route("/buttons/", methods=['GET'])
def show_buttons():
    return flask.jsonify(buttons)

if __name__ == "__main__":
    application.debug = False
    application.run()
