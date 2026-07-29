# Suggested Prompts for SSOJet M2M Authentication

## Full Implementation

> "I need to authenticate my backend service / daemon with a SSOJet-protected API using Client Credentials.
>
> Follow `skills/authentication/m2m-client-credentials/SKILL.md` exactly.
>
> Requirements:
> 1. Use the Client Credentials grant to obtain an access token from SSOJet.
> 2. Cache the token and reuse it until expiry (with a 60-second buffer).
> 3. Use the token to call my protected API at `<my_api_endpoint>`.
> 4. Handle token refresh automatically when the cached token expires.
>
> My M2M credentials:
> - Client ID: `<service_client_id>`
> - Client Secret: `<service_client_secret>`
> - Token Endpoint: `https://auth.ssojet.com/oauth2/token`
> - Target language: **{Node.js / Python / Go / C#}**"

## Cron Job / Scheduled Task

> "I have a cron job that needs to call a SSOJet-protected API every hour.
> Reference `skills/authentication/m2m-client-credentials/SKILL.md`.
>
> Implement:
> - Token acquisition at startup with caching.
> - Automatic refresh before each API call if the token is expired.
> - Proper error handling if the token endpoint is unreachable."
