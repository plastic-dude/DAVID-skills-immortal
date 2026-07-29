# Suggested Prompts for SSOJet OIDC — PHP / Laravel

## Full Implementation

> "Add 'Sign in with SSO' to my Laravel application using SSOJet.
>
> Follow `skills/authentication/oidc-hosted-page-laravel/SKILL.md` exactly.
>
> Requirements:
> 1. Install `laravel/socialite`.
> 2. Create a custom SSOJet Socialite provider and register it in `AppServiceProvider`.
> 3. Add environment variables for Issuer URL, Client ID, Client Secret, and Redirect URI.
> 4. Add an SSO toggle to my existing Blade login template.
> 5. Create an `SSOController` that handles login form submission (detecting SSO vs password) and the OIDC callback.
> 6. The callback should `updateOrCreate` the user and start a Laravel session.
>
> My SSOJet config:
> - Issuer URL: `https://auth.ssojet.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:8000/auth/callback`"

## Add SSO to Existing Login

> "My Laravel app uses the default Breeze/Jetstream auth. Add SSOJet SSO as an alternative.
> Reference `skills/authentication/oidc-hosted-page-laravel/SKILL.md`.
> Keep the existing auth scaffolding and add SSO alongside it."
