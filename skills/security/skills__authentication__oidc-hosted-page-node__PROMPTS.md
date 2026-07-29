# Suggested Prompts for SSOJet OIDC — Node.js / Express

## Full Implementation

> "Add 'Sign in with SSO' to my Express.js application using SSOJet.
>
> Follow `skills/authentication/oidc-hosted-page-node/SKILL.md` exactly.
>
> Requirements:
> 1. Install `openid-client` and `express-session`.
> 2. Configure the OIDC Issuer and client in a dedicated module.
> 3. Add an SSO toggle to my existing EJS/Pug/HTML login page.
> 4. Create `/auth/sso` route to initiate the OIDC redirect with `login_hint`.
> 5. Create `/auth/callback` route that exchanges the code for tokens and stores user info in the session.
>
> My SSOJet config:
> - Issuer URL: `https://auth.ssojet.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:3000/auth/callback`"

## Add SSO to Existing Login

> "My Express app already has Passport.js local strategy for login. Add SSOJet SSO as an additional strategy.
> Reference `skills/authentication/oidc-hosted-page-node/SKILL.md`.
> Keep both login paths working and leading to the same session."
