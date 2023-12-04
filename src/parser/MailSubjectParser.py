import email

def parse_mime_subject(mail: email.message.Message) -> str:
	'''Function to parse the subject line from MIME emails.

	Parameters
	----------
		mail: email.message.Message
			The MIME email.

	Returns
	-------
		String of the subject line.
	'''

	return mail["Subject"]