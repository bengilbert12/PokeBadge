from tinydb import TinyDB, Query

db = TinyDB('db.json')

table = db.table('trainers')

al = table.all()

for trainer in al:
    que = Query()
    table.upsert({'can_level': 'True'}, que['name'] == trainer['name'])