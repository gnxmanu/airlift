import smtplib, ssl, os, re, getpass

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import formataddr
from email.utils import formatdate
from email import encoders

# Extract user info
path = "/Users/USERNAME/Folder_Containing_Payload_Files"

list1 = os.listdir(path)

all_excels = [i for i in list1 if i.endswith('.xls')]
all_emails = [os.path.splitext(x)[0] for x in all_excels]

def extractMailNames():
    nodomains = [line.split("@") for line in all_excels]
    x = [nodomain[0] for nodomain in nodomains]
    global all_users
    all_users = x
extractMailNames()

# Mail details
sender_email = "NAME@DOMAIN.com"
sender_name = "YOUR INSTITUTIONAL NAME"

print("E-Mails will be sent to {}.".format(all_emails))
print("from".format(sender_email))

password = getpass.getpass(prompt='Type your password: ', stream=None)
receiver_emails = all_emails
receiver_names = all_users
receiver_files = all_excels

for receiver_email, receiver_name, receiver_file in zip(receiver_emails, receiver_names, receiver_files):

    message = MIMEMultipart("mixed")
    message['To'] = formataddr((receiver_name, receiver_email))
    message['From'] = formataddr((sender_name, sender_email))
    message['Subject'] = 'INSERT HERE THE SUBJECT OF YOUR E-MAIL'

    file = receiver_file

    text = """\
        Dear X,\n

        This is the first line\n

        This is the second line\n

        Sincerely yours,\n

        Me\n

        \n
        This is signature"""

    # Insert body text and signature in HTML, below a Minimal Working Example
    html ="""\
    <html>
      <body>
        <p>
        Dear X,<br><br>

        This is the first line<br><br>

        This is the second line<br><br>

        Sincerely yours,<br><br>

        Me

        </p>
        <p><br>
        Signature
        </p>
      </body>
    </html>
    """

    # part1 = MIMEText(text, "plain") # Plain Text disabled by default
    part2 = MIMEText(html, "html")

    # message.attach(part1) # Plain Text disabled by default
    message.attach(part2)

    # # Add xls attachment
    part3 = MIMEBase('application', "octet-stream")
    part3.set_payload(open("/Users/USERNAME/Folder_Containing_Payload_Files/"+receiver_file, "rb").read())

    # Encode file in ASCII characters
    encoders.encode_base64(part3)
    part3.add_header('Content-Disposition', 'attachment', filename=receiver_file)
    message.attach(part3)

    try:
        # Create a SMTP session and encrypting
        server = smtplib.SMTP_SSL("smtp.yourorganisation.com", 465)

        # Log in
        server.login("yourloginid", password)

        # Send email
        server.sendmail(sender_email, receiver_email, message.as_string())

        print("Email sent to {}.".format(receiver_email))

    except Exception as e:
        print("Something went wrong! {}.".format(e))

print("All emails sent.")
server.quit()
print("Connection closed.")
