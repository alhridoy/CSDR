from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = []
next_id = 1

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()
    user = {
        'id': next_id,
        'name': data.get('name'),
        'email': data.get('email')
    }
    users.append(user)
    next_id += 1
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)