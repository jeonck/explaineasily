#!/usr/bin/env python3
"""Append rows for terms missing from README.md and the ELI5 skill table, after the last row of that category.

Usage:
    python3 update_tables.py [--category security] [--skill .claude/skills/eli5/SKILL.md]

README row:  | <English name> | <ko title> | [slug-ko](docs/slug-ko.html) | [slug-en](docs/slug-en.html) |
SKILL row:   | <category> | <English name> | <ko title> |
The English name is derived from h1 ("What is a <em>Pentest</em>?" -> "Pentest"). Idempotent: existing rows are kept.
If the category has no rows yet, the rows are appended after the last table row of the file — move them by hand.
"""
import argparse, glob, importlib.util, os, re, sys


def load(category):
    sys.path.insert(0, "terms"); sys.path.insert(0, f"terms/{category}"); terms = []  # 분야 전용 _world.py
    for f in glob.glob(f"terms/{category}/[!_]*.py"):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); terms.append(m.PAGE)
    return sorted(terms, key=lambda p: p["order"])


def en_name(p):
    h = re.sub(r"<[^>]+>", "", p["h1"][1])
    return re.sub(r"^What (is|are) (a |an |the )?", "", h).rstrip("?").strip()


def insert_after_last(s, row_pat, rows):
    last = list(re.finditer(row_pat, s, re.M))
    if not last: return s + "\n" + rows
    end = last[-1].end(); return s[:end] + rows + s[end:]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--category", default="security")
    ap.add_argument("--skill", default=".claude/skills/eli5/SKILL.md"); a = ap.parse_args()
    terms = load(a.category)
    # README
    s = open("README.md").read()
    have = set(re.findall(r"\[([a-z0-9]+)-ko\]\(docs/", s))
    new = [p for p in terms if p["slug"] not in have]
    rows = "".join(f"| {en_name(p)} | {p['title'][0]} | [{p['slug']}-ko](docs/{p['slug']}-ko.html) | [{p['slug']}-en](docs/{p['slug']}-en.html) |\n" for p in new)
    cat_slugs = {p["slug"] for p in terms}
    pat = r"^\| .*\[(%s)-ko\]\(docs/.*\|\n" % "|".join(map(re.escape, cat_slugs & have)) if cat_slugs & have else r"^\| .*\[[a-z0-9]+-ko\]\(docs/.*\|\n"
    if new: open("README.md", "w").write(insert_after_last(s, pat, rows))
    print("README +", [p["slug"] for p in new])
    # SKILL table
    if os.path.exists(a.skill):
        s = open(a.skill).read()
        new2 = [t for t in terms if t["title"][0] not in s]
        rows = "".join(f"| {a.category} | {en_name(t)} | {t['title'][0]} |\n" for t in new2)
        if new2: open(a.skill, "w").write(insert_after_last(s, r"^\| %s \| .*\|\n" % re.escape(a.category), rows))
        print("SKILL +", [t["slug"] for t in new2])


if __name__ == "__main__":
    main()
