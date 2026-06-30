# Enterprise Java Mastery – Project Constitution

This document is the governing authoring guide for the entire Enterprise Java Mastery book series.

## Project Identity

Title: Enterprise Java Mastery

Type: Premium enterprise Java technical book series

Audience: Java developers with 10+ years of experience

Primary goal: Create a production-grade, architecture-aware, senior-level Enterprise Java reference.

This is not a beginner Java book. This is not a generic interview question bank. This is an enterprise engineering reference.

## Target Reader

The reader is expected to already understand:

- Java fundamentals
- Object-oriented programming
- Basic Collections
- Basic Spring Boot
- Basic SQL
- General software engineering concepts

The book should focus on senior-level depth, production decision-making, internal working, performance, architecture, and enterprise trade-offs.

## Writing Style

Use a professional, concise, technically precise writing style.

Avoid:

- Beginner explanations
- Filler text
- Motivational language
- Jokes
- Emojis
- Unnecessary storytelling
- Toy-only examples

Prefer:

- Enterprise scenarios
- Production trade-offs
- Performance implications
- Architecture reasoning
- Staff Engineer-level decision-making

## Frozen Chapter Template

Every chapter must follow exactly this structure:

1. Learning Objectives
2. Introduction
3. Why This Matters in Enterprise Applications
4. Core Concepts
5. Internal Working
6. Architecture / Design Discussion
7. Diagrams
8. Code Listings
9. Tables
10. Performance Considerations
11. Engineering Decision Record (EDR)
12. Enterprise Use Cases
13. Best Practices
14. Common Mistakes
15. Interview Questions & Answers
16. Staff Engineer Perspective
17. Summary
18. Next Chapter

Do not add exercises.

## Engineering Decision Record Format

Every chapter must include an Engineering Decision Record section with:

- Decision
- When to use this
- When to avoid this
- Trade-offs
- Production recommendation

## Code Standards

All Java code must:

- Be Java 21 compatible unless discussing legacy behavior
- Use production-oriented naming
- Use meaningful packages
- Avoid toy examples
- Prefer enterprise domains such as banking, payments, insurance, retail, logistics, identity, workflow, messaging, and sustainability
- Be readable and maintainable
- Avoid cleverness when clarity is better

## Enterprise Focus

Every chapter must answer:

- Why does this matter in enterprise applications?
- What production issues can this cause?
- What are the performance implications?
- What are the memory implications?
- What are the trade-offs?
- How should a Staff Engineer think about this?
- What interview questions are commonly asked at senior level?

## Case Study Rule

Enterprise case studies belong only to Volume II, Part 11.

Do not add case studies elsewhere.

## Build Command Rule

When the user says `build next`, generate the next unfinished chapter from the frozen roadmap.

Before generating, internally validate:

- Correct roadmap position
- No duplicate topic
- Correct folder
- Correct template
- Enterprise relevance
- Production-grade examples
- Summary and next chapter included

## Scope Freeze

Do not add, remove, rename, reorder, merge, or split topics until Version 1.0 of the full manuscript is complete unless explicitly instructed by the user.
