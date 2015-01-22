import csv
from datetime import date
from models import Person

def _export_to_csv(query, csv_filename, delimiter):
	with open(csv_filename, 'wb') as csv_file:
		csv_writer = csv.writer(csv_file, delimiter=delimiter, quotechar='|', quoting=csv.QUOTE_MINIMAL)
		_write_header(csv_writer)

		page_size = 500
		cursor = None
		has_data = True

		print 'Exporting people...'
		while has_data:
			result, next_cursor, more = query.fetch_page(page_size, start_cursor=cursor)

			for item in result:
				_save_item(csv_writer, item)

			if next_cursor and more:
				cursor = next_cursor
			else:
				has_data = False

		print 'Export completed.'

def _write_header(csv_writer):
	csv_writer.writerow(['Name', 'Date'])

def _save_item(csv_writer, item):
	csv_writer.writerow([item.name, item.date])

def people_approved(filename='people-approved.csv'):
	filename = str(date.today()) + '-' + filename
	query = Person.query(Person.status == 2).order(Person.date)
	_export_to_csv(query, filename, ',')

def people_all(filename='people-all.csv'):
	filename = str(date.today()) + '-' + filename
	query = Person.query().order(Person.date)
	_export_to_csv(query, filename, ',')
