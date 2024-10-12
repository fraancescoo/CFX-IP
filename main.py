import requests
import os

def main():
    try:
        print('''
  /$$$$$$  /$$$$$$$$ /$$   /$$      /$$$$$$ /$$$$$$$ 
 /$$__  $$| $$_____/| $$  / $$     |_  $$_/| $$__  $$
| $$  \\__/| $$      |  $$/ $$/       | $$  | $$  \\ $$
| $$      | $$$$$    \\  $$$$/ /$$$$$$| $$  | $$$$$$$/
| $$      | $$__/     >$$  $$|______/| $$  | $$____/ 
| $$    $$| $$       /$$/\\  $$       | $$  | $$      
|  $$$$$$/| $$      | $$  \\ $$      /$$$$$$| $$      
 \\______/ |__/      |__/  |__/     |______/|__/      
                                                     
                                                     
        https://github.com/Fraancescoo/CFX-IP

''')

        print('(https://cfx.re/join/xxxxxxxx or xxxxxxxx)')
        cfx_id = input('Enter the server id: ')
        print()

        if cfx_id == None or len(cfx_id) < 1:
            input('The server id entered is invalid.')
            os.system('cls')
            main()
            return

        url: str
        server_id: str

        if cfx_id.startswith('https://cfx.re/join/'):
            url = cfx_id
            server_id = cfx_id.split('/')[4]
        elif cfx_id.startswith('cfx.re/join/'):
            url = f'https://{cfx_id}'
            server_id = cfx_id.split('/')[2]
        else:
            server_id = cfx_id
            url = f'https://cfx.re/join/{server_id}'

        req = requests.get(url)
        headers = req.headers        
        keys = headers.keys()

        if 'x-citizenfx-join-token' in keys:
            print(f'Join Token: {headers.get("x-citizenfx-join-token")}')
        if 'x-citizenfx-url' in keys:
            citizenurl = headers.get('x-citizenfx-url')
            splitted = citizenurl.split('/')[2].split(':')
            print(f'URL: {citizenurl}\nIP: {splitted[0]}\nPort: {splitted[1]}')
        if 'last-modified' in keys:
            print(f'Last Modified: {headers.get("last-modified")}')

        content = req.content.decode()
        lines = content.splitlines()

        srvn = lines[145]
        print(f'Server Name: {srvn.split('"')[2][1:].replace('</h1>', '')}')

    except KeyboardInterrupt:
        exit(0)

if __name__ == '__main__':
    main()