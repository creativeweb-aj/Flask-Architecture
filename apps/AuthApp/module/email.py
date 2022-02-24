import datetime
from apps.AuthApp.models import EmailHandler
from settings.extension import db
from flask import render_template_string
import uuid
import smtplib
import os

API_BASE_URL = os.environ.get('API_BASE_URL', 'http://localhost:5000')


class EmailService:
    def saveEmail(self, user):
        subject = "Creative Web Verify Your Email"
        key = str(uuid.uuid4())
        url = API_BASE_URL + "/email/verify?id=" + key
        body = render_template_string("Hello, This is you verification link {{ link }}", link=url)
        dateTime = str(datetime.datetime.timestamp(datetime.datetime.now()))
        obj = EmailHandler(user_id=user.id, subject=subject, body=body, uuid=key,
                           created_on=dateTime, updated_on=dateTime)
        db.session.add(obj)
        db.session.commit()

        self.sendEmail(obj, user)

        return obj

    def sendEmail(self, data, user):
        subject = data.subject
        body = data.body
        email = user.email
        emailId = os.environ.get('MAIL_USERNAME')
        password = os.environ.get('MAIL_PASSWORD')
        message = """From: From Person <%s>
        To: To Person <%s>
        Subject: %s

        %s
        """ % (emailId, email, subject, body)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        s.starttls()
        # Authentication
        s.login(emailId, password)
        s.set_debuglevel(True)
        try:
            # sending the mail
            s.sendmail(emailId, [email], message)
        except smtplib.SMTPException:
            print(smtplib.SMTPException)
        # terminating the session
        s.quit()
        self.updateEmail(data)
        return data

    def updateEmail(self, data):
        id = data.id
        dateTime = str(datetime.datetime.timestamp(datetime.datetime.now()))
        emailObj = EmailHandler.query.filter_by(id=id, is_sent=False).first()
        emailObj.is_sent = True
        emailObj.sent_on = dateTime
        emailObj.updated_on = dateTime
        db.session.commit()
        return emailObj
