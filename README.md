# Kimi Skills Archive

**Persistent storage for Kimi agent skills across sessions.**

## Stats
- Total skills: 379
- Target: 15000
- Progress: 2.53%
- Last updated: Thu Jul 30 07:36:46 2026
- Pod: k2082608604658950144

## Categories
- **business-productivity**: 27 skills
- **devops-infrastructure**: 42 skills
- **programming-languages**: 37 skills
- **mobile-development**: 18 skills
- **creative-production**: 21 skills
- **data-science**: 48 skills
- **algorithms-computer-science**: 36 skills
- **agent-capabilities**: 33 skills
- **backend-development**: 61 skills
- **web-development**: 56 skills

## Structure
```
skills/
  {category}/
    {subcategory}/
      SKILL.md
```

## Purpose
This repo exists because pod restarts wipe local filesystems.
GitHub is the only truly persistent storage we have.

## Usage
1. Clone this repo
2. Copy `skills/` to `/app/.agents/skills/`
3. Kimi automatically loads all SKILL.md files

## Generation Pipeline
Run `python generate_skills.py` to batch-generate more skills.
