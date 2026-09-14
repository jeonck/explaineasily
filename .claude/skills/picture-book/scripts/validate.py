#!/usr/bin/env python3
"""Build + validate picture-book term pages.

Usage:
    python3 validate.py [--category security] [--slugs a b c] [--strict]

Checks:
  1. `python3 -W error build.py` passes (any SyntaxWarning fails the build).
  2. Every <svg> in docs/*.html parses as XML; every internal href exists; no ⟦ ⟧ placeholders remain.
  3. PAGE structure of terms/<category>/*.py: 5 panels, exactly one hero with 4 tricks, 8 glossary rows,
     (ko, en) tuples everywhere, unique `order` within the category, slug == filename.
     Structure problems are warnings unless --strict (older pages may use looser formats).
"""
import argparse, glob, importlib.util, os, re, subprocess, sys
import xml.dom.minidom


def build():
    r = subprocess.run([sys.executable, "-W", "error", "build.py"], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-2000:], r.stderr[-4000:]); sys.exit("build failed")
    print("build ok")


def check_docs():
    n = 0
    for f in sorted(glob.glob("docs/*.html")):
        s = open(f).read()
        for m in re.finditer(r"<svg.*?</svg>", s, re.S):
            xml.dom.minidom.parseString(m.group(0)); n += 1
        for href in re.findall(r'href="([a-z0-9\-]+\.html)"', s):
            assert os.path.exists("docs/" + href), (f, href)
        assert "⟦" not in s, f"placeholder left in {f}"
    print("docs ok:", n, "svgs")


def check_pages(category, slugs, strict):
    sys.path.insert(0, "terms")
    files = [f"terms/{category}/{s}.py" for s in slugs] if slugs else sorted(glob.glob(f"terms/{category}/[!_]*.py"))
    bad, orders = [], {}
    for f in files:
        name = os.path.basename(f)[:-3]
        spec = importlib.util.spec_from_file_location(name, f)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); P = m.PAGE
        if P["slug"] != name: bad.append((f, "slug != filename"))
        if len(P["panels"]) != 5: bad.append((f, f"panels={len(P['panels'])}"))
        heroes = [p for p in P["panels"] if p.get("hero")]
        if len(heroes) != 1 or "tricks" not in heroes[0] or len(heroes[0]["tricks"][1]) != 4: bad.append((f, "hero/tricks"))
        if len(P["glossary"]) != 8: bad.append((f, f"glossary={len(P['glossary'])}"))
        for k in ("title", "h1", "sub"):
            if not (isinstance(P[k], tuple) and len(P[k]) == 2): bad.append((f, k))
        for p in P["panels"]:
            for k in ("alt", "caption", "small"):
                if not (isinstance(p.get(k), tuple) and len(p[k]) == 2): bad.append((f, k))
        orders.setdefault(P["order"], []).append(P["slug"])
    dups = {k: v for k, v in orders.items() if len(v) > 1}
    if dups: bad.append(("order collision", dups))
    print(f"pages checked: {len(files)}; structure issues: {len(bad)}")
    for b in bad: print("  -", b)
    if bad and strict: sys.exit(1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--category", default="security"); ap.add_argument("--slugs", nargs="*")
    ap.add_argument("--strict", action="store_true"); a = ap.parse_args()
    build(); check_docs(); check_pages(a.category, a.slugs, a.strict)
