import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def mail_form_detaillant(submit_values, logo):
    if logo:
        msg = MIMEMultipart('related')
        msg['Subject'] = 'Nouveau détaillant'
        msg['From'] = "infos@ingredients.quebec"
        msg['To'] = "infos@ingredients.quebec"
        content = MIMEText("Nom: " + submit_values['name'] + "\n\r" + "Description: " + submit_values['description']
                           + "\n\r" + "URL: " + submit_values['URL'] + "\n\r" + "Code Postal: "
                           + submit_values['code_postal'])
        image_file = MIMEImage(logo.stream.read())
        msg.attach(content)
        msg.attach(image_file)
    else:
        msg = MIMEText("Nom: " + submit_values['name'] + "\n\r" + "Description: " + submit_values['description']
                       + "\n\r" + "URL: " + submit_values['URL'] + "\n\r" + "Code Postal: "
                       + submit_values['code_postal'])
        msg['Subject'] = 'Nouveau détaillant'
        msg['From'] = "infos@ingredients.quebec"
        msg['To'] = "infos@ingredients.quebec"

    # Send the message via our own SMTP server.
    smtp_connection = smtplib.SMTP('127.0.0.1')
    smtp_connection.send_message(msg)
    smtp_connection.quit()
