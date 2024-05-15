import os
from flask import Flask, render_template, request, redirect, url_for, flash
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("API KEY HERE"),
)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index(img1=None, img2=None):
    if "submit" in request.form:
        prompt = request.form["prompt"]
        response = client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            n=2,
            size="1024x1024"
        )
        img1 = response.data[0].url
        img2 = response.data[1].url
    return render_template('index.html', img1=img1, img2=img2)


app.run()
