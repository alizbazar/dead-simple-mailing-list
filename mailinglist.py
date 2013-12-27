#
# Dead Simple Mailing List
#
# Copyright 2013 alizbazar
# MIT Licence
#
# Script for forwarding email to multiple addresses
# (essentially acting as a dead simple mailing list)
#
# Dec 27 15:16:34 EET 2013
#

import sys, email, smtplib

def forward_email(to_addresses, reply_to='', subject_id=''):

    try:
        raw_email = sys.stdin.read()

    except:
        raise SystemExit

    if not to_addresses:
        raise ValueError('to_addresses[] array missing')

    email_data = email.message_from_string(raw_email)

    if reply_to:
        email_data['Reply-to'] = reply_to


    if subject_id:
        subject = email_data['Subject']
        if subject.find(subject_id) == -1:
            subject = subject_id + ' ' + subject
            del email_data['Subject']
            email_data['Subject'] = subject
 
    try:
        smtp_conn = smtplib.SMTP()
        smtp_conn.connect()
        smtp_conn.sendmail(email_data['From'], to_addresses, email_data.as_string())
        smtp_conn.close()

    except:
        raise SystemExit