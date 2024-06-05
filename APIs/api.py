from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Your existing routes here...


# Sample food data
foods = [
    {"id": 1, "name": "Pizza", "category": "Italian"},
    {"id": 2, "name": "Sushi", "category": "Japanese"},
    {"id": 3, "name": "Tacos", "category": "Mexican"},
    {"id": 4, "name": "Burger", "category": "American"},
    {"id": 5, "name": "Pad Thai", "category": "Thai"},
    {"id": 6, "name": "Ramen", "category": "Japanese"},
    {"id": 7, "name": "Pasta", "category": "Italian"},
    {"id": 8, "name": "Curry", "category": "Indian"},
    {"id": 9, "name": "Pho", "category": "Vietnamese"},
    {"id": 10, "name": "Tikka Masala", "category": "Indian"}
clear
# Route to get all foods
@app.route('/foods', methods=['GET'])
def get_foods():
    return jsonify(foods)

# Route to get a specific food by ID
@app.get('/foods/<int:id>')
def get_food(id):
    for food in foods:
        if food["id"] == id:
            return jsonify(food)
    return jsonify({"error": "Food not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
