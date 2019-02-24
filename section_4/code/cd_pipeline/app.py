from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/13/enhanced/webdr10/anigif_enhanced-3148-1446487779-9.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/10/enhanced/webdr13/anigif_enhanced-5483-1446477662-2.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
