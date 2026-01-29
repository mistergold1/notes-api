from flask import Flask, request, jsonify
from storage import Storage

app = Flask(__name__)
storage = Storage("notes.json")


@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(storage.get_all())


@app.route("/notes", methods=["POST"])
def create_note():
    data = request.json
    if not data or "text" not in data:
        return {"error": "text is required"}, 400

    note = storage.add(data["text"])
    return jsonify(note), 201


@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    if not storage.delete(note_id):
        return {"error": "note not found"}, 404
    return {}, 204


if __name__ == "__main__":
    app.run(debug=True)
