import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "helix.mcpd@gmail.com"
EMAIL_PASSWORD = "#helix2020axx!"


def send_emails(recipient_address):
    msg = EmailMessage()
    msg["Subject"] = "Rasa sending emails"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recipient_address
    msg.set_content('''
Hi all,

This is just a show case.

Best,''')

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            smtp.send_message(msg)
        print("Successfully sent email")
    except smtplib.SMTPException as e:
        print("{}: {}".format(e.errno, e.strerror))
    except smtplib.SMTPSenderRefused:
        print("Sender address refused.")
    except smtplib.SMTPDataError:
        print("SMTP server refused to accept the message data.")
    except smtplib.SMTPConnectError:
        print("Error occurred during establishment of a connection with the server.")
    except smtplib.SMTPAuthenticationError:
        print("SMTP authentication went wrong.")


if __name__ == "__main__":
    send_emails("jin.he@axxessio.com")