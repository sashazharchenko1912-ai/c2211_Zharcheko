import requests
response = requests.get('https://www.google.com/?hl=uk')
print(response.text)