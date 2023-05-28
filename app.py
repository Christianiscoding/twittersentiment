from flask import Flask

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    data = {'message': 'Hello from Letes go!'}
    return data

if __name__ == '__main__':
    app.run()

