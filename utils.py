import random
from tinydb import Query, TinyDB
from tinydb.operations import set

db = TinyDB('db.json')

def get_streamer(streamer):
    streamer_table = db.table('streamers')
    Streamer = Query()
    streamer = streamer_table.search((Streamer.name == streamer))
    return streamer

def get_trainer(streamer, user):
    trainer_table = db.table('trainers')
    Trainer = Query()
    trainer = trainer_table.search((Trainer.streamer == streamer) & (Trainer.name == user))
    if not trainer:
        return None
    return trainer[0]

def create_trainer(streamer, user):
    trainer_table = db.table('trainers')
    trainer_id = trainer_table.insert({'name': user, 'pokemon': '', 'level': 1, 'can_level': False, "streamer": streamer})
    trainer = trainer_table.get(doc_id=trainer_id)
    return trainer

def get_or_create_trainer(streamer, user):
    trainer = get_trainer(streamer, user)
    if not trainer:
        trainer = create_trainer(streamer, user)

    return trainer

def get_random_poke():
    poke_table = db.table("pokemon")
    pokes = poke_table.all()
    poke = random.choice(pokes)
    return str(poke['name'])

def get_poke(streamer, user):
    trainer = get_or_create_trainer(streamer, user)
    print(f'{trainer=}')
    return trainer['pokemon']


def create_poke(streamer, user):
    trainer_table = db.table("trainers")
    random_poke = get_random_poke()
    Trainer = Query()
    if streamer == 'dynamungo':
        random_poke = 'Pep' + random_poke[3:]
    trainer_table.update(set("pokemon", random_poke), ((Trainer.name == user) & (Trainer.streamer == streamer)))
    return random_poke
    

def get_or_create_poke(streamer, user):
    poke = get_poke(streamer, user)
    return poke or create_poke(streamer, user)

def can_level(streamer, user):
    trainer = get_trainer(streamer, user)
    return trainer["can_level"]

def get_level(streamer, user):
    return get_trainer(streamer, user)['level']

def level_up_poke(streamer, user):
    trainer_table = db.table('trainers')
    Trainer = Query()
    trainer = get_trainer(streamer, user)
    if can_level(streamer, user):
        trainer_table.update(set('level', trainer['level'] + 1), ((Trainer.name == user) & (Trainer.streamer == streamer)))
        trainer_table.update(set('can_level', False), ((Trainer.name == user) & (Trainer.streamer == streamer)))

        return get_level(streamer, user)
    return None