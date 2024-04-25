import psycopg2

con = psycopg2.connect(
    dbname="item",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)
cur = con.cursor()


def upload_item(name: str, description: str) -> int:
    cur.execute('''
        INSERT INTO item (name, description, rating_value, rating_count) VALUES (%s, %s, %s, %s)
    ''', (name, description, 0., 0))
    con.commit()
    return cur.lastrowid #wrong

def delete_item(id: int) -> None:
    cur.execute('DELETE FROM item WHERE id = %s', (id,))
    con.commit()

def apply_rating(id: int, rating: int) -> None:
    if not 1 <= rating <= 10:
        raise TypeError("Rating must be an integer between 1 and 10.")
    cur.execute('SELECT rating_value, rating_count FROM item WHERE id = %s', (id,))
    previous_rating, count = cur.fetchone()
    new_rating = (previous_rating * count + rating) / (count + 1)
    cur.execute('UPDATE item SET rating_value = %s, rating_count = %s WHERE id = %s', (new_rating, count+1, id))
    con.commit()

def sort_by_popularity():
    cur.execute('SELECT * FROM item ORDER BY rating_count DESC')
    return cur.fetchall()

def sort_by_quality():
    cur.execute('SELECT * FROM item ORDER BY rating_value DESC')
    return cur.fetchall()


if __name__ == "__main__":
    cur.execute('''
        CREATE TABLE IF NOT EXISTS item (
            id SERIAL PRIMARY KEY,
            name TEXT,
            description TEXT,
            rating_value FLOAT,
            rating_count INTEGER
        )
        '''
    )
