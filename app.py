from flask import Flask
import os
import time
import subprocess

# Create a Flask application instance
app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"  # Replace with your full name
    username = os.getenv('USER') or os.getenv('USERNAME') or 'unknown_user'
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    
    # Get top command output
    top_output = subprocess.getoutput('top -bn1')

    html = f"""
    <html>
        <body>
            <h1>System Information</h1>
            <p><b>Name:</b> {name}</p>
            <p><b>Username:</b> {username}</p>
            <p><b>Server Time (IST):</b> {server_time}</p>
            <h2>Top Output</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return html

# Start the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
