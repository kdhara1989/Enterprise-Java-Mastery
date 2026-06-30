from pathlib import Path

root = Path(__file__).resolve().parents[1]
output = root / "book.md"

files = []
files.extend(sorted((root / "front-matter").glob("*.md")))

for volume in ["volume-1", "volume-2", "volume-3"]:
    for part in sorted((root / volume).glob("part-*")):
        files.extend(sorted(part.glob("*.md")))

with output.open("w", encoding="utf-8") as out:
    for file in files:
        if file.name == "README.md":
            continue
        out.write(file.read_text(encoding="utf-8"))
        out.write("\n\n---\n\n")

print(f"Generated {output}")
