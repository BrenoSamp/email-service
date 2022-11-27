import smtplib
import email.message


def sendMail(nome, setor, destinatario):
    corpo_email = f"""
    <p>Ola {nome}</p>
    <p>Chegou um novo ticket para o setor {setor}</p>
    """
    msg = email.message.Message()
    msg['Subject'] = "Novo ticket para o setor " + setor
    msg['From'] = "bymdeskmail@gmail.com"
    msg['To'] = destinatario
    password = "lbzyllhaiglciawo"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')