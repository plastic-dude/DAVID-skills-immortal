# 🚀 SSOJet Agent Skills

Empower your AI agents with specialized knowledge to implement Authentication, Team Management, and SCIM provisioning in minutes.

[![SSOJet Docs](https://img.shields.io/badge/SSOJet-Documentation-blue?style=for-the-badge&logo=read-the-docs&logoColor=white)](https://docs.ssojet.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## 📑 Table of Contents

- [Overview](#overview)
- [Quick Start](#-quick-start)
- [How to Use](#️-how-to-use)
  - [For AI Agents](#-for-ai-agents)
  - [For Developers](#-for-developers)
- [Available Skills](#-available-skills)
  - [Authentication](#-authentication)
  - [Management](#-management)
- [Resource Center](#-resource-center)
- [Contributing](#-contributing)

---

## Overview

**SSOJet Agent Skills** is a curated collection of high-context "skills" designed specifically for AI coding agents (such as Antigravity, Cursor, Claude Code, or Codex). 

Integrating Single Sign-On (SSO), Team Management, and SCIM provisioning can be complex. These skills provide your AI agent with the exact implementation patterns, API specifications, and troubleshooting steps needed to get the job done right the first time.

## ⚡ Quick Start

Install all SSOJet skills into your coding agents with a single command:

```bash
npx add-skill ssojet/skills
```

Or install a specific skill:

```bash
npx add-skill ssojet/skills --skill oidc-hosted-page-nextjs
```

> The CLI **auto-detects** your installed agents (Antigravity, Cursor, Claude Code, Codex) and places skills in the correct directory.

## 🛠️ How to Use

### 🤖 For AI Agents

**Option 1: Install via CLI** *(Recommended)*

```bash
# Install all skills
npx add-skill ssojet/skills

# Install specific skills
npx add-skill ssojet/skills --skill oidc-hosted-page-nextjs --skill team-management

# List available skills
npx add-skill ssojet/skills --list

# Install globally (across all projects)
npx add-skill ssojet/skills -g
```

**Option 2: Context Injection**

Instruct your agent to read a specific skill before starting:
> *"Analyze the skill at `./skills/authentication/oidc-hosted-page-nextjs/SKILL.md` and implement the login flow in my current project."*

**Option 3: Manual Installation**

Copy the relevant skill folder into your project's agent skills directory:
- Antigravity: `.antigravity/skills/`
- Cursor: `.cursor/skills/`
- Claude Code: `.claude/skills/`

### 👨‍💻 For Developers
Each skill folder contains:
- `SKILL.md`: A comprehensive guide and technical specification.
- `PROMPTS.md` (Optional): Optimized prompts to help you direct an AI to implement the skill.

---

## 📚 Available Skills

### 🔐 Authentication
Seamlessly integrate "Sign in with SSO" using the SSOJet Hosted Login Page.

| Language / Framework | Skill Link | Description |
| :--- | :--- | :--- |
| **Generic OIDC** | [ssojet-auth-oidc](./skills/authentication/oidc-hosted-page/SKILL.md) | Standard OIDC Authorization Code flow. |
| **Next.js** | [ssojet-auth-nextjs](./skills/authentication/oidc-hosted-page-nextjs/SKILL.md) | Full App Router integration guide. |
| **Node.js** | [ssojet-auth-node](./skills/authentication/oidc-hosted-page-node/SKILL.md) | Backend implementation for Express/Node. |
| **Python** | [ssojet-auth-python](./skills/authentication/oidc-hosted-page-python/SKILL.md) | Integration for Flask. |
| **Go** | [ssojet-auth-go](./skills/authentication/oidc-hosted-page-go/SKILL.md) | Lightweight Go implementation. |
| **.NET Core** | [ssojet-auth-dotnet](./skills/authentication/oidc-hosted-page-dotnet/SKILL.md) | ASP.NET Core OIDC middleware integration. |
| **Angular** | [ssojet-auth-angular](./skills/authentication/oidc-hosted-page-angular/SKILL.md) | SPA with angular-auth-oidc-client. |
| **React** | [ssojet-auth-react](./skills/authentication/oidc-hosted-page-react/SKILL.md) | SPA with react-oidc-context. |
| **Java** | [ssojet-auth-java](./skills/authentication/oidc-hosted-page-java/SKILL.md) | Spring Boot OAuth2 client integration. |
| **Laravel** | [ssojet-auth-laravel](./skills/authentication/oidc-hosted-page-laravel/SKILL.md) | Laravel Socialite OIDC provider. |
| **PHP** | [ssojet-auth-php](./skills/authentication/oidc-hosted-page-php/SKILL.md) | Vanilla PHP with openid-connect-php. |
| **Android** | [ssojet-auth-android](./skills/authentication/oidc-hosted-page-android/SKILL.md) | Native Android with AppAuth. |
| **iOS** | [ssojet-auth-ios](./skills/authentication/oidc-hosted-page-ios/SKILL.md) | Native iOS/Swift with AppAuth. |
| **M2M** | [ssojet-auth-m2m](./skills/authentication/m2m-client-credentials/SKILL.md) | Machine-to-Machine Client Credentials flow. |

### 👥 Management
Advanced organizational and user management capabilities.

| Skill | Description |
| :--- | :--- |
| [Team Management](./skills/management/team-management/SKILL.md) | API-driven team creation, role assignment, and invitations. |

---

## 📖 Resource Center

Explore our granular API documentation and references:

| Category | Reference Link |
| :--- | :--- |
| **Core APIs** | [Users](./skills/apis/users.md), [Tenants](./skills/apis/tenants.md),
| **Advanced** | [Roles](./skills/apis/roles.md),[Permissions](./skills/apis/permissions.md),[Team](./skills/apis/team-invites.md)
| **General Docs** | [Official SSOJet Documentation](https://docs.ssojet.com) |

## 🤝 Contributing

We are constantly expanding our library of skills. If you have built an integration for a new framework or found a bug:
1. **Fork** the repository.
2. **Create** a new branch (`feature/new-skill`).
3. **Submit** a Pull Request.

---

Built with ⚡ by the [SSOJet Team](https://ssojet.com).
