def build_prompt(user_question, faqs):
    context = "\n".join([f"Q: {row['Question']}\nA: {row['Answer']}" for _, row in faqs.iterrows()])
    return f"""
You are a helpful assistant for a car rental website.

Here are some FAQs:
{context}

Answer the following question as clearly and helpfully as possible:
Q: {user_question}
A:"""
