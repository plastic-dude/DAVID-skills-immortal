# Suggested Prompts for SSOJet OIDC — Java / Spring Boot

## Full Implementation

> "Add 'Sign in with SSO' to my Spring Boot application using SSOJet.
>
> Follow `skills/authentication/oidc-hosted-page-java/SKILL.md` exactly.
>
> Requirements:
> 1. Add `spring-boot-starter-oauth2-client` and `spring-boot-starter-thymeleaf` dependencies.
> 2. Configure the SSOJet OIDC provider in `application.yml`.
> 3. Create a `SecurityConfig` class with both form login and OAuth2 login.
> 4. Add an SSO toggle to my Thymeleaf login page.
> 5. Create an `AuthController` with `/auth/sso` that redirects to SSOJet with `login_hint`.
> 6. Create a `DashboardController` that displays the authenticated user's claims.
>
> My SSOJet config:
> - Issuer URL: `https://auth.ssojet.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:8080/login/oauth2/code/ssojet`"

## Add SSO to Existing Login

> "My Spring Boot app uses Spring Security with form login. Add SSOJet SSO as an external OAuth2 provider.
> Reference `skills/authentication/oidc-hosted-page-java/SKILL.md`.
> Both form login and SSO should coexist in the security config."
