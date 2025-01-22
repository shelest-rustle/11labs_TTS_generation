import pandas
import os

from dotenv import load_dotenv
from elevenlabs import ElevenLabs, Voice, save

from spain_digits import convert_numbers_to_words

load_dotenv()

eleven = ElevenLabs(api_key=os.environ.get('api_key'))
voice = Voice(voice_id=os.environ.get('voice_id'))  # id голоса

df = pandas.read_excel("название_файла_для_генерации.xlsx")  # xlsx файл, должны быть столбцы prompt_name и prompt_text

# 11labs нормализует числа только на английском языке,
# поэтому для испанского нужно их конвертировать в текст до синтеза
prompts_with_digits = ['example_prompt_with_digits1', 'example_prompt_with_digits2', 'example_prompt_with_digits3']


for _, row in df.iterrows():
    prompt_name = row['prompt_name']
    prompt_text = row['prompt_text']
    prompt_filename = prompt_name
    if prompt_name in prompts_with_digits:
        prompt_text = convert_numbers_to_words(prompt_text)  # конвертация чисел в числительные для синтеза на испанском

    try:
        print(f"Audio generate for {prompt_filename}...")
        audio = eleven.generate(
            text=prompt_text,
            voice=voice,  
        )
        save(audio, filename=f"{prompt_filename}.wav")
        print(f"File saved: {prompt_filename}")
    except Exception as e:
        print(f"Error during generate {prompt_filename}: {e}")
