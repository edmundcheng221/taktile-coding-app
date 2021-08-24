from re import sub
import threading
from flask import Flask, render_template, redirect, request

app = Flask(__name__) 

class Fold:
    
    """
    Fold left:
    [a, b, c, d]
    operator can be +, -, *, /
    let us use + for example
    return a + b + c + d
    if there is a starting number specified
    return ((((starting + a) + b) + c) + d)
    """
    @staticmethod
    def fold_left(operation, lst, starting=None):
        try:
            if len(lst) == 0:
                print("empty list")
                return 0
            if starting is not None:
                lst.insert(0, starting)
            res = lst[0]
            for num,ele in enumerate(lst):
                if num+1 < len(lst):
                    res = operation(res, lst[num+1])
            return res
        except ZeroDivisionError:
            return None

    """
    Fold right:
    [a, b, c, d]
    operator can be +, -, *, /
    let us use + for example
    
    return (a + (b + (c + d)))
    
    if there is a starting number specified
    
    return (starting + (a + (b + (c + d))))
    """

    @staticmethod
    def fold_right(operation, lst, starting=None):
        try:
            if len(lst) == 0:
                print("empty list")
                return 0
            if starting is not None:
                new_lst = lst[::-1]
                res = operation(new_lst[0],starting)
                new_lst.pop(0)
                for ele in new_lst:
                    res = operation(ele,res)
                return res
            else:
                new_lst = lst[::-1]
                res = new_lst[0]
                new_lst.pop(0)
                for ele in new_lst:
                    res = operation(ele,res)
                return res
        except ZeroDivisionError:
            return None


def add(item1, item2):
    return item1 + item2


def subtract(item1, item2):
    return item1 - item2


def multiply(item1, item2):
    return item1 * item2


def divide(item1, item2):
    # Cannot divide by 0
    if item2 == 0:
        raise ZeroDivisionError
    return item1 / item2


@app.route("/") 
def index(): 
   return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
   text = request.form['text']
   fold_type = request.form['fold']
   operation = request.form['operation']
   lst = text.split(",")
   new_lst = [int(x) for x in lst]
   instance = Fold()
   if str(fold_type).upper() == "LEFT": 
      if str(operation).upper() == "ADD": 
         output = instance.fold_left(add, new_lst)
      elif str(operation).upper() == "SUBTRACT": 
         output = instance.fold_left(subtract, new_lst)
      elif str(operation).upper() == "MULTIPLY": 
         output = instance.fold_left(multiply, new_lst)
      elif str(operation).upper() == "DIVIDE": 
         output = instance.fold_left(divide, new_lst)
      else:
         raise Exception("Invalid operation; check spelling")
   elif str(fold_type).upper() == "RIGHT": 
      if str(operation).upper() == "ADD": 
         output = instance.fold_right(add, new_lst)
      elif str(operation).upper() == "SUBTRACT": 
         output = instance.fold_right(subtract, new_lst)
      elif str(operation).upper() == "MULTIPLY": 
         output = instance.fold_right(multiply, new_lst)
      elif str(operation).upper() == "DIVIDE": 
         output = instance.fold_right(divide, new_lst)
      else:
         raise Exception("Invalid operation; check spelling")
   else:
      raise Exception("Invalid fold")

   return render_template('index.html', result="The answer is: " + str(output))


if __name__ == '__main__': 
   app.run(port=5000, debug=True)