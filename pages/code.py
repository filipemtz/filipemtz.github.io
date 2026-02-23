from __future__ import annotations

import enum
import os
import shutil
from typing import Dict, List, Optional

from bs4 import BeautifulSoup


def extract_papers(html: str) -> List[Dict]:
    soup = BeautifulSoup(html, "html.parser")

    papers: List[Dict] = []
    current_year: Optional[int] = None

    # Traverse in document order to correctly associate year with papers
    for element in soup.find_all(["h2", "div"]):
        # Detect year headers
        if element.name == "h2" and "paper-year" in element.get("class", []):
            year_text = element.get_text(strip=True)
            if year_text.isdigit():
                current_year = int(year_text)
            continue

        # Detect paper blocks
        if element.name == "div" and "paper" in element.get("class", []):
            if current_year is None:
                # Skip malformed entries without year context
                continue

            # --- Title and link ---
            title_div = element.find("div", class_="paper-title")
            if title_div is None:
                continue

            link_tag = title_div.find("a")
            if link_tag:
                title = link_tag.get_text(strip=True)
                link = link_tag.get("href")
            else:
                title = title_div.get_text(strip=True)
                link = None

            # --- Authors ---
            authors_div = element.find("div", class_="paper-authors")
            authors: List[str] = []
            if authors_div:
                author_tags = authors_div.find_all("div", class_="paper-author")
                for author_tag in author_tags:
                    name = author_tag.get_text(strip=True)
                    if name:
                        authors.append(name)

            # --- Venue ---
            venue_div = element.find("div", class_="paper-publication")
            venue = venue_div.get_text(strip=True) if venue_div else ""

            papers.append(
                {
                    "title": title,
                    "authors": authors,
                    "year": current_year,
                    "link": link,
                    "venue": venue,
                }
            )

    return papers


import re
import unicodedata


def limpar_texto(texto):
    # 1. Remover acentos (normalização NFD)
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join([c for c in texto if not unicodedata.combining(c)])

    # 2. Remover símbolos não alfabéticos (mantém letras e espaços, se desejar)
    # ^\w é tudo que NÃO é letra, número ou underline
    # \s mantém espaços, remova se não quiser espaços
    texto = re.sub(r"[^\w\s]", " ", texto)
    texto = texto.replace(" ", "-")

    return texto


if __name__ == "__main__":
    with open("publications-old.qmd", "r", encoding="utf-8") as f:
        html_content = f.read()

    extracted = extract_papers(html_content)

    for count, paper in enumerate(extracted):
        title = paper["title"].replace("\n", " ")
        year = paper["year"]
        link = paper["link"]
        authors = "[" + ",".join([f'"{a}"' for a in paper["authors"]]) + "]"
        venue = paper["venue"].replace("\n", " ")

        first_author = paper["authors"][0].split()[-1]
        mini_title = "-".join(title.split()[:4])
        paper_dir = limpar_texto(f"{year}_{first_author}_{mini_title}".lower())
        print(paper_dir)

        header = f"""---
title: \"{title}\"
date: {year}-01-01
author: {authors}
publication: \"{venue}\"
categories: []
url_source: \"{link}\"
url_preprint:
journ: \"{venue}\"
year: {year}
---
        """

        if link:
            header += f"""
[Check out the paper!]({link})
            """
        else:
            header += """
Link to the paper is coming soon.
            """

        os.makedirs(os.path.join("publications", paper_dir), exist_ok=True)
        with open(
            os.path.join("publications", paper_dir, "index.qmd"), "w", encoding="utf-8"
        ) as f:
            f.write(header)
