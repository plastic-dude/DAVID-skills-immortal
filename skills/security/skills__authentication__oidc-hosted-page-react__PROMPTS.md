# Suggested Prompts for SSOJet OIDC — React

## Full Implementation

> "Add 'Sign in with SSO' to my React application using SSOJet.
>
> Follow `skills/authentication/oidc-hosted-page-react/SKILL.md` exactly.
>
> Requirements:
> 1. Install `oidc-client-ts`, `react-oidc-context`, and `react-router-dom`.
> 2. Configure the OIDC provider and wrap my app with `<AuthProvider>`.
> 3. Add an SSO toggle to my existing login page component.
> 4. Use `auth.signinRedirect()` with `login_hint` when SSO is selected.
> 5. Create an `AuthCallback` component that checks auth state and navigates.
> 6. Set up the route for `/auth/callback`.
>
> My SSOJet config:
> - Issuer URL: `https://auth.ssojet.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:5173/auth/callback`"

## Add SSO to Existing Login

> "My React app already has a custom auth context with JWT login. Add SSOJet SSO alongside it.
> Reference `skills/authentication/oidc-hosted-page-react/SKILL.md`.
> Both paths should result in the same authenticated state in my auth context."
