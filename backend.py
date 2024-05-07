from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

con = psycopg2.connect(
    dbname="item", user="postgres", password="password", host="localhost", port="5432"
)
cur = con.cursor()

app = Flask(__name__)
CORS(app)


# Helper Functions
def items_to_json(items):
    return jsonify(
        {
            "items": [
                {
                    "id": item[0],
                    "name": item[1],
                    "description": item[2],
                    "rating_value": item[3],
                    "rating_count": item[4],
                }
                for item in items
            ]
        }
    )


# Routing
@app.route("/upload_item", methods=["POST"])
def upload_item():
    data = request.json
    cur.execute(
        """
        INSERT INTO item (name, description, rating_value, rating_count) VALUES (%s, %s, %s, %s) RETURNING id
    """,
        (data["name"], data["description"], 0.0, 0),
    )
    con.commit()
    return jsonify({"id": cur.fetchone()[0]})


@app.route("/delete_item", methods=["POST"])
def delete_item():
    data = request.json
    cur.execute("DELETE FROM item WHERE id = %s", (data["id"],))
    con.commit()
    return jsonify({})


@app.route("/submit_rating", methods=["POST"])
def submit_rating():
    data = request.json
    rating, id = data["rating"], data["id"]
    if not 1 <= rating <= 10:
        raise TypeError("Rating must be between 1 and 10.")
    cur.execute("SELECT rating_value, rating_count FROM item WHERE id = %s", (id,))
    previous_rating, count = cur.fetchone()
    new_rating = (previous_rating * count + rating) / (count + 1)
    cur.execute(
        "UPDATE item SET rating_value = %s, rating_count = %s WHERE id = %s",
        (new_rating, count + 1, id),
    )
    con.commit()
    return jsonify({})


@app.route("/ranking/popularity", methods=["GET"])
def sort_by_popularity():
    cur.execute("SELECT * FROM item ORDER BY rating_count DESC")
    return items_to_json(cur.fetchall())


@app.route("/ranking/quality", methods=["GET"])
def sort_by_quality():
    cur.execute("SELECT * FROM item ORDER BY rating_value DESC")
    return items_to_json(cur.fetchall())


if __name__ == "__main__":
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS item (
            id SERIAL PRIMARY KEY,
            name TEXT,
            description TEXT,
            rating_value FLOAT,
            rating_count INTEGER
        )
        """
    )
    app.run(debug=True)
