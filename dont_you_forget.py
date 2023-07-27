try:
    import os
except:
    print('Could not import requirement: os')
try:
    import smtplib
except:
    print('Could not import requirement: smtplib')
try:
    import random
except:
    print('Could not import requirement: random')
try:
    from email import encoders
except:
    print('Could not import requirement: encoders')
try:
    from email.mime.base import MIMEBase
except:
    print('Could not import requirement: MIMEBase')
try:
    from email.mime.multipart import MIMEMultipart
except:
    print('Could not import requirement: MIMEMultipart')
try:
    from email.mime.text import MIMEText
except:
    print('Could not import requirement: MIMEText')

def __main__():
    #image settings
    _image_location = ''

    SendEmail(_image_location)

## end : [__main__]


def SendEmail(image_location):
    #smtp settings
    _host = "smtp.gmail.com"
    _port_tls = 587
    _ssl_port = 465
    _use_tls_ssl = True
    #email details
    _to_email = ''
    _bcc = ''
    _from_email = '' 
    _password = ''
    _subject = f"Don't You Forget About Me"
    _message_body = f"""Here is your daily reminder that I exist!

    - Love Eric"""
    _image_to_attach = GetImage(image_source=image_location)
    #message list
    _message = MIMEMultipart()
    _message["From"] = _from_email
    _message["To"] = _to_email
    _message["Bcc"] = _bcc
    _message["Subject"] = _subject
    _message.attach(MIMEText(_message_body, "plain"))

    try:
        with open(_image_to_attach, "rb") as _attachement:
            _mime_base = MIMEBase("application", "octet-stream")
            _mime_base.set_payload(_attachement.read())
        
        encoders.encode_base64(_mime_base)
        _mime_base.add_header("Content-Disposition", f"attachment; filename={_image_to_attach}")
        _message.attach(_mime_base)

    except Exception as _mime_base_error:
        print("There was an error in the mime-base")
        print(str(_mime_base_error))
    

    try:
        with smtplib.SMTP('smtp.gmail.com', _port_tls) as _email_server:
            print("try send message...")
            _email_server.ehlo()
            _email_server.starttls()
            _email_server.ehlo()
            _email_server.login(_from_email, _password)
            _email_server.send_message(msg=_message)
            print("complete.")

    except Exception as e:
        print(f"failure - message settings : {_host}, {_password}, {_port_tls}, {_ssl_port}, {_use_tls_ssl}")
        print("")
        print(f"message details -  {_to_email} {_from_email} : {_message_body}")
        print("")
        print(f"error details :{e}")

## end : [SendEmail]


def GetImage(image_source):
    _path_exists = CheckPath(image_source)
    _image_selected = ""

    if (_path_exists is True): 
        try:
            _image_list = os.listdir(image_source)
            _random_number = GetRandomNumber(_image_list.__len__())
            _image = _image_list[_random_number]

            try:
                _image_selected = os.path.join(image_source, _image)
            except:
                print("could not join image source and image name")
        except:
            print("could not list images in the path provided")

    else:
        print(f"the path {image_source} does not exist.") 

    return _image_selected

## end : [GetImages]


def GetRandomNumber(upper_bound):
    _random_number = 0

    if upper_bound > 0:
        try:
            _random_number = random.randint(0, upper_bound)
        except:
            _random_number = 0
    
    return _random_number
## end : [GetRandomNumber  ]



def CheckPath(path):
    _path_exists = False

    try:
        _path_exists = os.path.isdir(path)
    except:
        print(f"the path entered was not valid : {path}")
        # this error is going to be fatal and prevent the program from running further.
        exit()
    
    return _path_exists

## end : [CheckPath]




__main__()