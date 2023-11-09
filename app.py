import openai
from dotenv import dotenv_values
from flask import Flask, render_template, request
import json

## Setting OpenAI API

config = dotenv_values('.env')
openai.api_key = config['OPENAI_API_KEY']

## Prompt background

def get_colors(msg):
    prompt = """
            You are an expert generator of color palletes based on text prompts.
            You should generate color palettes that fir the theme, mood, or instructions in the prompt.
            The palettes should be between 2 and 5 colors if the number desired is not specified.
            
            Desired format: a JSON array of hexadecimal color codes
            
            text: {msg}
            result:
            """

    response = openai.Completion.create(
        prompt= prompt,
        model= "text-davinci-003",
        max_tokens= 200
    )
    
    colors = json.loads(response['choices'][0]['text'])
    return colors


## Setting the app
app = Flask(__name__,
            template_folder='templates')

@app.route("/palette", methods=['POST'])
def prompt_to_palette():

    query = request.form.get("query")
    colors = get_colors(query)

    return {"colors": colors}

@app.route("/")
def index():
    
    return render_template("index.html", encoding="utf-8")

if __name__ =="__main__":
    app.run(debug=True)