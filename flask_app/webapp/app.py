from flask import Flask,request,render_template
from flask_mail import Mail,Message
import pandas as pd

app = Flask(__name__)
mail = Mail(app)

# configuration of mail 
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465

app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app) 

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/table',methods=['POST'])
def table():
    file = request.files['file']
    data = pd.read_excel(file)
    specific_column = data['email'].tolist()
    sender_mail = request.form.get('email')
    sender_pass = request.form.get('password')

    app.config['MAIL_USERNAME'] = sender_mail
    app.config['MAIL_PASSWORD'] = sender_pass

    mail.init_app(app)

    body = request.form.get('mail_body')
    subject = request.form.get('subject')
 
    msg = Message(
        subject=subject,
        sender=sender_mail,
        recipients=specific_column
                )
    msg.body = body
    mail.send(msg)
    return render_template('table.html',tables=specific_column,titles='')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')


# nljsjpoabmoupxqn

