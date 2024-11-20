import random
from django.core.mail import EmailMessage
from .models import User, OneTimePassword
from django.conf import settings


def generateOtp():
    otp = ''
    for i in range(6):
        otp += str(random.randint(0, 9))
    return

def second_code_to_user(email):
    Subject = "One time passcode for Email Verification"
    otp_code = generateOtp()
    
    user = User.objects.get(email=email)
    current_site = "myAuth.com"
    email_body = f'Hello {user.username}, your code is {otp_code}! \n Thanks for your verification on {current_site}!'
    from_email = settings.DEFAULT_FROM_EMAIL
    
    OneTimePassword.objects.create(user=user, code=otp_code)
    d_email = EmailMessage(subject=Subject, body=email_body, from_email=from_email, to=[email])
    d_email.send(fail_silently=True)
    
    
def send_normal_email(data):
    email = EmailMessage(
        subject=data['email_subject'],
        body=data['email_body'],
        from_email=settings.EMAIL_HOST_USER,
        to=[data['to_email']]
    )
    email.send()