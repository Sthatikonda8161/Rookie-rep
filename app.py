from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def helloworld():
    return 'Hello world'

@app.route('/aboutus', methods=['GET'])
def aboutworld():
    return 'About Us'


if __name__=="__main__":
    app.run(port=3000, debug=True)