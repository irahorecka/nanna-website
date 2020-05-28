from flask import render_template, request, url_for, flash, redirect
from nannaElise import app
from nannaElise.forms import RegistrationForm, LoginForm
from nannaElise.models import Post

posts = [
    {
        'author': 'Nanna Elise',
        'title': 'Blog Post 1',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus euismod ligula ante, eu convallis arcu ullamcorper id. Nulla facilisi. Morbi egestas metus vel ex ultricies interdum. Pellentesque ultricies, leo in eleifend pretium, ex augue eleifend magna, placerat sodales metus lectus ut turpis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nunc rutrum vulputate risus a dictum. Nulla venenatis pretium elit, quis volutpat lacus iaculis non. Pellentesque felis magna, elementum in semper vel, placerat ac lorem. In eleifend elit vel eleifend semper. Aliquam eget pellentesque sapien.',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Mauris et nunc elit. Curabitur consequat ante quis finibus tempus. Vestibulum cursus urna sed enim tristique, sit amet facilisis risus dictum. Quisque ac ligula mattis, imperdiet dolor sed, condimentum sem. Duis eget urna non orci ultrices aliquam eget sit amet ante. Pellentesque maximus tincidunt scelerisque. Duis vehicula velit nisl, vel sodales est congue eget. In hendrerit lacus vel ex dictum, non dignissim mi scelerisque. Nam volutpat, magna non pellentesque fermentum, ex ipsum fringilla dui, quis ultricies neque mi pretium sem. Donec finibus a neque sit amet luctus. Aenean mattis, lorem sed cursus bibendum, turpis leo ultrices nulla, in egestas ante sem a velit. Quisque volutpat dui leo, vitae vulputate nibh tincidunt id.',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'Ira Horecka',
        'title': 'Blog Post 3',
        'content': 'Phasellus ut iaculis orci, sed dictum nibh. Vivamus accumsan libero sit amet mauris commodo volutpat. Nullam feugiat ligula eget ligula auctor feugiat. Vestibulum in nisi consectetur, facilisis odio vitae, mollis tortor. Proin facilisis felis at tortor dapibus convallis. Aliquam erat volutpat. Nam at gravida nisi. Nulla facilisi. Donec sed lacus purus. Aliquam lacinia ligula ut hendrerit facilisis.',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
def main():
    """Redirect base url to home"""
    return redirect(url_for('home'))


@app.route("/home")
def home():
    title = "Home"
    return render_template("home.html", title=title)


@app.route("/videos")
def videos():
    title = "Videos"
    return render_template("videos.html", title=title)


@app.route("/recipes")
def recipes():
    title = "Recipes"
    return render_template("recipes.html", title=title)


@app.route("/blog")
def blog():
    title = "Blog"
    return render_template("blog.html", title=title, posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You have been logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful. Please check username and password", 'danger')
    return render_template('login.html', title='Login', form=form)
