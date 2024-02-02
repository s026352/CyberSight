from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "system",
      "content": [
        {"type": "text", "text": "You're a vision assistant, skilled in helping blind people in their grocery task through photos they took. You can help them understand where they are, what's in front of them and where is a certain product."},
      ],
    },
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Is there a Italian wedding soup in front of me? If yes, where is it?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://i.cbc.ca/1.6326969.1643135404!/fileImage/httpImage/empty-grocery-shelves-vancouver.jpg",
          },
        },
      ],
    }
  ],
)

for response in response.choices:
    print(response)