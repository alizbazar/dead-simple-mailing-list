Dead Simple Mailing List
==================================

Script for forwarding email to multiple addresses, essentially acting as a dead simple mailing list

## Function

Emails piped to the mailing list script get forwarded to specified email addresses.

Reply-To header is added to make sure further communication goes through the mailing list.

Additinal identifier (i.e. \[List Foo\]) can be added to the subject line. If email already has it, perhaps due to the previous reply, it's not added again.

## Usage

Create a file for your mailing list by modifying `list-example.py` and pipe specific emails to the script  
_(For example in CPanel this is possible with plain email forwarding)_