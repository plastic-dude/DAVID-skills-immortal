# Suggested Prompts for Implementing SSOJet OIDC Authentication

Use these prompts when asking an AI assistant to add "Sign in with SSO" to your application using SSOJet.

> **Tip:** Replace `{framework}` with your target framework (e.g., Next.js, React, Node.js, Go, etc.) and point the agent to the matching skill file.

## Option 1: Full Implementation (Comprehensive)

> "I need to add 'Sign in with SSO' to my existing **{framework}** application using SSOJet as an OIDC provider.
>
> Please follow the guide in `skills/authentication/oidc-hosted-page-{framework}/SKILL.md` exactly.
>
> Key requirements:
> 1. Install the required OIDC library listed in the prerequisites.
> 2. Set up the OIDC client configuration with my SSOJet Issuer URL and Client ID.
> 3. Modify the existing login page to add an **SSO toggle** that hides the password field.
> 4. Implement the **SSO redirect** with `login_hint` from the email field.
> 5. Handle the **OIDC callback** to exchange the authorization code for tokens and create a user session.
> 6. Add error handling for failed authentication attempts.
>
> My SSOJet configuration:
> - Issuer URL: `https://auth.ssojet.com`
> - Client ID: `<my_client_id>`
> - Redirect URI: `http://localhost:3000/api/auth/callback`
>
> Please start with the environment/config setup and then modify the login page."

## Option 2: Step-by-Step (Iterative)

**Step 1: Setup & Configuration**
> "Help me set up SSOJet OIDC in my **{framework}** project.
> Reference `skills/authentication/oidc-hosted-page-{framework}/SKILL.md`.
>
> - Install the required dependencies.
> - Create the environment variables / config file for Issuer URL, Client ID, Client Secret, and Redirect URI.
> - Initialize the OIDC client / middleware.
>
> Don't modify any pages yet — just get the OIDC configuration in place."

**Step 2: Login Page Modification**
> "Now modify my existing login page to support SSO.
> Follow the 'Update Login Page/UI' section in the skill file.
>
> Add:
> - A 'Sign in with SSO' toggle button.
> - When toggled, hide the password field and change the submit button to 'Continue with SSO'.
> - On submit in SSO mode, redirect to the SSO initiation endpoint with the email as `login_hint`."

**Step 3: Callback Handler**
> "Create the OIDC callback handler.
> Follow the callback section in the skill file.
>
> It should:
> - Exchange the authorization code for tokens.
> - Extract the user's profile (name, email, sub) from the ID token or userinfo endpoint.
> - Create or update a session for the authenticated user.
> - Redirect to the dashboard on success, or back to login with an error message on failure."

**Step 4: Testing**
> "Help me test the SSO integration end-to-end.
> - Walk me through starting the app and navigating to the login page.
> - Show me how to verify the SSO toggle works.
> - Confirm the redirect to SSOJet and the callback flow."

## Option 3: Add SSO to an Existing Auth System

> "My **{framework}** app already has email/password login.
> I want to add 'Sign in with SSO' as an alternative without breaking the existing flow.
>
> Please reference `skills/authentication/oidc-hosted-page-{framework}/SKILL.md` and:
> 1. Keep the existing login form intact.
> 2. Add a toggle for SSO mode that conditionally shows/hides the password field.
> 3. When in SSO mode, initiate the OIDC flow instead of the password login.
> 4. After SSO callback, create a session the same way the existing login does.
>
> Make sure both login paths (password and SSO) lead to the same authenticated state."

## Option 4: M2M / Backend Service Authentication

> "I need to authenticate my backend service with a SSOJet-protected API using Machine-to-Machine credentials.
>
> Please follow `skills/authentication/m2m-client-credentials/SKILL.md`.
>
> Requirements:
> - Use the Client Credentials grant to obtain an access token.
> - Cache the token and reuse until expiry.
> - Use the token to call `{my_api_endpoint}`.
>
> My M2M credentials:
> - Client ID: `<service_client_id>`
> - Client Secret: `<service_client_secret>`
> - Token Endpoint: `https://auth.ssojet.com/oauth2/token`"
