from flask import Flask         # this Flask is class

app = Flask(__name__)           # this Flask is object

if __name__ == '__main__':
  app.run()