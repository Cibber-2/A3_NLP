# CS50 FITNESS
#### Description:

# Calorie Calculator Flask Application

This is a Flask application that provides a calorie calculator and a chat bot feature.

## Dependencies

The application uses the following dependencies:
- `os` module for accessing the environment variables.
- `openai` module for interacting with the OpenAI API.
- `Flask` for building the web application.
- `render_template` function for rendering HTML templates.
- `request` object for handling HTTP requests.
- `redirect` function for redirecting to a different URL.
- `apology` function (defined in a separate module) for displaying error messages.

## Configuration

- The OpenAI API key is stored in an environment variable called `API_KEY`.

## Routes

### Route: "/"

- Method: GET and POST
- Description: This is the main route of the application. When accessed with the GET method, it renders the "calorie_calculator.html" template, which displays a form for entering personal information for calorie calculation. When accessed with the POST method, it processes the form data, calculates the Total Daily Energy Expenditure (TDEE) based on the provided information, and renders the "result.html" template, which displays the calculated TDEE.

### Route: "/calorie_calculator"

- Method: GET
- Description: This route redirects to the main route ("/"). It is mainly used for redirecting users back to the calorie calculator page after submitting the form.

### Route: "/chat_bot"

- Method: GET and POST
- Description: This route provides a chat bot feature. When accessed with the GET method, it renders the "chat_bot.html" template, which displays a form for entering a question. When accessed with the POST method, it sends the question to the OpenAI API using the "text-davinci-002" model, retrieves the response, and renders the "chat_bot.html" template, displaying the original question and the generated response.

## Calorie Calculation

The application calculates the Total Daily Energy Expenditure (TDEE) using the provided personal information and activity level. Here's the formula used:

- For males: BMR = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
- For females: BMR = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

The calculated BMR (Basal Metabolic Rate) is then multiplied by a multiplier based on the selected activity level to get the TDEE.

## Chat Bot

The chat bot feature uses the OpenAI API to generate responses to user questions. The question entered by the user is used as a prompt for the API call, and the generated response is displayed back to the user.

The OpenAI API parameters used for generating the response are as follows:
- Model: "text-davinci-002"
- Temperature: 0.2 (low value for more focused responses)
- Max Tokens: 1024 (maximum length of the generated response)
- Top P: 1 (no truncation based on probability)
- Frequency Penalty: 0 (no penalty for repeating similar responses)
- Presence Penalty: 0 (no penalty for irrelevant or unrelated responses)


# Calorie Calculator HTML Template

This is an HTML template for the Calorie Calculator page.

## Template Inheritance

The template extends the "layout.html" template, indicating that it inherits its structure and styling.

## Block: title

- This block sets the title of the page as "Calorie Calculator".

## Block: main

- This block contains the main content of the page, including a form for entering personal information for calorie calculation.
- The form is wrapped in a container with a centered heading.
- A description is provided to explain the purpose of the form.
- The form includes the following input fields:
    - Age: A number input field for entering the age.
    - Gender: A dropdown select field for selecting the gender.
    - Height: A number input field for entering the height in centimeters.
    - Weight: A number input field for entering the weight in kilograms.
    - Activity: A dropdown select field for selecting the daily physical activity level.
- The form includes a submit button for calculating the calories.
- The form uses Bootstrap classes for styling.

## Footer

- The template includes a simple footer with a copyright notice.


# Chat Bot HTML Template

This is an HTML template for the Chat Bot page.

## Template Inheritance

The template extends the "layout.html" template, indicating that it inherits its structure and styling.

## Block: title

- This block sets the title of the page as "Chat Bot".

## Block: main

- This block contains the main content of the page, which includes a chat bot interface.
- The chat bot interface is contained within a container and centered heading.
- The interface consists of a card with a form for asking questions to the bot.
- The form includes a text input field for entering the question and a submit button.
- The form uses Bootstrap classes for styling.
- If a question is submitted (if `question` is defined), another card is displayed below the form.
- The card displays the original question asked by the user and the response generated by the bot.


# Results HTML Template

This is an HTML template for the Results page.

## Template Inheritance

The template extends the "layout.html" template, indicating that it inherits its structure and styling.

## Block: title

- This block sets the title of the page as "Results".

## Block: main

- This block contains the main content of the page, which displays the results of the calorie calculation.
- The results are presented in a table format using Bootstrap's table classes.
- The table has two columns: "Weight goal" and "Calories per day".
- The table body includes multiple rows, each representing a different weight goal and its corresponding recommended daily calorie intake.
- The values for daily calorie intake are dynamically inserted using Flask's template engine.

- Below the table, there is a card that provides additional information about the caloric recommendations.
- The card body contains multiple paragraphs explaining the effect of adjusting daily calorie intake on weight gain or loss.
- The values for calorie intake and weight changes are dynamically inserted using Flask's template engine.

- At the bottom of the card, there is a card footer that includes a small disclaimer explaining the limitations of the calculator.


