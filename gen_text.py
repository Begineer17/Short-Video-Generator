import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import time

GOOGLE_API_KEY = "YOUR_GEMINI_API"
genai.configure(api_key=GOOGLE_API_KEY)

model_gemini = genai.GenerativeModel('gemini-1.5-flash')

def generate_prompt_from_hashtags(des: str="A lovely seasight of peace #peace #sea", instrument: str='piano', mood: str='happy'):
    prompt_vid = f"Generate a short, less than 20-word description for my video about natural environment has meaningful continuous loop using this video title and hashtags (ignore the hashtags that you don't understand, don't generate anything else than my desired description and the content must be approriate, straightforward, not be metaphoric, not contain harrasment, dangerous content, sexually explicit, hate speech according to Gemini safety rating): {des}"
    prompt_melody = f"Generate a short, less than 15-word description for the climax of my {mood} {instrument} melody example: 'A {mood} {instrument} melody', based on this video title and hashtags (ignore the hashtags that you don't understand, don't generate anything else than my desired description and the content must be approriate, straightforward, not be metaphoric, not contain harrasment, dangerous content, sexually explicit, hate speech according to Gemini safety rating): {des}"

    response_vid = model_gemini.generate_content(
        prompt_vid,
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH
        }
        )
    
    time.sleep(4)
    
    response_melody = model_gemini.generate_content(
        prompt_melody,
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH
        }
        )

    if response_vid.parts and response_melody.parts:
        # print('Prompt video:', response_vid.text)
        # print('Prompt melody:', response_melody.text)
        return response_vid.text, response_melody.text # Only print if there are parts in the response
    else:
        print("Model did not generate any text. Check safety ratings:")
        for candidate in response_vid.candidates:
            print(candidate.safety_ratings)
        for candidate in response_melody.candidates:
            print(candidate.safety_ratings)
        return None, None
    
# generate_prompt_from_hashtags()
    
# Source: https://ai.google.dev/gemini-api
