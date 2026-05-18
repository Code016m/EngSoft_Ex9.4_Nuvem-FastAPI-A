from flask import Flask, jsonify, request

app = Flask(__name__)


# GET principal
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API Flask running on CLOUD!"})


# GET + POST
@app.route('/salutation', methods=['GET', 'POST'])
def salutation():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
    else:
        name = request.args.get('name', 'Guest')
    return jsonify({"message": "Hello, %s!" % name})

# PUT
@app.route('/users/<name>/update', methods=['GET', 'POST'])
def update_user(name):
    return jsonify({"message": "User %s was updated" % name})


# DELETE
@app.route("/users/<name>/delete", methods=["GET", "DELETE"])
def delete_user(name):
    return jsonify({"message": "User %s was deleted" % name})

if __name__ == '__main__':
    app.run(debug=True)
