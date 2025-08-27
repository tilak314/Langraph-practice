# import google.generativeai as genai

# API_KEY = "AIzaSyDXssKltyLl0AcyWxwSKrycDDYJ0nYpih4"  # Replace with your actual API key

# genai.configure(api_key=API_KEY)

# try:
#     models = genai.list_models()
#     print("Available models:")
#     for m in models:
#         print(m.name)
# except Exception as e:
#     print("Error listing models:", e)



import google.generativeai as genai

API_KEY = "AIzaSyDXssKltyLl0AcyWxwSKrycDDYJ0nYpih4"  # Replace with your actual API key

genai.configure(api_key=API_KEY)

try:
    model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
    response = model.generate_content("Hello, Gemini!")
    print("API key is working. Response:", response.text)
except Exception as e:
    print("API key is not working. Error:", e)