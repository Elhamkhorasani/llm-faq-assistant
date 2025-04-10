import openai
import pandas as pd
from prompts import build_prompt

openai.api_key = "YOUR_OPENAI_KEY"  # Or load from env

def answer_question(question, faq_path="data/faq.csv"):
    faqs = pd.read_csv(faq_path)
    prompt = build_prompt(question, faqs)
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()
