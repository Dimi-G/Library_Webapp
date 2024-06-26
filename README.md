## Website for managing personal (book) library
A python application using Flask framework for the web application, Flask-WTF for the Form classes, Flask_sqlalchemy for the database querying,
& Bootstrap-Flask, a collection of Jinja macros for rendering Flask-related data and objects to Bootstrap markup HTML.

## Features
  - Manually add book, author and rating
  - Search book via Google Books API and add it
  - Update rating
  - Delete book from database

  ![demo](static/demo.gif)

## Setup
1. Clone the repository:

    ```bash
    git clone https://github.com/Dimi-G/Library_Webapp.git
    ```

2. Create and activate a virtual environment:

    ```bash
    pip python3 -m venv .venv
    .venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create the database:

    ```bash
    python3 bookdatabaser.py
    ```

5. Run the application:

    ```bash
    python3 main.py
    ```

    The application will be available at `http://localhost:5000`.

## Project Structure

The project follows a standard Flask application structure:

- `app.py`: The main entry point for the application.
- `instance/books.db`: The book database.
- `templates/`: HTML templates for rendering pages.
- `static/`: Static files such as images, CSS and JavaScript.

## Contributing
Contributions are welcome! If you have any improvements or bug fixes, feel free to submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

