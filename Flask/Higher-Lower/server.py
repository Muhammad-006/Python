from flask import Flask
import random

app = Flask(__name__)
winner = random.randint(0,9)
images = ["https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTFia3d6ZzBjN2I3YTRkaDUzMWJvaHB3aHV2cHBpOGNicWJ1ZW01ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PzrPi0UVzgYHm/giphy.gif",
          "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3dtemF6aWJueXpmYmdxeW0xOHk1am5qeWNmMW85cnVlbTZwbXhlbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZlujEYRgp0q3e/giphy.gif",
          "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExenRpN3NxbGJqM2g1N215b2NmYWRlbmVhdHo5cndmZ2dkMmE0eGVtNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UIpzEC5QTvuOQ/giphy.gif",
          "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzJwdmMzdXVtcHhjeDIyNjIxdGlqNGY3bTJ0eDJma3E4NDQ0dmp1aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gyRWkLSQVqlPi/giphy.gif",
          "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjZhaHFwNG5jOG1uYmd0dXRvc3QzZ2NveTF1ZTFvZHl0NG95bmM1dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Pgb4zlVQqnUB2/giphy.gif",
          "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDI3ZGR1cTNmenNwazJ0ZjF2YTBlZnV1dXEwZGgwYmdpZmxhNjZ2bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/AF3xMm5xbp8k0/giphy.gif",
          "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGlzc2xmOGZodnQ2aWRtbnlwcDlvZ2o4MnN1Z2dkeG94NGFnOHZsNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LMn7PRCVDcnvO/giphy.gif",
          "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeDJzOWc4YjdjNHpna3luZWdiejdrN2o3czBlZm13dDR2M2R4NHJpeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VxbvpfaTTo3le/giphy.gif",
          "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHN3djh4cTNwdHhnZGZ1eHk5djA2MTBwNGEwcXZyNnl5dThqOHRpaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT0BKCbFA2v8lEmTio/giphy.gif",
          "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHQ3dXhvZjFiNHhnbmJ0YjNtdmYzdXBqajc1aGNxOWh4Y3g0NHcwMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CkMnLcOgKOxfa/giphy.gif",
          "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDBqeXE4Z2dsN25ibnRnamNlN3Zxd3Q3dzNiYmJwcXp1bm9ncnowMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Nm8ZPAGOwZUQM/giphy.gif",
          "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3NheGlzM2NsYzFiNTFsYnNtcGQ2cnI1NzU3dGZiZ2VudjJyMDNmdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tKyqZtLzZxCLbKitIq/giphy.gif",
          "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHNneWZndm5jMWJqajBrd2Y0ajQ1aWFqOHBuZHg5ZnhraW15NjFuciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/X2A2d62PrrMCk/giphy.gif",]

@app.route('/')
def front_page():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width = 500>")

@app.route('/<int:value>')
def checking_function(value):
    if value == winner:
        return ("<h1 style = 'color: green'>You found me!</h1>"
            "<img src = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width = 500>")
    elif value < winner:
        return ("<h1 style = 'color: red'>Too low, try again!</h1>"
            f"<img src = '{random.choice(images)}' width = 500>")
    elif value > winner:
        return ("<h1 style = 'color: blue'>Too high, try again!</h1>"
            f"<img src = '{random.choice(images)}' width = 500>")


if __name__ == '__main__':
    app.run(debug=True)