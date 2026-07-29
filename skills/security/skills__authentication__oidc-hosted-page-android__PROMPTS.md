# Suggested Prompts for SSOJet OIDC — Android

## Full Implementation

> "Add 'Sign in with SSO' to my native Android (Kotlin) application using SSOJet.
>
> Follow `skills/authentication/oidc-hosted-page-android/SKILL.md` exactly.
>
> Requirements:
> 1. Add `net.openid:appauth` to `build.gradle`.
> 2. Configure the custom URL scheme and manifest redirect activity.
> 3. Create an `AuthConfig` object with Issuer, Client ID, and Redirect URI.
> 4. Add an SSO toggle button to my login activity layout.
> 5. Use AppAuth to launch the authorization request with PKCE and `login_hint`.
> 6. Handle the callback in `registerForActivityResult`, exchange the code for tokens, and navigate to the dashboard.
>
> My SSOJet config:
> - Issuer URL: `https://auth.ssojet.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `com.example.myapp://auth/callback`"
