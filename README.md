# Documentation

This is a flask app that allows for users to specify array, left or right fold, and the operation.

To clone repo:

`git clone https://github.com/edmundcheng221/taktile-coding-app.git`

Navigate to project directory:

`cd project`

Run Unit Tests:

`python3 test_fold.py`

# Activate environment

* Note that these commands are for macOS. YMMV depending on your OS.

Activate environment:

`source env/bin/activate`

Specify app.py:

`export FLASK_APP=app.py`

Enter development environment:

`export FLASK_ENV=development`

Run app:

`flask run`

# Install dependencies

`pip3 install -r requirements.txt`

# Using application

- Please pass an array of items into the input field.
- Make sure you type the array in this exact format: a,b,c.
- Comma separated, no spaces.
- Please enter either left or right fold.
- Type in an operation (add, multiply, subtract, or divide).
- Make sure the spelling is correct.