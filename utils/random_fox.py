# https://randomfox.ca/floof/
import requests

#
def fox():
    url = 'https://randomfox.ca/floof/'
    response = requests.get(url)

    if response.status_code:
        data = response.json()
        image = data.get('image')
        #print(data)
        return image

#
if __name__ == '__main__':
    print(fox())

#print(response)






