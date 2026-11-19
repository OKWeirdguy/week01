from flask import Flask         # this Flask is class

app = Flask(__name__)           # this Flask is object

@app .route('/')                # route is homepage
def index():                     # 6-7th line is the function in the homepage and as you can see that "def" is how you make function 
  return "<h2>Hello World!</h2>"# you can do the HTML too

if __name__ == '__main__':
  app.run(debug=True)