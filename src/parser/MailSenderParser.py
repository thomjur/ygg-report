import email

def parse_mime_sender(mail: email.message.Message) -> str:
	'''Function to parse the sender line from MIME emails.

	Parameters
	----------
		mail: email.message.Message
			The MIME email.

	Returns
	-------
		String of the from: line.
	'''
	return mail["From"]