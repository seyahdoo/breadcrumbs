"""Utility file to seed info from Yelp API into the breadcrumbs database"""

from sqlalchemy import func
import sqlalchemy

from model import connect_to_db, db

from server import app

if __name__ == "__main__":

    # NUKE DB
    # sudo su postgres
    # createuser dbuser
    # createdb dbuser
    # psql
    # ALTER USER dbuser PASSWORD '1234';
    # ALTER USER dbuser WITH SUPERUSER;

    engine = sqlalchemy.create_engine(
        "postgresql://dbuser:1234@localhost",
        isolation_level='AUTOCOMMIT')
    conn = engine.connect()

    try:
        conn.execute("drop database issuetracker")
    except Exception as e:
        pass

    conn.execute("create database issuetracker")
    conn.close()

    connect_to_db(app)

    # Configure mappers before creating tables in order for search trigger in
    # SQLAlchemy-Searchable to work properly
    db.configure_mappers()

    # In case tables haven't been created, create them
    db.create_all()

    db.session.commit()
