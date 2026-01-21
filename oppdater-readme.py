import json
from pathlib import Path
from collections import defaultdict
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("oppgaver.json","r",encoding="utf-8") as f:
    oppgaveinfo = json.load(f)

PROBLEM_URL = "https://projecteuler.net/problem={nr}"

def emoji_til(vanskgrad):
    prosentpoeng = int(vanskgrad.removesuffix("%"))
    if prosentpoeng in (5,10): return "🟩"
    if prosentpoeng in (15,20): return "🟨"
    if prosentpoeng in (25,30): return "🟧"
    if prosentpoeng in (35,40): return "🟥"
    if prosentpoeng in (45,50): return "🟫"
    return "⬛"

løsningsfiler = {p.stem: p for p in Path("losninger 1-100").iterdir()}

with open("README.md", "w", encoding="utf-8") as f:
    f.write("# Project Euler\n\n")

    f.write(f"Tilsammen **{len(løsningsfiler)}** oppgaver løst.\n\n") 
    f.write(f"Av hensyn til Project Eulers retningslinjer er løsninger fra og med problem 101 holdt private.\n\n") 

    prosentgruppert = defaultdict(list)

    for løst in sorted(løsningsfiler, key=lambda x: int(x.split("-")[0])):
        nr,_ = løst.split("-")
        f.write(emoji_til(oppgaveinfo[nr]["vanskelighetsgrad"])) 

        prosentgruppert[int(oppgaveinfo[nr]["vanskelighetsgrad"].removesuffix("%"))].append(løst)

    f.write("\n\n")
    
    for emoji,prosentgruppe in zip("🟩🟨🟧🟥🟫⬛", ((5,10), (15,20), (25,30), (35,40), (45,50), (55,60,65,70,75,80,85,90,95,100))):
        f.write(f"<details>\n") 
        f.write(f"\t<summary>\n") 
        f.write(f"\t\t{emoji} <strong>{f'{prosentgruppe[0]}+' if len(prosentgruppe) > 2 else f'{prosentgruppe[0]}-{prosentgruppe[1]}'} %</strong> – løst {sum(len(prosentgruppert[prosent]) for prosent in prosentgruppe)}\n") 
        f.write(f"\t</summary>\n") 

        f.write("\t<table>\n")
        for prosent in prosentgruppe:
            for løst in prosentgruppert[prosent]:
                nr,tittel = løst.split("-")
                f.write(f"\t\t\t<tr>\n") 
                f.write(f"\t\t\t\t<td>{nr}</td>\n")
                f.write(f'''\t\t\t\t<td>\n\t\t\t\t\t<a href="{PROBLEM_URL.replace('{nr}', nr)}">{tittel}</td>\n''')
                f.write(f'\t\t\t\t<td>{oppgaveinfo[nr]["vanskelighetsgrad"]}</td>\n')
                f.write(f'''\t\t\t\t<td><a href="{løsningsfiler[løst]}">🔍</a></td>\n''')
                f.write("\t\t\t</tr>\n")
        f.write("\t</table>\n")
        f.write("</details>\n\n")
    




