import flask
from flask import request

buttons = {('buttonId' + str(num)): False for num in range(4)}

# Amazon Elastic Beanstalk looks for an 'application' callable by default.
application = flask.Flask(__name__)


@application.route("/button/<button_id>/", methods=['GET', 'PUT'])
def show_button(button_id):
    if request.method == 'PUT':
        for key in buttons:
            new_value = True if key == button_id else False
            buttons[key] = new_value
    return flask.jsonify(buttons[button_id])


@application.route("/buttons/", methods=['GET'])
def show_buttons():
    return flask.jsonify(buttons)

if __name__ == "__main__":
    application.debug = False
    application.run()
