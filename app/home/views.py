from flask import render_template, request
from flask_login import login_required
from ..models import Pitch, Category

from . import home


@home.route('/')
def index():
    """
    Render the homepage template on the / route
    """

    rows = Pitch.get_pitches()

    id = []
    name = []
    upvotes = []
    downvotes = []
    created_at = []

    for row in rows:
        id.append(row.id)
        name.append(row.name)
        upvotes.append(row.upvotes)
        downvotes.append(row.downvotes)
        created_at.append(row.created_at)

    mylist = zip(id, name, upvotes, downvotes, created_at)

    return render_template('home/index.html', title="Welcome", mypitches=mylist)


@home.route('/profile/<int:id>')
@login_required
def profile(id):
    """
    Render the dashboard template on the /profile route
    """

    rows = Pitch.get_my_pitches(id)
    print(rows)

    id = []
    name = []
    upvotes = []
    downvotes = []
    created_at = []

    for row in rows:
        id.append(row.id)
        name.append(row.name)
        upvotes.append(row.upvotes)
        downvotes.append(row.downvotes)
        created_at.append(row.created_at)

    mylist = zip(id, name, upvotes, downvotes, created_at)

    return render_template('home/profile.html', title="Profile", mypitches=mylist)


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")


@home.route("/add/category", methods=['GET', 'POST'])
@login_required
def add_category_form():
    rows = Category.get_categories()

    id = []
    name = []
    created_at = []

    for row in rows:
        id.append(row.id)
        name.append(row.name)
        created_at.append(row.created_at)

    mylist = zip(id, name, created_at)

    if request.method == 'POST':
        name = request.form.get('name')

        category = Category(name=name)
        category.save_category()

        return render_template('home/add_category.html', title="Add Category", mycategories=mylist, message="Category added.")

    return render_template("home/add_category.html", title="Add Category", mycategories=mylist)


@home.route("/add/pitch", methods=['GET', 'POST'])
@login_required
def add_pitch_form():
    rows = Category.get_categories()

    id = []
    name = []
    created_at = []

    for row in rows:
        id.append(row.id)
        name.append(row.name)
        created_at.append(row.created_at)

    mylist = zip(id, name, created_at)

    if request.method == 'POST':
        name = request.form.get('name')
        category_id = request.form.get('category_id')
        user_id = request.form.get('user_id')

        pitch = Pitch(name=name, category_id=category_id, user_id=user_id)
        pitch.save_pitch()

        return render_template('home/add_pitch.html', title="Add Pitch", mycategories=mylist, message="Pitch added.")

    return render_template("home/add_pitch.html", title="Add Pitch", mycategories=mylist)
