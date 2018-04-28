TODO fix start of readme

Issue Tracker
---

<img align="center" src="/static/img/screenshots/homepage.png" width="700">

**Issue Tracker** is a web application designed to let foodies search restaurants, track their eating history, as well as connect with friends. If you have trouble remembering what restaurants you’ve been to before, or what you’ve ordered at a restaurant that was good, then Breadcrumbs is your go-to app.

Search for restaurants by name or address. With the queried results, you can select and add a restaurant that you have visited to your own personal map, leaving behind a trail of Issue Tracker for your restaurant history. Connect with friends to see where your friends have dined at and what dishes they've tried. Breadcrumbs is a social media network built for foodies.

Issue Tracker is created with love, sweat, and tears by Ashley Hsiao. You can connect with Ashley by [email](mailto:aiyihsiao@gmail.com), [LinkedIn](http://linkedin.com/in/ashleyhsia0), or [Twitter](http://twitter.com/ashleyhsia0).

## Table of Contents

1. [Technologies](#technologies)
3. [Installation](#installation)
7. [Author](#author)

## <a name="technologies"></a>Technologies

**Front-end:** [HTML5](http://www.w3schools.com/html/), [CSS](http://www.w3schools.com/css/), [Bootstrap](http://getbootstrap.com), [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript), [jQuery](https://jquery.com/)

**Back-end:** [Python](https://www.python.org/), [Flask](http://flask.pocoo.org/), [Jinja2](http://jinja.pocoo.org/docs/dev/), [MongoDB](https://www.mongodb.com/), [PyMongo](https://api.mongodb.com/python/current/)

**APIs:** [Yelp](https://www.yelp.ca/developers/documentation/v2/overview), [Google Maps](https://developers.google.com/maps/)

## <a name="installation"></a>Installation

### Prerequisite:

Install [MongoDB](https://www.mongodb.com/).

(On Ubuntu 16)
```
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5

$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list

$ sudo apt-get update

$ sudo apt-get install -y mongodb-org

$ sudo service mongod start
```

Also, you can install [Robo3T](https://robomongo.org/) if you want to control MongoDB via GUI

### Set up Breadcrumbs:

Clone this repository:

```$ git clone https://github.com/seyahdoo/issue-tracker.git```

Create a virtual environment and activate it:

```
$ virtualenv env
$ source env/bin/activate
```

Install the dependencies:

```$ pip install -r requirements.txt```

Run MongoDB.

To run the app, start the server:

```$ python server.py```

Go to `localhost:8080` in your browser to start using Issue Tracker!


## Thanks for original author
## <a name="authoe"></a>Author
Ashley Hsiao is a Software Engineer living in Vancouver, BC.
[Email](mailto:aiyihsiao@gmail.com) | [LinkedIn](http://linkedin.com/in/ashleyhsia0) | [Twitter](http://twitter.com/ashleyhsia0).
