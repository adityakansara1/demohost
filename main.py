from flask import Flask, render_template

app = Flask(__name__, template_folder="templets")


@app.route("/")
def adi():
    name = "Aditya Kansara"
    return render_template('index.html', name=name)


@app.route("/about")
def kan():
    framework = "FLASK"
    return render_template('about.html', framework=framework)


if __name__ == "__main__":
    app.run()
