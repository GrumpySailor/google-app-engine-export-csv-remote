from google.appengine.ext import ndb

class Person(ndb.Model):
	name = ndb.StringProperty()
	status = ndb.IntegerProperty(default=1)
	date = ndb.DateTimeProperty(auto_now_add=True)
