# Enterprise Java Mastery – Naming Conventions

## Repository Folders

Use lowercase kebab-case.

Examples:

```text
volume-1/
part-01-enterprise-java-collections/
```

## Chapter Files

Use two-digit sequence numbers and lowercase kebab-case.

Examples:

```text
01-collections-framework-overview.md
02-collection-interface.md
03-list-interface.md
04-set-interface.md
```

## Volume Numbering

Use decimal chapter numbering inside content.

Examples:

```text
# 1.1 Collections Framework Overview
# 1.2 Collection Interface
# 1.3 List Interface
```

## Figures

Figures are numbered sequentially within Volume I.

Format:

```text
Figure 1.001 – Title
```

## Tables

Tables are numbered sequentially within Volume I.

Format:

```text
Table 1.001 – Title
```

## Listings

Code listings are numbered sequentially within Volume I.

Format:

```text
Listing 1.001 – Title
```

## Code Packages

Use enterprise-style packages.

Examples:

```java
package com.enterprise.collections;
package com.enterprise.payments;
package com.enterprise.banking;
package com.enterprise.identity;
```

## Git Commit Messages

Use conventional commit style.

Examples:

```text
feat(volume-1): add set interface chapter
docs: update progress tracker
chore: initialize book repository
fix: correct table numbering in collection interface chapter
```
