import requests
import json
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

HOST_URL = 'http://127.0.0.1:3000'
MODE = 'default'

def keyboard_controller():
    global MODE
    msg = 'Enter image name or enter `exit` to exit: '
    while(True):
        user_input = input(msg)
        if user_input.lower() == 'exit':
            return 'exit'
        else:
            if not user_input:
                msg = 'image name can not be empty!\n Enter new value: '
                continue
            else:
                MODE = 'find'
                return {'name': user_input}


def url_handler():
    if MODE == 'find':
        return HOST_URL + '/find'
    else:
        return HOST_URL


def image_preview(data):
    image = mpimg.imread( BytesIO(base64.b64decode(data)), format='PNG')

    plt.imshow(image, interpolation='nearest')
    plt.show()


def main():
    params = {}
    while(True):
        try:
            response = json.loads(requests.get(url_handler(), params=params).text)
            
            if not 'name' in params.keys():
                print(response['data'])
            else:
                if response['data']['is_exist'] == False:
                    print('%s not found!' % (params['name']))
                else:
                    print('%s is exist!' % (params['name']))
                    user_input = input('Do you want to see that ([y]/n)? ')
                    if user_input.lower() != 'n':
                        image_preview(response['data']['image_data'])
            
            controller_output = keyboard_controller()
            if controller_output == 'exit': 
                break
            params = controller_output

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        

if __name__ == '__main__':
    main()