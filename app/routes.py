from app import db
from app.models.book import Book
from flask import Blueprint, request, jsonify, make_response

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["POST"], strict_slashes=False)
def add_book():
    request_body = request.get_json()
    new_book = Book(title = request_body["title"],
                    description = request_body["description"])
        
    db.session.add(new_book)
    db.session.commit()

    return {
        "success": True,
        "message": f"Book {new_book.title} has been created."
    }, 201

@books_bp.route("", methods=["GET"], strict_slashes=False)
def books_index():
    books = Book.query.all()
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response), 200

@books_bp.route("/<book_id>", methods=["GET"], strict_slashes=False)
def get_single_book(book_id):
    book = Book.query.get(book_id)

    if book == None:
        return make_response("", 404)
    
    return {
        "id": book_id,
        "title": book.title,
        "description": book.description
    }

@books_bp.route("/<book_id>", methods=["PUT"], strict_slashes=False)
def update_book(book_id):
    book = Book.query.get(book_id)
    form_data = request.get_json()
    
    if book == None:
        return make_response("", 404)

    book.title = form_data["title"]
    book.description = form_data["description"]

    db.session.commit()

    return f"Book {book.id} successfully updated.", 200

@books_bp.route("/<book_id>", methods=["DELETE"], strict_slashes=False)
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return make_response("", 404)

    db.session.delete(book)
    db.session.commit()

    return f"Book {book_id} successfully deleted.", 200