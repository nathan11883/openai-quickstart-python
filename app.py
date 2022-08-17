# http://127.0.0.1:5000/
import os
from tkinter.messagebox import QUESTION

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        QUESTION = request.form["question"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(QUESTION),
            temperature=0,max_tokens=600,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(QUESTION):
    return """{}""".format(
        QUESTION.capitalize()
    )
