
from PIL import Image 
from pytesseract import pytesseract 
from pdf2image import convert_from_path
from openai import AzureOpenAI
import tiktoken

# Defining paths to tesseract.exe 
# and the image we would be using 
path_to_tesseract = r"files\\tesseract\\tesseract.exe"
images = convert_from_path(
	"docs\\21-2432-2022-12-29.pdf", poppler_path=r"files\\poppler\\poppler-24.02.0\\Library\\bin")
client = AzureOpenAI(
    api_key = "c1577a69d9524294b2e46c84353c9929",
    api_version =  "2023-10-01-preview",
    azure_endpoint = "https://ai-proxy.lab.epam.com"
  )
deployment_name = "gpt-4-1106-preview"
finalText = ''
encoding = tiktoken.encoding_for_model("gpt-4")
  # Please only use this one if you absolutely need it. It's slower and more expensive.
  # deployment_name = "gpt-4"
  # deployment_name = "gpt-4-32k"
 
  # For embeddings only, but small private models may perform better and cheaper
  # https://huggingface.co/spaces/mteb/leaderboard
  # deployment_name = "text-embedding-ada-002"

def callDialAPI(promptText):
  print(client.chat.completions.create(
      model=deployment_name,
      temperature=0,
      messages=[
          {
          "role": "user",
          "content": "extract details like Full Matter Name , Parties Involved, current state of matter,lead company person, sustantive law, leads firm, matter_id, lead outside counsel, matter type, matter description,law firm/vendor, days pending in json format, return null if value not present in "
                  +  promptText
                          },
      ],
  ))

for i in range(len(images)):
	# Save pages as images in the pdf
    images[i].save(f'docs\\extract-text\\image_{i+1}.png', 'PNG')
    image_path = f'docs\\extract-text\\image_{i+1}.png'
    # Opening the image & storing it in an image object 
    img = Image.open(image_path) 
  
    # Providing the tesseract executable 
    # location to pytesseract library 
    pytesseract.tesseract_cmd = path_to_tesseract 
    
    # Passing the image object to image_to_string() function 
    # This function will extract the text from the image 
    text = pytesseract.image_to_string(img) 
    extractText = text[:-1]
    # Displaying the extracted text 
    finalText = finalText+extractText+' '
    token_count = len(encoding.encode(finalText))
    #print(token_count)
    #print(token_count>32700)


callDialAPI(finalText)