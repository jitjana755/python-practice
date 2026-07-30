from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key="supersecret"

@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "721625":
            session["user"] = username  # store in session
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials. Try again", mimetype="text/plain")

    return '''
       <h2>Login page</h2>

       <form method="POST">
       Username: <input type="text" name="username"><br>
       Password: <input type="password" name="password"><br>
       

       <input type="submit" value="Login">

       </form>
    '''


# welcome page(after login)
@app.route("/welcome")
def welcome():

    if "user" in session:
        return f'''
          <h2>Welcome, {session["user"]}</h2>
          <a href="{url_for('logout')}">Logout</a>
        '''

    return redirect(url_for("login"))


# logout route
@app.route("/logout")
def logout():

    session.pop("user", None)
    # session["user"]="sagar"

    return redirect(url_for("login"))


app.run(debug=True)
#project 1 
