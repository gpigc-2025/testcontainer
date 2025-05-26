from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Team C Wooooo</title>
    <style>
    body {
    font-family: 'Papyrus', 'Comic Sans MS', cursive, sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
    background-color: #000000;
    color: #d40000;
  }
  
  .container {
    width: 90%;
    margin: auto;
    max-width: 1200px;
  }
  
  .navbar {
    background-color: #000000;
    padding: 1.5rem 0;
  }
  
  .navbar .logo {
    color: #000000;
    font-size: 1.5rem;
    font-weight: bold;
    float: left;
  }
  
  .nav-links {
    list-style: none;
    float: right;
    margin: 0;
    padding: 0;
  }
  
  .nav-links li {
    display: inline;
    margin-left: 20px;
    margin-top: 10px;
  }
  
  .nav-links a {
    color: #ffffff;
    text-decoration: none;
    font-size: 1rem;
  }
  
  .nav-links a:hover {
    text-decoration: underline;
  }
  
  .hero {
    text-align: center;
    padding: 2rem 0;
    background-color: #ffffff;
    color: #000000;
  }
  
  .hero h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }
  
  .hero p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
  }
  
  .cta-button {
    background-color: #cc0202;
    color: #fff;
    padding: 0.7rem 1.5rem;
    font-size: 1rem;
    border: none;
    border-radius: 5px;
    text-decoration: none;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .cta-button:hover {
    background-color: #ff4500;
  }
  
  .section {
    padding: 2rem 0;
    text-align: center;
    background-color: #ffffff;
  }
  
  .section:nth-child(even) {
    background-color: #000000;
  }
  
  .section h3 {
    font-size: 1.8rem;
    margin-bottom: 1rem;
  }
  
  .contact-form {
    max-width: 600px;
    margin: 1rem auto;
  }
  
  .contact-form input,
  .contact-form textarea {
    width: 100%;
    margin: 0.5rem 0;
    padding: 0.8rem;
    border: 1px solid #ff0000;
    border-radius: 5px;
    font-size: 1rem;
  }
  
  .contact-form button {
    background-color: #4caf50;
    color: #fff;
    padding: 0.8rem 1.5rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
  }
  
  .contact-form button:hover {
    background-color: #45a049;
  }
  
  footer {
    text-align: center;
    padding: 1rem 0;
    background-color: #333;
    color: #fff;
    font-size: 0.9rem;
  }
  

      .error-box {
        position: absolute;
        top: 10px;
        left: 50%;
        transform: translateX(-50%);
        width: 300px;
        height: 100px;
        background: rgba(255, 0, 0, 0.8);
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        z-index: 1000;
        border: 3px solid black;
        box-shadow: 0 0 10px black;
      }
    </style>
  </head>
  <body>
    <header class="navbar">
      <div class="container">
        <h1 class="logo">Team C Tester Website</h1>
        <nav>
          <ul class="nav-links">
            <li><a href="#about">About</a></li>
            <li><a href="#team">Our Team</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </nav>
      </div>
    </header>

    <div class="error-box">Uh oh SpaghettiOs, you can't see what's here now!</div>

    <main>
      <section class="hero">
        <h2>Welcome to Team C!</h2>
        <p>Your go-to squad for innovation, creativity, and knowledge (ICK).</p>
        <a href="#contact" class="cta-button">Get in Touch</a>
      </section>

      <section id="about" class="section">
        <h3>About Us</h3>
        <p>
          We are a group of problem-solvers who love taking on new challenges.
          Our mission is to deliver excellence in every project we undertake.
        </p>
      </section>

      <section id="team" class="section">
        <h3>Meet the Team</h3>
        <p>
          Our team is a mix of engineers, designers, and visionaries who work
          together to bring ideas to life.
        </p>
      </section>

      <section id="contact" class="section">
        <h3>Contact Us</h3>
        <p>Have a question or want to collaborate? Drop us a message below!</p>
        <form class="contact-form">
          <input type="text" placeholder="Your Name" required />
          <input type="email" placeholder="Your Email" required />
          <textarea placeholder="Your Message" required></textarea>
          <button type="submit">Send Message</button>
        </form>
      </section>
    </main>

    <footer>
      <p>2024 Team C. No rights reserved.</p>
    </footer>
  </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        os._exit(1)  # This forcefully kills the process (crashes container)
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
