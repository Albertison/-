from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Миссия Колонизация Марса"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def erion():
    aer = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
           "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return '<br>'.join(aer)


@app.route("/image_mars")
def marsian():
    with open("image_mars.html", 'r', encoding='utf-8') as html_str:
        return html_str.read()


@app.route('/promotion_image')
def test():
    with open("second.html", "r", encoding='utf-8') as strig:
        return strig.read()


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
