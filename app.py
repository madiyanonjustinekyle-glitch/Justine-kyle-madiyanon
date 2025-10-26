from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    # Inline HTML + CSS for the homepage
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask API Home</title>
        <style>
            body {
                font-family: 'Poppins', Arial, sans-serif;
                background: linear-gradient(135deg, #007BFF, #00C6FF);
                color: #333;
                margin: 0;
                padding: 0;
            }
            .container {
                background: #fff;
                max-width: 700px;
                margin: 100px auto;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
                text-align: center;
            }
            h1 {
                color: #007BFF;
                margin-bottom: 10px;
            }
            p {
                font-size: 1.1rem;
                color: #555;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                text-decoration: none;
                background: #007BFF;
                color: white;
                padding: 12px 20px;
                border-radius: 8px;
                transition: 0.3s;
            }
            a:hover {
                background: #0056b3;
            }
            footer {
                margin-top: 40px;
                font-size: 0.9rem;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to My Flask API!</h1>
            <p>This is a simple enhanced Flask app with embedded HTML and CSS styling.</p>
            <a href="/student">View Student JSON Data</a>
            <footer>
                <p>Created with ❤️ using Flask</p>
            </footer>
        </div>
    </body>
    </html>
    """

@app.route('/student')
def get_student():
    # Return JSON data
    return jsonify({
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    })

if __name__ == '__main__':
    app.run(debug=True)
