# Youtube-Video-Collector

Youtube-Video-Collectoris a Python app for collecting youtube video details for a specific topic (here cricket).

## Installating Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Steps to run

- Set up postgres database and change the db_name and password in settings.py accordingly
- Set an environment variable for API_KEY (using to hide in code)
- create a superuser to visit the [admin page](http://127.0.0.1:8000/admin) :
```bash
python manage.py createsuperuser
```
- Run the server :
```bash
python manage.py runserver
```
- Running background tasks(There is a management command to run tasks that have been scheduled):

```bash
python manage.py process_tasks
```

You will find the project hosted at the [local server](http://127.0.0.1:8000/) and the home page is the api response page.



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)