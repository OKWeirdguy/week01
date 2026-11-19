from flask import Flask         # this Flask is class

app = Flask(__name__)           # this Flask is object

@app .route('/')                # route is homepage
def home():                     # 6-7th line is the function in the homepage and as you can see that "def" is how you make function 
  return "Hello World!"

if __name__ == '__main__':
  app.run()