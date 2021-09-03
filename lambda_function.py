import os
import smtplib
import requests
from email.message import EmailMessage

def lambda_handler(event, context):
    CAT_API_URL = "https://api.thecatapi.com/v1/images/search"
    EMAIL_ADDRESS = "lslestercayabyab@gmail.com"
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

    # Get cat image url 
    try:
        cat_api_res = requests.get(url=CAT_API_URL)
        cat_image_url = cat_api_res.json()[0]['url']
    except Exception as e:
        print(f"Something went wrong caused by {e}.")

    # Send email
    try:
        msg = EmailMessage()
        msg['Subject'] = "Cat of the day!"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = "ekoraim@gmail.com"
        
        msg.set_content(f"Here is your cat!\n{cat_image_url}")
        msg.add_alternative(f'Here is your cat!<br/><br/><img src="{cat_image_url}" width="300px">', subtype="html")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print("Done sending email!")
    except Exception as e:
        print(f"Something went wrong caused by {e}.")

