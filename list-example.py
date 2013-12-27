#!/usr/bin/python
import mailinglist

# email_addresses = ['Foo Bar <foo@foobar.com>']
email_addresses = [
    'Foo Bar1 <foo1@foobar.com>',
    'Foo Bar2 <foo2@foobar.com>'
]

# Address of the mailing list
# email_replyto = 'Foo <list@foobar.me>'
email_replyto = 'Foo <list@foobar.me>'

# Identifier prepended to the subject line
# identifier = '[Foo]'
identifier = '[Foo]'

mailinglist.forward_email(email_addresses, email_replyto, identifier)
