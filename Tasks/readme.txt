run commands:


pip install -r requirements.txt
gunicorn -b localhost:<portnumber> serve:application --reload


