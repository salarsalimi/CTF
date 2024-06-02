from flask import Flask, render_template, request
from subprocess import getoutput

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    command = request.args.get("command")
    if not command:
        return render_template("index.html")
    
    arg = request.args.get("arg")
    if not arg:
        arg = ""

    if command == "list_processes":
        return getoutput("ps")
    elif command == "list_connections":
        return getoutput("netstat -tulpn")
    elif command == "list_storage":
        return getoutput("df -h")
    elif command == "destroy_humans":
        return getoutput("/www/destroy_humans.sh " + arg)
    
    return render_template("index.html")