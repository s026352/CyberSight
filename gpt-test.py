import base64
import requests
import sqlite3


# OpenAI API Key
api_key = "YOUR_API_KEY"


# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def read_db():
    # Connect to database
    conn = sqlite3.connect('Couche_Tard_1_Aisle.db')
    c = conn.cursor()

    # Query database
    c.execute("SELECT * FROM Items;")
    rows = c.fetchall()

    # Close connection
    conn.close()

    return rows

# Path to your image
image_path = "image_2.png"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "You're a vision assistant, skilled in helping blind people in their grocery task through photos "
                  "they took. You can help them understand where they are, what's in front of them and where is a "
                  "certain product."
        },
        {
          "type": "text",
          "text": "The user is currently in a grocery store. The store's grocery aisles are labeled in a list of "
                  "sections of homogeneous products. For each section, the list denotes them in the format of (None, "
                  "product_name, x_coordinate_1, y_coordinate_1, z_coordinate_1, x_coordinate_2, y_coordinate_2, "
                  "z_coordinate_2), with y axis being the height and y_coordinate = 0 indicate ground level. The list "
                  "is provided to you by the user as a string."
        },
      ],
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": str(read_db())
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        },
        {
          "type": "text",
          "text": "I am at the location where I took this photo. Where should I go to find Dorito chips? Explain in "
                  "terms of left/right/forward/backward, not in numerical coordinate system."
        }
      ]
    }
  ],
  "max_tokens": 500
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())