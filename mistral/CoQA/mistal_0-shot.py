import pandas as pd
import numpy as np
import math

import os
from transformers import AutoModelForCausalLM, AutoTokenizer

df = pd.read_csv('CoQAR_data.csv')

model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)

generated_responses = []

for index, row in df.iterrows():
    query_text = row['query']
    
    prompt = query_text
    inputs = tokenizer(prompt, return_tensors="pt")

    response = model.generate(**inputs, max_new_tokens=20)

    text_content=tokenizer.decode(response[0], skip_special_tokens=True)
    generated_responses.append(text_content)

df['mist_ans'] = generated_responses

csv='0-shot_mistral_ans.csv' # keep your desired name
df.to_csv(csv)
