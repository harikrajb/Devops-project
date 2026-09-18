from flask import Flask
import socket
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <title>Azure DevOps Docker Project</title>
    </head>
    <body>
        <h1>Azure DevOps + Docker + Ansible</h1>
        <h2>Application is running successfully!</h2>

        <p><b>Hostname:</b> {socket.gethostname()}</p>
        <p><b>Server Time:</b> {datetime.datetime.now()}</p>

        <hr>

        <p>Platform: Azure</p>
        <p>Container Platform: Docker</p>
        <p>Configuration Management: Ansible</p>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)