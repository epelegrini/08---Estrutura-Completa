import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(subject, recipient, body):
    api_key = os.environ.get('SENDGRID_API_KEY')
    if not api_key:
        raise ValueError("SENDGRID_API_KEY not found in environment variables")
    sg = SendGridAPIClient(api_key)
    from_email = 'flaskaulas@zohomail.com' 
    message = Mail(
        from_email=from_email,
        to_emails=recipient,
        subject=subject,
        html_content=body)
    try:
        response = sg.send(message)
        print(f"Email sent to {recipient}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")
