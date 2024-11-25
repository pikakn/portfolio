import google.generativeai as genai

genai.configure(api_key='AIzaSyCmuQlhuS0Fl00jI7h8PJIM_An1tBv-09Y')

def ask_gemini(prompt):
    gemini_pro = genai.GenerativeModel("gemini-pro")
    response = gemini_pro.generate_content(prompt)
    return response.text

#print(ask_gemini('こんばんは'))