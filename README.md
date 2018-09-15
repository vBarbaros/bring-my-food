# [Bring My Food](https://bring-my-food.herokuapp.com/)
# Bring-My-Food Web App
<table>
<tr>
<td>
  A webapp showcasing the implementation of the main components for a Flask application, demonstrating the main components of an "Ask for Waiter" in a restaurant and keeping track of your orders.
</td>
<td>
  It also show how to integrate and make use of MongoDB, ensure secure authentication with haslib, and apply url-obfuscation with bitlyhelper.
</td>
</tr>
</table>


## Hosted 

- [Heroku](https://www.heroku.com/about) - Heroku is a container-based cloud Platform as a Service (PaaS).

- Check the [bring-my-food-production](https://bring-my-food.herokuapp.com/) instance;

- !!! No split of this project in dev, staging, production since the limit for free web apps, hosted on Heroku (for free), is very small [hey, give me some money and I'll apply the full dev-cycle ;) ]


### Landing Page

![Home Page](bringmf-screenshots/01-home.png)

### Account Page

![Once Logged In, Access Your Account](bringmf-screenshots/02-account.png)

### Account Page - New Request Created

![From Your Account and Generate Your Request](bringmf-screenshots/03-account-newrequest.png)

### Account Page - Send New Request

![Use the Obfuscated Url to Send Your Request](bringmf-screenshots/04-send-request.png)

### Dashboard Page

![Track the Progress of Your Request](bringmf-screenshots/05-dashboard-track-request.png)

### [Development](https://github.com/vBarbaros/bring-my-food/blob/dev/CONTRIBUTING.md)
Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 

### Bug / Feature Request

If you find a bug kindly open an issue [here](https://github.com/vBarbaros/bring-my-food/issues/new) by including the steps to reproduce it.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/vBarbaros/bring-my-food/issues/new).


## Built with 

- [Flask](http://flask.pocoo.org/docs/1.0/) - Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. And before you ask: It's BSD licensed!.


## Credits

- The Book [Flask: Building Python Web ServicesGareth Dwyer, Shalabh Aggarwal, Jack Stouffer](https://www.packtpub.com/web-development/flask-building-python-web-services) While using the tutorials described in this book, I made the following improvement:
	1) adapted the overall architecture of the current Flask webapp to a more reusable one;
	2) added a mock-database, to make it usable and deployable on Heroku (but with a locally installed MongoDB, it works fine with the real DB);
	3) prepared the necesary files to make it deployable to Heroku in seconds!!!

## To-do
- Add Unit Tests;
- Add CI using Travis CI;
- Improve upon app's architecture, using templates and styling;
- Integrate the app with a real MongoDB DataBase, directly on Heroku (with a locally installed MongoDB, it works fine, though);
- (...to be added, there is always stuff that can be added);


## [License](https://github.com/vBarbaros/bring-my-food/blob/dev/LICENSE)

MIT © [Victor Barbaros](https://github.com/vBarbaros)
