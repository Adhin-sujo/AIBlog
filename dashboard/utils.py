import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

def generate_blog_content(title, tone, style):
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    prompt = f"Generate a blog post in html format only with the title '{title}', tone '{tone}', and style '{style}'."
    response = model.generate_content(prompt)
    text = f"inputs: title = {title}"
    return response.text
