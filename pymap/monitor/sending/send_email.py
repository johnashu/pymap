from smtplib import SMTPException, SMTPHeloError, SMTPAuthenticationError
from smtplib import SMTP_SSL as SMTP  # SSL connection
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pymap.includes.config import *

# <!--[if mso]>
# <style type="text/css">
# .tableClass {
# margin: 0px 0px 0px 24px !important;

# padding: 0px 0px 20px 0px !important;
# }
# </style>
# <![endif]-->


def send_email(subject: str, message: str) -> None:
    if not alert_envs.SEND_EMAIL:
        print("Email sending not turned on, no email sent!")
        return

    msg = MIMEMultipart("alternative")

    msg["From"] = alert_envs.EMAIL_FROM
    msg["To"] = alert_envs.EMAIL_TO
    msg["Subject"] = subject

    ServerConnect = False

    html_output = f"<html> <head></head><body>{message}</body></html>"

    # # text must be the first one
    # msg.attach(MIMEText(message, 'plain')) 
    # html must be the last one
    msg.attach(MIMEText(html_output, "html"))

    try:
        smtp_server = SMTP(alert_envs.EMAIL_SMTP, alert_envs.PORT)
        smtp_server.login(alert_envs.EMAIL_FROM, alert_envs.EMAIL_PASS)
        ServerConnect = True
    except SMTPHeloError as e:
        log.error(f"Server did not reply  ::  {e}")
    except SMTPAuthenticationError as e:
        log.error(f"Incorrect username/password combination ::  {e}")
    except SMTPException as e:
        log.error(f"Authentication failed ::  {e}")

    if ServerConnect:
        try:
            smtp_server.sendmail(
                alert_envs.EMAIL_FROM, alert_envs.EMAIL_TO, msg.as_string()
            )
            print(msg.as_string())
            print("Successfully sent email")
        except SMTPException as e:
            log.error(f"Unable to send email  ::  {e}")
        finally:
            smtp_server.close()
            print("Email server connection closed")


# send_email('VOLUME Resized', 'HELLO TEST')

from tabulate import tabulate
table = [["Sun",696000,1989100000],["Earth",6371,5973.6],
         ["<p style='color:red'>Moon</p>",1737,73.5], 
         ["Mars",3390,641.85]]
print(tabulate(table, tablefmt='unsafehtml'))