# Registration App - Flask with SQLAlchemy

A complete user registration application demonstrating Flask-WTF forms, SQLAlchemy ORM, and database persistence.

## Features

- **Flask-WTF Forms**: Secure forms with CSRF protection
- **Form Validators**: 
  - DataRequired, Email, Length, EqualTo validators
  - Custom validators for duplicate username/email detection
  - Password confirmation matching
- **SQLAlchemy ORM**: User model with proper relationships and constraints
- **Password Security**: Passwords hashed using Werkzeug
- **Database Persistence**: User data saved to SQLite database
- **Custom HTML/CSS**: Clean, responsive UI without AI-generated boilerplate
- **Error Handling**: Form validation errors displayed on registration page
- **Flash Messages**: User feedback on successful registration

## Project Structure

```
flask_app/
├── flaskapp.py          # Main Flask application
├── config.py            # Configuration management
├── models.py            # SQLAlchemy User model
├── forms.py             # Flask-WTF RegistrationForm
├── templates/
│   ├── base.html        # Base template with navigation
│   ├── home.html        # Home page
│   ├── register.html    # Registration form with error handling
│   └── confirm.html     # Confirmation page (database query)
├── static/
│   └── istockphoto-1473666403-612x612.jpg  # Waterfall image
└── users.db             # SQLite database (created on first run)
```

## Required Packages

```
Flask==2.3.0
Flask-WTF==1.1.1
Flask-SQLAlchemy==3.0.5
Werkzeug==2.3.0
WTForms==3.0.1
email-validator==2.0.0
```

## How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install Flask Flask-WTF Flask-SQLAlchemy Werkzeug WTForms email-validator
```

### 2. Navigate to Project Directory

```bash
cd flask_app
```

### 3. Run the Application

```bash
python flaskapp.py
```

The app will start at `http://localhost:5000`

### 4. Access the App

- **Home Page**: `http://localhost:5000/`
- **Registration**: `http://localhost:5000/register`
- **Confirmation**: Automatically redirected after successful registration

## Database Setup

The application automatically creates `users.db` on first run. No manual setup required.

To reset the database, delete `users.db` and restart the app.

## Form Validation

The registration form includes:

- **Username**: Required, 3-80 characters, must be unique
- **Email**: Required, valid email format, must be unique
- **City**: Required, 2-100 characters
- **Phone Number**: Required, 10-20 characters
- **Password**: Required, minimum 6 characters
- **Confirm Password**: Must match password field

## Key Implementation Details

### models.py
- `User` model with proper fields and constraints
- Password hashing with `set_password()` and verification with `check_password()`
- Indexed unique fields for efficient lookups

### forms.py
- Flask-WTF `RegistrationForm` with all validators
- Custom validation methods for duplicate detection
- User-friendly error messages

### flaskapp.py
- SQLAlchemy initialization with Flask app
- Form-based registration with database persistence
- Error handling and rollback on registration failure
- Confirmation page queries database to verify user was saved

### templates/
- Clean, custom HTML without boilerplate
- Base template for consistent navigation
- Inline styling for simplicity
- Form error display with visual feedback
- Flash message rendering

## Testing the Registration

1. Fill out the registration form
2. Submit the form
3. Observe validation errors if any field is invalid
4. On successful submission, you'll be redirected to the confirmation page
5. The confirmation page queries the database to fetch the user details
6. User data is persistently stored in `users.db`

## Security Features

- CSRF protection enabled via Flask-WTF
- Password hashing using Werkzeug security
- Email validation with email-validator
- Unique constraints on username and email
- Input length validation
- Database rollback on errors

## Future Enhancements

- Login functionality with session management
- Email verification
- Password reset functionality
- Admin dashboard to view all users
- User profile updates
- Delete account functionality
