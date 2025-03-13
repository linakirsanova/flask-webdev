from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Web World!"

@app.route('/about')
def about():
    return """<p>My name is Angelina Filippova, I'm a London-based
      frontend developer with 8 years of experience in web-development.
      I'm a curious individual with a passion for technology and learning new things.</p>
      <br><p>I enjoy exploring the possibilities of AI and finding
      creative ways to use digital tools.</p>"""


@app.route('/favorite-songs')
def songs():
  html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Favorite Songs</title>
    </head>
    <body>
        <h2>My Favorite Songs</h2>
        <ul>
            <li><strong>Crazy</strong> by Gnarls Barkley</li>
            <li><strong>Rolling in the Deep</strong> by Adele</li>
            <li><strong>Take on Me</strong> by A-ha</li>
            <li><strong>505</strong> by Arctic Monkeys</li>
            <li><strong>Yeah Right</strong> by Joji</li>
            <li><strong>Often</strong> by The Weeknd</li>
        </ul>
    </body>
    </html>
    """
  return html

@app.route('/menu')
def menu():
  return """<p>Check out <a href="/about">my About page</a>!</p>
    <p>And a <a href="/favorite-songs"> list of my favorite songs</a>!</p>
  """