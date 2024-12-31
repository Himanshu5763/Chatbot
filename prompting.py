import google.generativeai as genai
import google.generativeai as genai

genai.configure(api_key="AIzaSyB0n2WqKYOtxqgF6DGn0NcG7YoW0acbmCw")

model = genai.GenerativeModel(model_name='gemini-pro')

chat = model.start_chat()

print("Type start and stop for chat control")
user_input = input("You:")
if user_input.lower() =="start":
    user_input = "Hello"
    while True:
        if user_input.lower() =="stop":
            print("Bot: Thank you")
            break
        response = chat.send_message(user_input)
        print("Bot: ",response.text)
        user_input = input("You: ")