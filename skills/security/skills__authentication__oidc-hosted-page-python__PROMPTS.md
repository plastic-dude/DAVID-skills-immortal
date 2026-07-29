# Suggested Prompts for SSOJet OIDC — Python / Flask

## Full Implementation

> "Add 'Sign in with SSO' to my Flask application using SSOJet.
>
> Follow `skills/authentication/oidc-hosted-page-python/SKILL.md` exactly.
>
> Requirements:
> 1. Install `authlib` and `flask`.
> 2. Register the SSOJet OIDC provider using Authlib's OAuth registry.
> 3. Add an SSO toggle to my existing Jinja login template.
> 4. Create a `/auth/sso` route to initiate the OIDC redirect with `login_hint`.
> 5. Create a `/auth/callback` route that exchanges the code for tokens and stores user info in the Flask session.
>
> My SSOJet config:
> - Issuer URL: `https://auth.ssojet.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:5000/auth/callback`"

## Add SSO to Existing Login

> "My Flask app uses Flask-Login for authentication. Add SSOJet SSO as an alternative.
> Reference `skills/authentication/oidc-hosted-page-python/SKILL.md`.
> Ensure the SSO callback creates a Flask-Login session identical to the password flow."
