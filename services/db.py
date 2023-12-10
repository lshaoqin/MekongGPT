import os
import firebase_admin
from firebase_admin import db
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

cred_obj = firebase_admin.credentials.Certificate('mekonggpt-firebase-adminsdk-tl6je-751134b214.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL': os.getenv('FIREBASE_URL')
	})

ref = db.reference('/')

def get_refresh_token():
	return ref.get()['REFRESH_TOKEN']

def set_refresh_token(token):
	ref.update({'REFRESH_TOKEN': token})

def store_reply(query, answer):
	ref.child('replies').push({
		'query': query,
		'answer': answer,
		'time' : str(datetime.now())
		})