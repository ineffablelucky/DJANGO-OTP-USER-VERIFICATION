# DJANGO-OTP-USER-VERIFICATION
Django twilio user verification


in settings.py , edit these

INSTALLED_APPS = [
    
    'django_otp',
    'otp_twilio',
    'OtpApp',
]


OTP_TWILIO_ACCOUNT = 'Axxxxxxxxxxxxxxxxxxxxxxxxxx'
OTP_TWILIO_AUTH = '0xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
OTP_TWILIO_FROM = '+1xxxxxxxxx '
OTP_TWILIO_NO_DELIVERY = False
OTP_TWILIO_TOKEN_VALIDITY = 18000
OTP_TWILIO_CHALLENGE_MESSAGE = 'Sent by SMS: {token}'
OTP_TWILIO_TOKEN_TEMPLATE = 'Sent from Django OTP Test App. Token is {token}'
