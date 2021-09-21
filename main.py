from flask import Flask, render_template
from post import Post


app = Flask(__name__)
post = Post()

@app.route('/')
def home():
    data = post.get_data()
    return render_template("index.html",posts=data)


@app.route('/post/<int:blog_id>')
def article(blog_id):
    data = post.return_dict(blog_id-1)
    return render_template('post.html',data = data)

if __name__ == "__main__":
    app.run(debug=True)
