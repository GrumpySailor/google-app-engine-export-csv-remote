from google.appengine.ext import ndb
from models import Person
from random import randint, choice
import webapp2


class MainPage(webapp2.RequestHandler):
	def get(self):
		given_names = [
			'Claire',
			'Emily',
			'James',
			'Kate',
			'Maple',
			'Marcio',
			'Mauricio',
			'Paula',
			'Rachel',
			'Rosalind'
		]

		surnames = [
			'Ball',
			'Barbosa',
			'Black',
			'Book',
			'Chair',
			'Cucumber',
			'Dog',
			'Googleson',
			'Johnson',
			'Jordan',
			'Lettuce',
			'Pineaple',
			'Smith',
			'Table',
			'White',
			'Windred'
		]

		num_items = 1000
		limit_per_batch = 200

		print 'Start saving.'

		for i in range(0, int(num_items / limit_per_batch)):
			people_list = []
			for j in range(0, limit_per_batch):
				person = Person()
				person.name = '%s %s' % (choice(given_names), choice(surnames))
				person.status = randint(0, 2)
				people_list.append(person)
			ndb.put_multi(people_list)

		print 'People added.'
		self.response.out.write(str(num_items) + ' people added')

application = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)
