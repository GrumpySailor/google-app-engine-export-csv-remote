##Google App Engine CSV Exporter

based on [gergelyorosz/gae-export-as-csv](https://github.com/gergelyorosz/gae-export-as-csv)

remember to run the following scripts inside the project's folder.


### Localhost:
<!-- localhost -->
	$ remote_api_shell.py -s localhost:8080 -p /_ah/remote_api

###Live server:
<!-- live server -->
	$ remote_api_shell.py -s gae-export-csv-remote.appspot.com

then run:

	$ import export_csv
	$ export_csv.people_approved()
	$ export_csv.people_all()
