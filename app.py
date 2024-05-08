import os
import openai

from flask import Flask, render_template, request, redirect
from helpers import apology

app = Flask(__name__)

openai.api_key = os.getenv("API_KEY")

@app.route("/", methods=["GET", "POST"])
def calories():
    """Show Calorie Calculator"""
    if request.method == 'GET':
        return render_template("calorie_calculator.html")

    else:
        age = int(request.form['age'])
        if age <= 0:
            return apology("Must provide a positive number for age")

        gender = request.form['gender']

        height = int(request.form['height'])
        if height <= 0:
            return apology("Must provide a positive number for height")

        weight = int(request.form['weight'])
        if weight <= 0:
            return apology("Must provide a positive number for weight")

        activity = request.form['activity']

        if gender == 'male':
            bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
        else:
            bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

        if activity == 'sedentary':
            tdee = bmr * 1.2
        elif activity == 'light':
            tdee = bmr * 1.375
        elif activity == 'moderate':
            tdee = bmr * 1.55
        elif activity == 'very_active':
            tdee = bmr * 1.725
        elif activity == 'extremely_active':
            tdee = bmr * 1.9

        return render_template('result.html', tdee=tdee)

@app.route("/calorie_calculator")
def calorie_calculator():
    return redirect("/")

@app.route("/chat_bot", methods=["GET", "POST"])
def chat_bot():
    if request.method == "GET":
        return render_template("chat_bot.html")

    else:
        question = request.form['question']

        completion = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"Q: {question}\nA:",
            temperature=0.2,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        response = completion.choices[0].text.strip()

        return render_template("chat_bot.html", question=question, response=response)
