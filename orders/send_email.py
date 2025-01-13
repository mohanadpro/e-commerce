import os
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import smtplib

email_sender = 'ebuy.13.1993@gmail.com'
email_password = 'vzhv fcaj tmfd qncl'
# email_receiver = 'may18615@gmail.com'
email_receiver = 'mohanad.13.93@gmail.com'

subject = "confirmation of your order"

body = """

<html>
  <head>
    <style>
        table, th, td{
            border: 1px solid black;
        }
        th,td{
            padding: 3px 6px;
        }
        table
        {
            border-collapse:collapse;        
        }
        td{
            text-align: center;
        }
        th{
            background-color:#f44804;
            color:white;
        }
</style>
  </head>
  <body style="font-size:15px">
    <p>Hello Dear!<br><br>
       Thanks for your order<br><br>
       Order number : 12314 <br><br>
       Total Price : 116$ <br><br>

       You can see Details in the below table
    </p>
    <table>
        <thead>
            <th> Item</th>
            <th> Number</th>
            <th> Price</th>
            <th> Total Price</th>
        </thead>
        <tbody>
            <tr> 
                <td> T-shirt </td>
                <td> 2 </td>
                <td> 13$</td>
                <td> 26 </td>
            </tr>
            <tr> 
                <td> Shoes </td>
                <td> 3 </td>
                <td> 30$</td>
                <td> 90 </td>
            </tr>
        </tbody>
    </table>
        <p>You will receive another email with the tracking number after we send your order<br><br>
       If you have another problem with the order<br><br>
       Please don't hesitate to contact us on the below email <br>
    
       </p> <br>
       <p>
       With special regards <br> 
       EBuy Customer Service <br>
       ebuy-customerservice@gmail.com
       </p>
  </body>
</html>
"""
part2 = MIMEText(body, 'html')

# em = EmailMessage()
em = MIMEMultipart('alternative')
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject

em.attach(part2)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())