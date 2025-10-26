from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # Inline HTML, CSS, and JS for the homepage
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask API - Enhanced</title>
        <style>
            body {
                font-family: 'Poppins', Arial, sans-serif;
                background: linear-gradient(135deg, #1e90ff, #00c6ff);
                color: #333;
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .container {
                background: #fff;
                width: 90%;
                max-width: 800px;
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 6px 25px rgba(0,0,0,0.2);
                text-align: center;
                animation: fadeIn 1s ease-in-out;
            }
            h1 {
                color: #007bff;
                font-size: 2.2rem;
            }
            p {
                color: #444;
                font-size: 1.1rem;
                margin: 15px 0 30px;
            }
            .btn {
                display: inline-block;
                background: #007bff;
                color: white;
                padding: 12px 25px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: bold;
                transition: 0.3s;
            }
            .btn:hover {
                background: #0056b3;
                transform: scale(1.05);
            }
            footer {
                margin-top: 40px;
                font-size: 0.9rem;
                color: #777;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-20px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to My Enhanced Flask API 🚀</h1>
            <p>Experience a modern look with embedded CSS and live API data fetching.</p>
            <a href="/student-page" class="btn">View Student Info</a>
            <footer>Created with ❤️ using Flask & HTML</footer>
        </div>
    </body>
    </html>
    """

@app.route('/student-page')
def student_page():
    # A styled page that fetches JSON data using JavaScript
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Student Info</title>
        <style>
            body {
                font-family: 'Poppins', Arial, sans-serif;
                background: linear-gradient(135deg, #00c6ff, #1e90ff);
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                color: #333;
            }
            .card {
                background: #fff;
                padding: 40px;
                border-radius: 16px;
                width: 90%;
                max-width: 600px;
                box-shadow: 0 6px 25px rgba(0,0,0,0.2);
                text-align: center;
                animation: slideIn 0.8s ease-out;
            }
            h1 {
                color: #007bff;
                margin-bottom: 20px;
            }
            .info {
                font-size: 1.2rem;
                color: #555;
                text-align: left;
                margin-top: 20px;
            }
            .info p {
                background: #f8f9fa;
                padding: 12px 15px;
                border-radius: 8px;
                margin: 8px 0;
            }
            a {
                display: inline-block;
                margin-top: 25px;
                text-decoration: none;
                background: #007bff;
                color: white;
                padding: 10px 20px;
                border-radius: 8px;
                transition: 0.3s;
            }
            a:hover {
                background: #0056b3;
            }
            @keyframes slideIn {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Student Information 🎓</h1>
            <div id="student-info" class="info">
                <p>Loading student data...</p>
            </div>
            <a href="/" class="btn">← Back to Home</a>
        </div>

        <script>
            // Fetch student data from the API
            fetch('/student')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('student-info').innerHTML = `
                        <p><strong>Name:</strong> ${data.name}</p>
                        <p><strong>Grade:</strong> ${data.grade}</p>
                        <p><strong>Section:</strong> ${data.section}</p>
                    `;
                })
                .catch(err => {
                    document.getElementById('student-info').innerHTML = "<p style='color:red;'>Failed to load data.</p>";
                });
        </script>
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
