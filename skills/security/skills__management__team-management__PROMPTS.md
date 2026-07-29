# Suggested Prompts for Implementing Team Management

Use these prompts when asking an AI assistant to implement the Team Management features in your Next.js application.

## Option 1: Full Implementation (Comprehensive)

> "I need to implement a comprehensive Team Management system in my Next.js application using SSOJet.
>
> Please follow the guide in `skills/management/team-management/SKILL.md` exactly.
>
> Key requirements:
> 1.  Implement the **Tenant Selection Flow** (Scenario A & B) as described in Step 4.
> 2.  Create a **Team Settings Page** that lists members using the API from Step 6.
> 3.  Add an **Invite Member** feature using the modal UI pattern described in the "Frontend/UI Implementation Guidelines".
> 4.  Ensure all API calls happen on the backend (Next.js API routes or Server Actions) using the management token.
>
> Please start by setting up the tenant context provider and the backend API routes."

## Option 2: Step-by-Step (Iterative)

**Step 1: Backend Setup**
> "Help me set up the backend API routes for Team Management.
> Reference `skills/management/team-management/SKILL.md`.
>
> Create Next.js API routes (or Server Actions) for:
> - Fetching user tenants (`GET /users/{id}/tenants`)
> - Creating a new tenant (`POST /tenants`)
> - Listing tenant members (`GET /tenants/{id}/users`)
>
> Ensure proper error handling and use the management token as described in the Core Architecture Rules."

**Step 2: Tenant Switcher**
> "Now, let's build the Tenant Switcher component.
> Refer to the 'Frontend/UI Implementation Guidelines' in `skills/management/team-management/SKILL.md`.
>
> It should:
> - List the user's available tenants.
> - Allow creating a new organization (handling the 'No Tenant' state).
> - Persist the selected tenant ID in the session/cookie."

**Step 3: Team Settings UI**
> "Finally, create the Team Settings page.
> Follow the 'Team Members List' and 'Invite Member Modal' guidelines in the skill file.
> Use the backend routes we created earlier to fetch and manage data."
