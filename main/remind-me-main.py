"""main file of flask"""

from flask import Flask, jsonify, request

from database_model import Remind, session

app = Flask(__name__)


@app.route('/remind_me_later', methods=['POST'])
def remind_me_later():
    """endpoint function which saves details in database, accept only application/json."""
    data = request.get_json()
    date = data.get("date", "")
    time = data.get("time", "")
    message = data.get("message", "")

    r = Remind(date=date, time=time, message=message)

    session.add(r)
    session.commit()

    return jsonify({"status": "stored"})
