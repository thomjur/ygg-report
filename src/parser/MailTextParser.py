from typing import Union
from bs4 import BeautifulSoup
import email

def guess_encoding(file_path):
    encodings = ['utf-8', 'iso-8859-1', 'windows-1252']  # Add more as needed
    for enc in encodings:
        try:
            with open(file_path, encoding=enc) as file:
                file.read()
                return enc
        except UnicodeDecodeError:
            continue
    return None

def parse_mime_tree(content: Union[email.message.Message, str]) -> str:
    '''Recursive function to parse messages from MIME type emails.
    
    The parser first tries to decode the message as UTF-8 and if this fails switches to "Windows-1525" encoding with replacement.
    Only considers Content-Type "text/*" payloads. Removes html tags from html style emails using BeautifulSoup.
    
    Parameters
    ----------
        mail: Union[email.message.Message, str]
            Parsed MIME mail with Python modul email
            
    Returns
    -------
        String of the email content.
    '''
    
    if type(content.get_payload()) == str and content.get("Content-Type") and content["Content-Type"].split(";")[0].strip().split("/")[0].strip() == "text":
        content = content.get_payload(decode=True)
        try:
            content = content.decode("UTF-8")
        except:
            try:
                content = content.decode("cp1252", errors="replace")
            except:
                content = content.decode("iso-8859-1", errors="replace")
                
        return BeautifulSoup(content, "html.parser").get_text() # removing html tags and noise
    
    if type(content.get_payload()) == list:
        for entry in content.get_payload():
            if entry["Content-Type"].split(";")[0].strip().split("/")[0].strip() == "text":
                return parse_mime_tree(entry)
            elif type(entry.get_payload()) == list:
                return parse_mime_tree(entry)
    