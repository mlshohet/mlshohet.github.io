import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

mail_sandbox = os.getenv("MAILGUN_SANDBOX")
mail_url = f"https://api.mailgun.net/v3/{mail_sandbox}/messages"

from_address = f"Your chatbot <postmaster@{mail_sandbox}>"
to_address = f"Mike <{os.getenv("MY_EMAIL")}>"

def record_user_details(email="(not provided)", name="(not provided)", phone="(not provided)", notes="(not provided)"):
    send_email(f"{name} with email {email} and phone {phone} chatted with me.\nThese are the chat notes: {notes}")
    return "OK"

import os
import requests
def send_simple_message():
  	return requests.post(
  		"https://api.mailgun.net/v3/sandboxd4e840b36a3a4f82a03c809d315b06a9.mailgun.org/messages",
  		auth=("api", os.getenv("MAILGUN_API_KEY")),
  		data={"from": "Your chatbox <postmaster@sandboxd4e840b36a3a4f82a03c809d315b06a9.mailgun.org>",
			"to": "Mike <mlshohet@gmail.com>",
  			"subject": "Hello Spinning Sardines",
  			"text": "Congratulations Spinning Sardines, you just sent an email with Mailgun! You are truly awesome!"})

def send_email(body_text):
    mail_data = {
        "from": from_address,
        "to": to_address,
        "subject": "Message from your chatbot",
        "text": body_text
        
    }
    
    mail_data_json = json.dumps(mail_data)
	try:
		return requests.post("https://api.mailgun.net/v3/sandboxd4e840b36a3a4f82a03c809d315b06a9.mailgun.org/messages",
							 auth=("api", os.getenv("MAILGUN_API_KEY")),
							 data={"from": "Your chatbox <postmaster@sandboxd4e840b36a3a4f82a03c809d315b06a9.mailgun.org>",
								   "to": "Mike <mlshohet@gmail.com>",
								   "subject": "Hello Spinning Sardines",
								   "text": "Congratulations Spinning Sardines, you just sent an email with Mailgun! You are truly awesome!"})
	except Exception as exc:
		print(f"Email delivery failed: {exc!r}", flush=True)
		return {"success": False, "error": str(exc)}
		
record_user_details_json = {
    "name": "record_user_details",
    "description": "Use this tool if the user provided an email address or phone",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {
                "type": "string", "description": "The email address of this user"
                },
            "name": {
                "type": "string", "description": "The user's name, if they provided it"
                },
            "phone": {
                "type": "string", "description": "The user's phone, if they provided it"
                },
            "notes": {
                "type": "string",
                "description": "Any additional info about the conversation that's worth recording to give context",
            },
        },
        "required": ["email"],
        "additionalProperties": False,
    },
}

tools = [
    {"type": "function", "function": record_user_details_json},
]

tool_map = {
    "record_user_details": record_user_details,
}


def handle_tool_calls(tool_calls):
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        tool = tool_map.get(tool_name)
        result = tool(**arguments) if tool else "Unknown tool: " + tool_name
        results.append(
            {"role": "tool", "content": json.dumps(result), "tool_call_id": tool_call.id}
        )
    return results
