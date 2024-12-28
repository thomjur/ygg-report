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
	# Check if X-Original-From exists
	if "X-Original-From" in mail:
		return mail["X-Original-From"]
	return mail["From"]