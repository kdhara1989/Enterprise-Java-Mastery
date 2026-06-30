# Enterprise Java Mastery – Style Guide

## Purpose

This guide ensures consistent writing, formatting, and technical depth across all chapters.

## Audience Depth

Assume the reader has 10+ years of Java experience.

Do not explain syntax as if the reader is new to Java.

Explain:

- Internals
- Trade-offs
- Edge cases
- Production concerns
- Architecture impact
- Performance implications
- Interview expectations

## Tone

Use a professional technical tone.

Preferred:

- Direct
- Precise
- Enterprise-focused
- Practical
- Decision-oriented

Avoid:

- Casual jokes
- Emojis
- Beginner analogies
- Filler paragraphs
- Marketing language

## Standard Chapter Structure

Every chapter must include:

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

## Code Style

Use:

- Java 21
- `package com.enterprise...`
- Meaningful names
- Records where useful
- Immutable collections where appropriate
- Defensive copies where needed
- Clear exception handling
- Enterprise scenario naming

Avoid:

- `foo`, `bar`, `baz`
- Animal examples
- Student examples
- Toy examples
- Overly clever one-liners

## Domain Examples

Prefer examples from:

- Banking
- Payments
- Insurance
- Retail
- E-commerce
- Supply chain
- Identity and access management
- Workflow platforms
- Notification systems
- Sustainability platforms

## Diagrams

Use ASCII diagrams in Markdown.

Do not depend on external images for core understanding.

## Tables

Use tables for:

- Comparison
- Complexity
- Selection guide
- Pros and cons
- Memory and performance analysis
- Production trade-offs
