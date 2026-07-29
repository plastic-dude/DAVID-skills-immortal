# Suggested Prompts for SSOJet OIDC — .NET Core

## Full Implementation

> "Add 'Sign in with SSO' to my ASP.NET Core application using SSOJet.
>
> Follow `skills/authentication/oidc-hosted-page-dotnet/SKILL.md` exactly.
>
> Requirements:
> 1. Install `Microsoft.AspNetCore.Authentication.OpenIdConnect` NuGet package.
> 2. Configure the OIDC middleware in `Program.cs` with my SSOJet credentials.
> 3. Add an SSO toggle to my existing Razor login view.
> 4. Create an `AccountController` that handles both password login and SSO initiation with `login_hint`.
> 5. The OIDC middleware callback should set the cookie and redirect to `/dashboard`.
>
> My SSOJet config:
> - Issuer URL: `https://auth.ssojet.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:5000/auth/callback`"

## Add SSO to Existing Login

> "My ASP.NET Core app uses Identity for authentication. Add SSOJet SSO as an external login provider.
> Reference `skills/authentication/oidc-hosted-page-dotnet/SKILL.md`.
> Keep the existing Identity login working alongside SSO."
