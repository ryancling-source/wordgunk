import re

with open('index.html', 'r') as f:
    html = f.read()

# New share card CSS - tight, clean, 1080x1350
new_css = """  #shareCardTarget{position:fixed;left:-9999px;top:0;width:1080px;height:1350px;background:var(--cream);padding:70px;font-family:'DM Serif Display',serif;color:var(--ink);display:flex;flex-direction:column;justify-content:flex-start;gap:0}
  #shareCardTarget .sc-brand{font-family:'Bebas Neue',sans-serif;font-size:1.8rem;letter-spacing:.04em;margin-bottom:0.6rem;padding-bottom:0.5rem;border-bottom:3px solid var(--ink);display:flex;justify-content:space-between;align-items:baseline}
  #shareCardTarget .sc-brand span{color:var(--accent)}
  #shareCardTarget .sc-brand small{font-family:'DM Mono',monospace;font-size:.85rem;color:var(--muted);letter-spacing:.1em}
  #shareCardTarget .sc-word{font-family:'Bebas Neue',sans-serif;font-size:8rem;letter-spacing:.02em;line-height:1;margin-bottom:0.3rem;margin-top:0.5rem}
  #shareCardTarget .sc-meta{font-family:'DM Mono',monospace;font-size:1.6rem;color:var(--gold);margin-bottom:0.4rem;display:flex;gap:1rem;align-items:baseline}
  #shareCardTarget .sc-meta .pos{color:var(--muted);font-style:italic;font-family:'DM Serif Display',serif;font-size:1.4rem}
  #shareCardTarget .sc-etymology{font-family:'DM Mono',monospace;font-size:1.3rem;color:var(--muted);border-left:4px solid var(--gold);padding-left:0.8rem;margin-bottom:0.8rem;line-height:1.4}
  #shareCardTarget .sc-definition{font-size:2.8rem;line-height:1.35;margin-bottom:0.8rem;font-weight:bold}
  #shareCardTarget .sc-example{font-style:italic;font-size:2rem;color:var(--muted);border-left:4px solid var(--ink);padding-left:1rem;line-height:1.4;margin-bottom:0}
  #shareCardTarget .sc-footer{font-family:'DM Mono',monospace;font-size:.9rem;color:var(--muted);letter-spacing:.1em;border-top:2px solid var(--ink);padding-top:0.8rem;margin-top:auto}"""

# Replace all existing shareCardTarget CSS lines
html = re.sub(r'  #shareCardTarget\{.*?\n  #shareCardTarget \.sc-footer\{[^\n]+\}', new_css, html, flags=re.DOTALL)

# Fix canvas dimensions
html = re.sub(r'width:\d+,height:\d+', 'width:1080,height:1350', html)

# Clean up any windowWidth/windowHeight duplicates
html = re.sub(r',windowWidth:\d+,windowHeight:\d+', '', html)

with open('index.html', 'w') as f:
    f.write(html)

print("Done! Share card CSS updated.")
