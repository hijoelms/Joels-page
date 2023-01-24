from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from flask_gravatar import Gravatar
import os
from notification_manager import NotificationManager

TWILIO_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_VIRTUAL_NUMBER = os.environ['TWILIO_VIRTUAL_NUMBER']
TWILIO_VERIFIED_NUMBER = os.environ['TWILIO_VERIFIED_NUMBER']


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
ckeditor = CKEditor(app)
Bootstrap(app)
gravatar = Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False, base_url=None)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/contact' , methods=["GET", "POST"])
def contact():
    print(request.method)
    if request.method == 'POST':

        data = request.form
        # send_email(data["name"], data["email"], data["phone"], data["message"])
        #
        print(data['name'], data['email'])
        user_name=data['name']
        user_email=data['email']
        user_ph_no = data['phone']
        user_msg = data['message']
        notification_manager = NotificationManager(TWILIO_SID, TWILIO_AUTH_TOKEN)
        notification_manager.send_sms(virtual_number=TWILIO_VIRTUAL_NUMBER , verified_number=TWILIO_VERIFIED_NUMBER,
            message=f"Message for you user_name:{user_name} user_email:{user_email} user_ph_no:{user_ph_no} user_msg: {user_msg}."
        )
        return render_template("contact.html", contact_rsp="Successfully sent your message", msg_sent=True)
    return render_template("contact.html", contact_rsp="Have questions? I have answers.", msg_sent =False)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
