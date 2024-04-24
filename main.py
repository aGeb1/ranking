import numpy as np
import sqlite3
import base64

con = sqlite3.connect("item.db")
cur = con.cursor()


# Serialization
def serialize_rating(rating_array: np.ndarray) -> str:
    return base64.b64encode(rating_array.tobytes()).decode('utf-8')

def deserialize_rating(rating_base64: str) -> np.ndarray:
    return np.frombuffer(base64.b64decode(rating_base64))


# Database Manipulation
def upload_item(name: str, description: str) -> int:
    empty_rating = serialize_rating(np.zeros(10))
    cur.execute('''
        INSERT INTO item (name, description, rating) VALUES (?, ?, ?)
    ''', (name, description, empty_rating))
    con.commit()
    return cur.lastrowid

def delete_item(id: int) -> None:
    cur.execute('DELETE FROM item WHERE id = ?', (id,))
    con.commit()

def apply_rating(id: int, rating: int) -> None:
    if not 1 <= rating <= 10:
        raise TypeError("Rating must be an integer between 1 and 10.")
    delta = np.zeros(10)
    delta[rating-1] = 1
    cur.execute('SELECT rating FROM item WHERE id = ?', (id,))
    previous_rating = deserialize_rating(cur.fetchone()[0])
    new_rating = serialize_rating(previous_rating + delta)
    cur.execute('UPDATE item SET rating = ? WHERE id = ?', (new_rating, id))
    con.commit()

def sort_by_popularity():
    def custom_sort(row):
        return np.dot(deserialize_rating(row[3]), np.ones(10))
    cur.execute('SELECT * FROM item')
    data = cur.fetchall()
    return sorted(data, key=custom_sort, reverse=True)

def sort_by_quality(popularity_weight: int):
    def custom_sort(row):
        unadjusted_rating = np.dot(deserialize_rating(row[3]), np.linspace(0.5, 5, 10))
        rating_count = np.dot(deserialize_rating(row[3]), np.ones(10))
        if rating_count == 0:
            return 0
        else:
            return (unadjusted_rating * np.log(rating_count)) / (rating_count * popularity_weight)
    cur.execute('SELECT * FROM item')
    data = cur.fetchall()
    return sorted(data, key=custom_sort, reverse=True)

if __name__ == "__main__":
    cur.execute('''
        CREATE TABLE IF NOT EXISTS item (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            rating INTEGER
        )
        '''
    )
