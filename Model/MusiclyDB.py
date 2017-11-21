from pony.orm import *

def define_entities(db):
    class Person(db.Entity):
        name = Required(unicode)
        pets = Set('Pet')

    class Pet(db.Entity):
        name = Required(unicode)
        kind = Required(unicode)
        owner = Required('Person')

def define_database(**db_params):
    db = Database(**db_params)
    define_entities(db)
    #set_sql_debug(True)
    db.generate_mapping(create_tables=True)
    return db

db = define_database(provider='sqlite', filename='musicly.db', create_db=True)

select(p for p in db.Person)