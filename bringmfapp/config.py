use_on_heroku = True
use_mockDB = True
base_url = ''


if use_on_heroku:
    base_url = 'https://bring-my-food.herokuapp.com/'
else:
    base_url = 'http://127.0.0.1:5000/'
