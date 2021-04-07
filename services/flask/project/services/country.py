from project import mongo

def fetchCountries():
    _countries = mongo.db.country.find()
    return _countries

def addCountry(data):
    mongo.db.todo.insert_one(data)
