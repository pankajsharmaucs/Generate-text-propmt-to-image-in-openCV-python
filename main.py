import os


import openai


PROMPT = "An eco-friendly computer from the 90s in the style of vaporwave"

response = openai.Image.create(

    prompt=PROMPT,

    n=1,

    size="256x256",

)


print(response["data"][0]["url"])
