import flask


def initialize_buttons():
    return {num: False for num in range(9)}

buttons = initialize_buttons()

# EB looks for an 'application' callable by default.
application = flask.Flask(__name__)


@application.route("/button/<number>/", methods=['GET', 'PUT'])
def show_button():
    pass


@application.route("/buttons/", methods=['GET'])
def show_buttons():
    return flask.jsonify(buttons)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
