# Contributing Guide

This repository is currently maintained as a controlled manuscript project.

## Build Workflow

1. Check `PROGRESS.md`.
2. Identify the next chapter.
3. Confirm it exists in `ROADMAP.md`.
4. Generate the chapter using the frozen template.
5. Save it to the correct volume and part folder.
6. Review formatting and numbering.
7. Update `PROGRESS.md`.
8. Commit changes.

## Commit Example

```bash
git add .
git commit -m "feat(volume-1): add set interface chapter"
git push origin main
```

## Review Checklist

Before committing, verify:

- Chapter follows the 18-section template.
- No exercises are present.
- Examples are enterprise-oriented.
- Java code is production-quality.
- Diagrams use Markdown/ASCII.
- Tables are formatted correctly.
- EDR section exists.
- Staff Engineer Perspective exists.
- Summary and Next Chapter exist.
- No roadmap changes were made.

## Do Not

- Change the roadmap.
- Change chapter structure.
- Add new topics.
- Add exercises.
- Rename folders.
- Split chapters without explicit approval.
