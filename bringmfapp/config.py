use_on_heroku = False
use_mockDB = True
base_url = ''


if use_on_heroku:
    base_url = 'https://dashboard.heroku.com/apps/bring-my-food/'
else:
    base_url = 'http://127.0.0.1:5000/'
