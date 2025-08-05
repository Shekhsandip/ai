from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Initialize OpenAI API (Replace with your API key)
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json["message"]

    # Using GPT model to generate AI response
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_message,
        max_tokens=100
    )

    reply = response.choices[0].text.strip()
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
