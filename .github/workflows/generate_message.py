import sys
import os
import openai

# Retrieve API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("Missing OPENAI_API_KEY environment variable")

client = openai.OpenAI(api_key = openai_api_key)

    
# Read the diff
with open(sys.argv[1], 'r') as f:
    diff = f.read()
    
# Make a request to the ChatGPT API
response = client.chat.completions.create(
    model="gpt-4",  # or "gpt-3.5-turbo"
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Generate a commit message for the following changes:\n{diff}"}
    ]
)

# set commit message
commit_message = response.choices[0].message.content

# Write the commit/PR message to a file
with open("commit_message.txt", "w") as f:
    f.write(commit_message)
