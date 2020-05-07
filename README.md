# Flask-Login

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) 
![GitHub repo size](https://img.shields.io/github/repo-size/SpencerOfwiti/Flask-Login.svg)
![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
[![contributors](https://img.shields.io/github/contributors/SpencerOfwiti/Flask-Login.svg)](https://github.com/SpencerOfwiti/Flask-Login/contributors)

A Flask application for performing User authentication with Flask-Login and Flask-SQLAlchemy.

## Table of contents
* [Built With](#built-with)
* [Features](#features)
* [Code Example](#code-example)
* [Contributions](#contributions)
* [Bug / Feature Request](#bug--feature-request)
* [Authors](#authors)
* [License](#license)
* [Acknowledgements](#acknowledgments)


## Built With
* [Python 3.6](https://www.python.org/) - The programming language used.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used.
* [Flask Login](https://flask-login.readthedocs.io/en/latest/) - The user session management library used.
* [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - The object relational mapper used.

## Features

- Create a user.

## Code Example

```python
class User(UserMixin, db.Model):
    """
    Creating a User object
    """
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
```

## Contributions

To contribute, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).


## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/SpencerOfwiti/Flask-Login/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/SpencerOfwiti/Flask-Login/issues/new). Please include sample queries and their corresponding results.

## Authors

* **[Spencer Ofwiti](https://github.com/SpencerOfwiti)** - *Initial work* 
    
[![github follow](https://img.shields.io/github/followers/SpencerOfwiti?label=Follow_on_GitHub)](https://github.com/SpencerOfwiti)
[![twitter follow](https://img.shields.io/twitter/follow/SpencerOfwiti?style=social)](https://twitter.com/SpencerOfwiti)

See also the list of [contributors](https://github.com/SpencerOfwiti/Flask-Login/contributors) who participated in this project.

## License

This project is licensed under the MIT license - see the [LICENSE](LICENSE) file for details
