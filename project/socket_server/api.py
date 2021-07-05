import requests
import json
import io
from PIL import Image

# put your name of image
data = {"name":"2.jpg"}
data_json = json.dumps(data)
url = 'http://127.0.0.1:2000'
# sending a request with name of image to the server
out_request = requests.get(url=url,data=data_json)

# if there was your image type of 'content-type' will be image
if out_request.headers['Content-Type']=='image/jpeg':

    print("there is this image")
    img_byte = out_request.content
    image = Image.open(io.BytesIO(img_byte))
    image.save('./out.jpg')

else:
    print(out_request.content.decode())