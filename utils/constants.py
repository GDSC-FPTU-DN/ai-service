import os

APP_DOMAIN = "http://localhost:8000"

TEMP_DIR = os.path.join(os.getcwd(), 'temp')

DOC_TEMPLATE = f'''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>GDSC AI Service</title>
  </head>
  <body>
    <img src="https://seeklogo.com/images/G/google-developers-logo-F8BF3155AC-seeklogo.com.png" alt="logo" width="100">
    <h1>GDSC AI Back-end Service</h1>
    <span>Served URL: </span>
    <a href="{APP_DOMAIN}">{APP_DOMAIN}</a>
    <ul>
      <li>Remove Background Service [POST]</li>
      <code>{APP_DOMAIN}/api/rembg</code>
    </ul>
    <ul>
      <li>Image to Text [POST]</li>
      <code>{APP_DOMAIN}/api/img2text</code>
    </ul>
    <ul>
      <li>Chats [POST]</li>
      <code>{APP_DOMAIN}/api/chats</code>
    </ul>
    <ul>
      <li>Face Detection [POST]</li>
      <code>{APP_DOMAIN}/api/fd</code>
    </ul>
  </body>
</html>
'''
