# Documentation

## Problem

#### Instructions

Fork this repository.

Implement `fold` in any language of your choice. Don't directly use the `fold` that is
already part of your language (see the list on Wikipedia).

Send us a link to your fork **within 1 week** of being invited to participate on this challenge.

Aim to use about 1 hour of time on the solution, don't use more than 2 hours. We give roughly
equal weight to the each of the following:

* Documentation
* Packaging
* Testing
* Readability of code
* Correctness of implementation
* Performance
* Generality
* Correntness of types (if applicable)

Please don't stress if your solution isn't perfect. With a timebox of at most 2 hours, 
you most likely won't be able to check all the boxes above. This challenge is intended as an 
exercise in tradeoffs. We want to understand how you view the overall value and lifecycle
of software.

## Solution

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
