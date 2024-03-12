import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL ="gpt-4-vision-preview"

client = OpenAI(api_key=openai_api_key)
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "이 이미지는 무슨 내용이니?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://flexible.img.hani.co.kr/flexible/normal/930/616/imgdb/resize/2019/1015/00501921_20191015.JPG",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])