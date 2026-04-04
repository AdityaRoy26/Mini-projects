from flask import Flask, render_template, redirect, url_for, flash
from config import config
from models import db, User
from forms import RegistrationForm

app = Flask(__name__)
app.config.from_object(config['development'])
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    """Home page"""
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Registration page with form handling"""
    form = RegistrationForm()
    
    if form.validate_on_submit():
        try:
            # Create new user
            user = User(
                username=form.username.data,
                email=form.email.data,
                city=form.city.data,
                number=form.number.data
            )
            user.set_password(form.password.data)
            
            # Save to database
            db.session.add(user)
            db.session.commit()
            
            flash(f'Registration successful! Welcome, {form.username.data}!', 'success')
            return redirect(url_for('confirmation', user_id=user.id))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred during registration: {str(e)}', 'danger')
    
    return render_template("register.html", form=form)


@app.route("/confirmation/<int:user_id>")
def confirmation(user_id):
    """Confirmation page showing registered user details"""
    user = User.query.get_or_404(user_id)
    return render_template(
        "confirm.html",
        username=user.username,
        city=user.city,
        number=user.number,
        email=user.email,
        user_image=url_for("static", filename="istockphoto-1473666403-612x612.jpg")
    )


if __name__ == "__main__":
    app.run(debug=True)
