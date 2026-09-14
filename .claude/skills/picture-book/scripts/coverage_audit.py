#!/usr/bin/env python3
"""Coverage audit: how many reference terms of a field are covered by the pages (titles, h1, summary, glossary).

Usage:
    python3 coverage_audit.py --category security --ref references.txt [--threshold 90]

references.txt: one term per line (English, lower-case; `|` separates accepted spellings, e.g. "pentest|penetration test").
A term counts as covered when any spelling appears in the page text of that category. Exit 1 if below threshold.
Use it as the stop condition of the loop: audit -> write the missing terms -> audit again.
"""
import argparse, glob, importlib.util, os, sys


def page_text(category):
    sys.path.insert(0, "terms"); sys.path.insert(0, f"terms/{category}"); out = []  # 분야 전용 _world.py
    for f in glob.glob(f"terms/{category}/[!_]*.py"):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); P = m.PAGE
        out.append(" ".join([P["h1"][1], P["title"][1], P["summary"][1][1]] + [g[1] + " " + g[2][1] + " " + g[3][1] for g in P["glossary"]]))
    return " ".join(out).lower()


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--category", default="security")
    ap.add_argument("--ref", required=True); ap.add_argument("--threshold", type=float, default=90.0)
    a = ap.parse_args()
    text = page_text(a.category)
    refs = [l.strip() for l in open(a.ref) if l.strip() and not l.startswith("#")]
    missing = [r for r in refs if not any(alt.strip().lower() in text for alt in r.split("|"))]
    pct = (len(refs) - len(missing)) / len(refs) * 100
    print(f"{len(refs)} reference terms; {len(refs) - len(missing)} covered; {pct:.1f}%")
    print("missing:", missing)
    sys.exit(0 if pct >= a.threshold else 1)


if __name__ == "__main__":
    main()
