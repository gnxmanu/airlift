# airlift
E-mail distribution automation with specific individual payload.

## Description
Takes all email-labeled files (e.g., 'anderson@metacortex.com.xlsx') from a folder and sends an email with the corresponding file to each individual. For Python 3.7.5.

### Dependencies
* Modules: `smtplib`, `ssl`, `os`,`re` `getpass`.
* Packages: `email.mime.text`, `email.mime.multipart`, `email.utils`, `email`.
* Specific objects: `MIMEText`, `MIMEMultipart`, `MIMEBase`, `formataddr`, `formatdate`, `encoders`.
* Attachement files (e.g., excel files '.xlsx') with the user mail as filename.

### Installing (terminal)
Clone repo from git.
``` console 
git clone github.com/gnxmanu/airlift.git
```

### Executing Program
User-specific variables need to be determined prior to execution (see **Arguments**). Afterwards run after cd into the .py location.
``` console 
python airlift.py
```
  
## Arguments
Change the folder path in 
``` python
# Extract user info
    path = "/Users/USERNAME/Folder_Containing_Payload_Files"
```
for that where the files are located.

Comment the following lines to not discriminate file types, if desired. Alternatively, determine the file type and corresponding extension. It defaults to excel files (.xls), but any file extension is supported.
``` python
# Subset only xls files
    all_excels = [i for i in list1 if i.endswith('.xls')]
    print(all_excels)
```

Edit only the following email information.
``` python
# Mail details
    sender_email = "NAME@DOMAIN.com"
    sender_name = "YOUR INSTITUTIONAL NAME"
```

``` python
# Mail subject
    message['Subject'] = 'INSERT HERE THE SUBJECT OF YOUR E-MAIL'
```

Write your e-mail body text in between the following lines for plain text (default is off) and HTML.
``` python
  text = """\
        Dear X,\n

        This is the first line\n

        This is the second line\n

        Sincerely yours,\n

        Me\n

    –\n
    This is signature
  """
```

``` python
  html = """\
    <html>
      <body>
        <p>
        Dear X,<br><br>

        This is the first line<br><br>

        This is the second line<br><br>

        Sincerely yours,<br><br>

        Me

        </p>
        <p>–<br>
        This is signature
        </p>
      </body>
    </html>
  """
```

Confirm the aforementioned folder path.
``` python
part3.set_payload(open("/Users/USERNAME/Folder_Containing_Payload_Files/"+receiver_file, "rb").read())
```

Add SMTP server address and port.
``` python
server = smtplib.SMTP("smtp.yourorganisation.com", 587) 
```

Input the email login ID at your organisation without the '@domain.com' part. **Do not code passwords**.
``` python
server.login("yourloginid", password)
```

## Authors
**Manuel V.**
<!-- **Manuel Velázquez** -->

[@gnxmanu](https://github.com/gnxmanu)

## Version History
* v1.0 –––––– Public Release. March 25, 2022

## License
This project is licensed under the [MIT] License - see the LICENSE.md file for details.
