# Suggested Prompts for SSOJet OIDC — Next.js

## Full Implementation

> "Add 'Sign in with SSO' to my Next.js (App Router) application using SSOJet.
>
> Follow `skills/authentication/oidc-hosted-page-nextjs/SKILL.md` exactly.
>
> Requirements:
> 1. Install `openid-client` and configure the OIDC Issuer in a server-side utility.
> 2. Modify my existing login page to add an SSO toggle.
> 3. Create an API route (`/api/auth/sso`) that initiates the OIDC redirect with `login_hint`.
> 4. Create a callback API route (`/api/auth/callback`) that exchanges the code for tokens and creates a session.
> 5. Handle errors and redirect back to login with a message on failure.
>
> My SSOJet config:
> - Issuer URL: `https://auth.ssojet.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:3000/api/auth/callback`"

## Add SSO to Existing Login

> "My Next.js app uses NextAuth / credentials login. Add SSOJet SSO as an alternative sign-in method.
> Reference the skill file at `skills/authentication/oidc-hosted-page-nextjs/SKILL.md`.
> Keep both password and SSO login working side by side."
