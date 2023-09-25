import smtplib
import requests
from password_file import passwords,api_key
import time





def send_email(password):
    server = smtplib.SMTP('smtp.gmail.com', 576)
    server.ehlo()
    server.starttls()
    server.login('rahulverma9449@gmail.com', password)
    subject = 'prices is done'
    body = 'price done'
    msg = f'subject: {subject} {body}'

    server.sendmail(
        'rahulverma9449@gmail.com',
        'rahulverma9449@gmail.com',
        msg
    )
    print('email is sent')
    server.quit()

def check_stock(api_key,password):
    prices = requests.get('https://financialmodelingprep.com/api/v3/quote/AAPL?apikey={api_key}').json()

    stock_price = prices[0]['price']
    print(stock_price)

if stock_price < 140:
    # send an email
    send_email(password)

    # run every 10 second
while(True):
    check_stock(api_key,password)
    time.sleep(600)