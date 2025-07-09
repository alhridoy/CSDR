from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = {}
user_counter = 1

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values()))

@app.route('/users', methods=['POST'])
def create_user():
    global user_counter
    data = request.get_json()
    user = {
        'id': user_counter,
        'name': data.get('name'),
        'email': data.get('email')
    }
    users[user_counter] = user
    user_counter += 1
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    data = request.get_json()
    users[user_id].update(data)
    return jsonify(users[user_id])

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    del users[user_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)