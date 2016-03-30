import pymongo

def get_db(db_name):
	client = pymongo.MongoClient
	db = client[db_name]
	return db