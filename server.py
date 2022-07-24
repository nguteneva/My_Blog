from flask import Flask
from flask import render_template

import smtplib
import requests
from flask import request


my_email = "nat_666@list.ru"
password = 'tGtG5Hw3TsWyNHLdNWdw'
link = "https://api.npoint.io/5a53af3908a610cb9f70"
app = Flask(__name__)
data = requests.get(link).json()

@app.route("/")
def blog():
    return render_template("index.html", text = data)

@app.route("/post")
def post():
    return render_template("post.html", text = data)

@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/", methods=['GET', 'POST'])
def form_entry():
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        with smtplib.SMTP("smtp.mail.ru") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs='nguteneva@gmail.com',
                                msg=f"Subject:You have a new message from the blog\n\nName: {name}\nemail: {email}\nPhone:{phone}\nMessage:{message}")
        return render_template('form-entry.html')
    else:
        return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)