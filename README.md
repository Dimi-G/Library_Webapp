## Website for managing personal (book) library
Using Flask framework for the web application, Flask-WTF for the Form classes, Flask_sqlalchemy for the database querying,
& Bootstrap-Flask, a collection of Jinja macros for rendering Flask-related data and objects to Bootstrap markup HTML.
Will be expanded to API usage for book suggestions/want-to-read lists.

## Features
  - Add book, author and rating
  - Edit rating
  - Delete rating

## Installation
- Web demo version can be found [here](https://library-webapp.onrender.com)
- For local usage change to the following in main.py: app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

## Contributing
If you'd like to contribute to the project, please follow these steps:

Fork the repository.
Create a new branch: git checkout -b feature/my-feature.
Commit your changes: git commit -m 'Add some feature'.
Push to the branch: git push origin feature/my-feature.
Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

