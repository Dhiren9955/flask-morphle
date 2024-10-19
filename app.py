from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Dhiren Chethan Raj"  
    username = os.getenv('USER') or os.getenv('USERNAME') or 'unknown_user'
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
