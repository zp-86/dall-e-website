from flask import Flask, render_template, request, redirect, url_for, flash
from openai_multi_client import OpenAIMultiClient

api = OpenAIMultiClient(endpoint="images",
                        data_template={"model": "dall-e-3"})





app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index(img1=None, img2=None, img=0):
    if "submit" in request.form:
        prompt = request.form["prompt"]
        def make_requests():
            for num in range(1, 3):
                api.request(data={
                    "model": "dall-e-3", "prompt": prompt, "size": "1024x1024", "quality": "standard"
                }, metadata={'num': num})
        api.run_request_function(make_requests)
        for result in api:
            num = result.metadata['num']
            response = result.response.data[0].url
            img += 1
            if img1 is None:
                img1 = response
            else:
                img2 = response
        img = 0
    return render_template('index.html', img1=img1, img2=img2)


app.run(debug=True)
