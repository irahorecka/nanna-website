from flask import render_template, request, url_for, flash, redirect, request
from nannaElise import app, db, bcrypt
from nannaElise.forms import RegistrationForm, LoginForm
from nannaElise.models import User, Post
from flask_login import login_user, logout_user, current_user, login_required

posts = [
    {
        'author': '奈菜',
        'title': 'ビーガンて何？',
        'content': '英語圏のみならず、アルファベットを使用している国々において、なんらかの業務やデザインでダミー文を表示しておくときに使われる伝統的な文章があります。Lorem ipsumと呼ばれているその文は、現在では使われなくなった古いラテン語の文献をもとに、現代の英語と文字の出現頻度を合わせて生み出された無意味な文章です。',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': '田村慎一',
        'title': 'ビーガン大好き！',
        'content': 'コンテンツの内容ではなく、純粋にデザインを評価する場合にこれらの文章は役にたちます。人間は文章を読んでその意味を理解してしまうと、その他の部分への評価に影響を与えてしまうと言われていることがその理由です。',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': '相良',
        'title': '今日の気分',
        'content': 'では、日本語の場合はどうでしょう。前述のラテン文字とは違い、日本語の表記体系は非常に複雑です。ひらがな・カタカナ・漢字・数字・アルファベットを織り交ぜて記述されるため、Lorem ipsumでは全く代用できません。',
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


# FORMS
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your has been created! You may now log in.", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Login unsuccessful. Please check email and password", 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')