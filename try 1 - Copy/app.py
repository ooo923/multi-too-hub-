from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Required for flash messages

# ✅ Working Gmail SMTP setup with App Password
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jasbantkumar010@gmail.com'
app.config['MAIL_PASSWORD'] = 'pvrpfxqtrmpxjaic'
app.config['MAIL_DEFAULT_SENDER'] = 'jasbantkumar010@gmail.com'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('interface.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send', methods=['POST'])
def send():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message(
        subject='New Contact Form Submission',
        sender=email,
        recipients=['jasbantkumar010@gmail.com'],
        body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    )
    try:
        mail.send(msg)
        flash('✅ ईमेल भेजा गया!', 'success')
    except Exception as e:
        print(e)
        flash('❌ ईमेल भेजने में समस्या हुई।', 'error')

    return redirect('/contact')

if __name__ == '__main__':
    app.run(debug=True)
