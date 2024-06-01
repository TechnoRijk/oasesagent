import requests
from transformers import pipeline

def generate_image(prompt):
    response = requests.post('https://api.crewai.com/generate', json={'prompt': prompt})
    return response.json()['image_url']

generator = pipeline('text-generation', model='gpt-3')

def generate_text(prompt):
    return generator(prompt, max_length=100)[0]['generated_text']
