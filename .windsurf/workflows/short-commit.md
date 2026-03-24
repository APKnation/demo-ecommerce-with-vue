---
description: Create commits with short messages (3-4 words maximum)
---

# Short Commit Message Workflow

This workflow ensures all commit messages are concise and limited to 3-4 words maximum.

## Steps:

1. **Stage your changes**
   ```bash
   git add .
   ```

2. **Create a short commit message**
   ```bash
   git commit -m "your-short-message"
   ```
   
   **Rules:**
   - Maximum 3-4 words
   - Be descriptive but brief
   - Use present tense
   - No periods at the end

   **Examples:**
   - "Add auth components"
   - "Fix login bug"
   - "Update main file"
   - "Create register view"

3. **Push changes**
   ```bash
   git push origin main
   ```

## Tips:
- Focus on what changed, not why
- Use imperative mood (Add, Fix, Update, Remove, etc.)
- Keep it under 30 characters total when possible
- Think of it as a headline, not a description

## Bad Examples (avoid):
- "I added the authentication components to the frontend because we need users to be able to log in"
- "This commit fixes a bug that was preventing users from registering new accounts"
- "Updated the main.js file to import the new authentication composables"

## Good Examples:
- "Add auth system"
- "Fix register flow"
- "Update imports"
- "Create login page"
