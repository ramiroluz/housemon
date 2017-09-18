[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# House Monitor energy sensor clustering

This project parses, saves, proccess and generate simple reports of energy sensor installed on some home.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need python3, scikit-learn and Flask to run this project. In a debian system you can run the following commands:

```
$ sudo apt install virtualenvwrapper
$ echo -e "# Enable virtualenvwrapper\nsource /usr/share/virtualenvwrapper/virtualenvwrapper.sh" >> ~/.bashrc
$ source ~/.bashrc   # with this you don't need to exit and enter bash/terminal again.
$ mkdir -p ~/projects/python/
$ cd ~/projects/python
$ git clone git@github.com:ramiroluz/homemon.git
$ cd homemon
$ mkvirtualenv -p /usr/bin/python3 housemon
$ setvirtualenvproject   # next time you run: workon homemon
$                        # and you will be in this same directory.
$ pip install -r requirements.txt
```

## Running the tests

To run the tests:

```
$ make test
```

If you rather prefer py.test:

```
$ make py.test
```

## To see it in action (NOT IMPLEMENTED YET)

To run it:

```
$ make run
```

Then access the following url: http://localhost:8000

## TODO

* Create the database model.
* Create web application.
* Create the report.

## Deploying

There is no deploy instructions yet, but it works like any regular Flask application.

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Flask RestFul](https://flask-restful.readthedocs.io/en/latest/) - Extension to create an API
* [scikit-learn](http://scikit-learn.org/stable/) - Machine Learning Lib

## Authors

* **Ramiro Batista da Luz** - [RamiroLuz](https://github.com/ramiroluz)

## License

This project is licensed under the GNU-GPLv3 License - see the [LICENSE.md](LICENSE.md) file for details
