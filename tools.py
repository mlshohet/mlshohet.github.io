import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(override=True)

def record_user_details(email="(email not provided)", name="(name not provided)", phone="(phone not provided)", notes="(not provided)"):
    send_email(f"A user with name {name}, email {email}, phone {phone} chatted with me. These are the chat notes: {notes}")
    return "OK"

address = os.getenv("EMAIL_ADDRESS")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
MY_EMAIL = os.getenv("MY_EMAIL")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(body_text):
    try:
        message = MIMEMultipart()
        message["From"] = EMAIL_USER
        message["To"] = MY_EMAIL
        message["Subject"] = "From resume bot"

        message.attach(MIMEText(f"Your resume bot sent an email with this text:\n\n{body_text}", "plain"))
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USER, MY_EMAIL, message.as_string())

    except:
       return "OK"


record_user_details_json = {
    "name": "record_user_details",
    "description": "Use this tool if a user provided an email address or phone",
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
