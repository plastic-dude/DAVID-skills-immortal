# Suggested Prompts for SSOJet OIDC — Angular

## Full Implementation

> "Add 'Sign in with SSO' to my Angular application using SSOJet.
>
> Follow `skills/authentication/oidc-hosted-page-angular/SKILL.md` exactly.
>
> Requirements:
> 1. Install `angular-auth-oidc-client`.
> 2. Configure the OIDC module in `app.config.ts` with PKCE (no client secret).
> 3. Create an `AuthService` that wraps `OidcSecurityService` and supports `login_hint`.
> 4. Add an SSO toggle to my existing login component.
> 5. Create an `AuthCallbackComponent` that handles the redirect and navigates to `/dashboard`.
> 6. Set up the route for `/auth/callback`.
>
> My SSOJet config:
> - Issuer URL: `https://auth.ssojet.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:4200/auth/callback`"

## Add SSO to Existing Login

> "My Angular app already has a form-based login. Add SSOJet SSO as an alternative.
> Reference `skills/authentication/oidc-hosted-page-angular/SKILL.md`.
> The SSO path should use PKCE and the existing login should stay untouched."
