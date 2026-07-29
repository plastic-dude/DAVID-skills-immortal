# Suggested Prompts for SSOJet OIDC — Go

## Full Implementation

> "Add 'Sign in with SSO' to my Go web application using SSOJet.
>
> Follow `skills/authentication/oidc-hosted-page-go/SKILL.md` exactly.
>
> Requirements:
> 1. Install `coreos/go-oidc/v3` and `golang.org/x/oauth2`.
> 2. Set up the OIDC provider and OAuth2 config.
> 3. Add an SSO toggle to my existing HTML login template.
> 4. Create `/auth/sso` handler to initiate the OIDC redirect with `login_hint` and CSRF state.
> 5. Create `/auth/callback` handler that validates the state, exchanges the code, verifies the ID token, and creates a session cookie.
>
> My SSOJet config:
> - Issuer URL: `https://auth.ssojet.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:8080/auth/callback`"

## Add SSO to Existing Login

> "My Go app uses gorilla/sessions for auth. Add SSOJet SSO alongside the existing password login.
> Reference `skills/authentication/oidc-hosted-page-go/SKILL.md`.
> Both flows should result in the same session cookie."
