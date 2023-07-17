import sys
import requests

BASE_URL = 'http://localhost:8888'


def upload(file_path):
    url = f'{BASE_URL}/upload'
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        print('File uploaded successfully.')
    else:
        print('Failed to upload file.')


def list_files():
    url = f'{BASE_URL}/'
    response = requests.get(url)
    if response.status_code == 200:
        files = response.json()
        print('Files on the server:')
        for file in files:
            print(file)
    else:
        print('Failed to retrieve files.')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage:')
        print('python screwdriver.py upload /path/to/file.mp3')
        print('python screwdriver.py list')
        sys.exit(1)

    command = sys.argv[1]

    if command == 'upload':
        if len(sys.argv) < 3:
            print('Please provide the file path to upload.')
            sys.exit(1)
        file_path = sys.argv[2]
        upload(file_path)
    elif command == 'list':
        list_files()
    else:
        print('Invalid command.')
