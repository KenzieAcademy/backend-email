#!/usr/bin/env python3
"""
A tiny email program to send spam to someone
"""

import os
import smtplib

EMAIL_ADDR = os.environ['EMAIL_ADDR']
EMAIL_PWD = os.environ['EMAIL_PWD']

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDR, EMAIL_PWD)

    # compose the email message
    subject = "Keep on Truckin"
    body = "Janell keep on Truckin that Truck"
    msg = f"Subject: {subject}\n\n{body}"

    # do actual send
    smtp.sendmail(EMAIL_ADDR, 'kenzie.academy@mailinator.com', msg)
