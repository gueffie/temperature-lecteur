import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "stephane.gueffie@gmail.com"
    password = "tdxz qbfs enuf rvdq"

    receiver = "stephane.gueffie@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)



if __name__ == "__main__":
    message = "Bonjour"
    send_email(message)