import pandas as pd
import numpy as np
import math
import anthropic
import os

df = pd.read_csv('CoQAR_data.csv')

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="<API_KEY>",
)
generated_responses = []


for index, row in df.iterrows():
    query_text = row['query']
    
     
    prompt = '''TASK: Answer the QUESTION based on the context below. Keep the answer short and concise.
    CONTEXT: '''+query_text + '''
    QUESTION: '''+row['question'] +'''
    ANSWER: Think step by step from the paragraph.
    '''
    
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
      
    generated_responses.append(message.content)

df['claude_ans'] = generated_responses

csv='COT_claude_ans.csv' # keep your desired name
df.to_csv(csv)

