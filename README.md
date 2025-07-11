# Social-Authentication Project

This is a Django project demonstrating social authentication using `social-auth-app-django` with Google, GitHub, and LinkedIn. It includes a custom user model and basic user authentication functionalities.

## Features

*   User registration and login with email and password.
*   Social login via Google OAuth2.
*   Social login via GitHub OAuth2.
*   Social login via LinkedIn OpenID Connect.
*   Custom User Model.

## Technologies Used

*   Python 3.x
*   Django 5.x
*   `social-auth-app-django`

## Setup Instructions

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Social-Authentication.git
cd Social-Authentication
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

*   **On Windows:**
    ```bash
    .\venv\Scripts\activate
    ```
*   **On macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

### 4. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 5. Database Migrations

Apply the database migrations to create the necessary tables:

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)

To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your superuser credentials.

### 7. Social Authentication Configuration

This project uses `social-auth-app-django` for social logins. You need to obtain API keys/secrets from Google, GitHub, and LinkedIn and add them to your `social_auth_project/settings.py` file.

**Example (settings.py):**

```python
# Google OAuth2
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'YOUR_GOOGLE_CLIENT_ID'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'YOUR_GOOGLE_CLIENT_SECRET'

# GitHub OAuth2
SOCIAL_AUTH_GITHUB_KEY = 'YOUR_GITHUB_CLIENT_ID'
SOCIAL_AUTH_GITHUB_SECRET = 'YOUR_GITHUB_CLIENT_SECRET'

# LinkedIn OpenID Connect
SOCIAL_AUTH_LINKEDIN_OIDC_KEY = 'YOUR_LINKEDIN_CLIENT_ID'
SOCIAL_AUTH_LINKEDIN_OIDC_SECRET = 'YOUR_LINKEDIN_CLIENT_SECRET'
SOCIAL_AUTH_LINKEDIN_OIDC_SCOPE = ['openid', 'profile', 'email']
```

**Important:** For development, ensure your redirect URIs are correctly configured in your OAuth provider settings (e.g., `http://localhost:8000/oauth/complete/google-oauth2/`).

### 8. Run the Development Server

```bash
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`.

## Usage

*   Navigate to `http://127.0.0.1:8000/` in your web browser.
*   You can register a new account or log in using your email and password.
*   Click on the social login buttons (Google, GitHub, LinkedIn) to authenticate using your respective social accounts.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is licensed under the MIT License.
