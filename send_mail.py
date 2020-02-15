import smtplib
from email.mime.text import MIMEText


def send_email(customer, dealer, rating, comments):
    """[summary]

    Arguments:
        customer {string} -- [description]
        dealer {string} -- [description]
        rating {string} -- [description]
        comments {string} -- [description]
    """
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'e1c8110fdc14f3'
    password = "51cbea0b9be8d7"
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'hung.quach@gmail.com'
    reciver_email = 'xenoki@me.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = reciver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, reciver_email, msg.as_string())
