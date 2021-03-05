from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/team')
def team():
    return render_template('team.html')
@app.route('/blog')
def blog():
    return render_template('blog.html')
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=="__main__":
    app.run()
