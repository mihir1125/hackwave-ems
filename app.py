from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    # Here you can process the user_input, maybe pass it to a chatbot model
    # and get a response
    # For demonstration purposes, let's just echo back the input
    bot_response = f"You said: {user_input}"
    return bot_response

if __name__ == '__main__':
    app.run(debug=True)
