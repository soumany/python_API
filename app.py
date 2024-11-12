from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for your API to allow cross-origin requests

# Sample data
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
]

# Route to get the list of books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

# Route to get a book by ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book), 200
    return jsonify({"message": "Book not found"}), 404

# Route to add a new book
@app.route('/api/books', methods=['POST'])
def add_book():
    new_book = request.json
    new_book["id"] = books[-1]["id"] + 1 if books else 1
    books.append(new_book)
    return jsonify(new_book), 201

# Route to update a book by ID
@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        data = request.json
        book.update(data)
        return jsonify(book), 200
    return jsonify({"message": "Book not found"}), 404

# Route to delete a book by ID
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
