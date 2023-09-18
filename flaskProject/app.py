from flask import Flask
import main
app = Flask(__name__)


def fonction():
    return "sa marche!"


uneVar = fonction()
print(uneVar)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/{hour}")
def var(hour: str):
    return main.testtest(hour)


if __name__ == '__main__':
    app.run()
