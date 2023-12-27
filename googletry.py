from dotenv import load_dotenv
import google.generativeai as genai
import os,time

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

start = time.time()
resp = model.generate_content("What is the data threshold for you?")
end = time.time()

print("Time taken: ",end-start)
print(resp.text)