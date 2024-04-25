# Ranking

This is a project for ranking items (this could be books, albums, headphones,
whatever). The goal is to have multiple users rate items and sort based on a
combination of aggregate rating and popularity. The project currently only
depends on `flask` and `psycopg2` and uses Docker Compose, just run
`sudo docker-compose up -d` and use curl to interact with the API.
