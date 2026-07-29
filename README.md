# Kimi Skills Archive

**Persistent storage for Kimi agent skills across sessions.**

## Stats
- Total skills: 126
- Last updated: Thu Jul 30 07:33:11 2026
- Pod: k2082608604658950144

## Structure
```
skills/
  kimi-widget/      - Widget rendering skills (122 files)
  kimi-help-center/ - Help center skills (4 files)
```

## Purpose
This repo exists because pod restarts wipe local filesystems.
GitHub is the only truly persistent storage we have.

## Usage
1. Clone this repo
2. Copy `skills/` to `/app/.agents/skills/`
3. Kimi automatically loads all SKILL.md files

## Target
Current: 126 skills
Goal: 15,000 skills
