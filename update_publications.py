#!/usr/bin/env python3
"""Fetch publications from arXiv and update profile.md."""

import re
import urllib.request
import xml.etree.ElementTree as ET

ARXIV_FEED = "https://arxiv.org/a/hirai_y_1.atom2"
PROFILE_PATH = "content/profile.md"
NS = {"atom": "http://www.w3.org/2005/Atom"}


def clean_latex(text):
    """Convert common LaTeX markup to plain Unicode."""
    text = re.sub(r"\\boldsymbol\{([^}]*)\}", r"\1", text)
    text = text.replace("\\times", "\u00d7")
    text = re.sub(r"(?<!\\)\$", "", text)
    text = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", text)
    return text.strip()


def fetch_papers():
    with urllib.request.urlopen(ARXIV_FEED) as resp:
        tree = ET.parse(resp)

    entries = tree.findall(".//atom:entry", NS)
    papers = []
    for entry in entries:
        title = clean_latex(" ".join(entry.find("atom:title", NS).text.split()))
        link = entry.find("atom:link[@rel='alternate']", NS)
        url = link.get("href") if link is not None else entry.find("atom:id", NS).text.strip()
        published = entry.find("atom:published", NS).text.strip()
        year = published[:4]
        authors = [
            n.text.strip()
            for n in entry.findall("atom:author/atom:name", NS)
        ]
        papers.append((title, url, authors, year))
    return papers


def format_markdown(papers):
    lines = []
    for title, url, authors, year in papers:
        author_str = ", ".join(authors)
        lines.append(f'- ["{title}"]({url}) — {author_str} ({year})')
    return "\n\n".join(lines)


if __name__ == "__main__":
    papers = fetch_papers()
    md = format_markdown(papers)

    with open(PROFILE_PATH, "r") as f:
        content = f.read()

    pattern = r"(<!-- ARXIV_START -->\n).*?(<!-- ARXIV_END -->)"
    updated = re.sub(pattern, rf"\g<1>{md}\n\g<2>", content, flags=re.DOTALL)

    with open(PROFILE_PATH, "w") as f:
        f.write(updated)

    print(f"Updated {PROFILE_PATH} with {len(papers)} paper(s).")
