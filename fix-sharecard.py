import re

with open('index.html', 'r') as f:
    html = f.read()

# Fix shareCardTarget container
old = "width:1080px;height:1350px;background:var(--cream);padding:70px;font-family:'DM Serif Display',serif;color:var(--ink);display:flex;flex-direction:column;justify-content:flex-start;gap:0}"
new = "width:1080px;min-height:1080px;max-height:1350px;overflow:hidden;background:var(--cream);padding:70px;font-family:'DM Serif Display',serif;color:var(--ink);display:block}"
html = html.replace(old, new)

# Tighter brand header
html = html.replace(
    "font-size:1.8rem;letter-spacing:.04em;margin-bottom:0.6rem;padding-bottom:0.5rem;border-bottom:3px solid var(--ink);display:flex;justify-content:space-between;align-items:baseline}",
    "font-size:1.8rem;letter-spacing:.04em;margin-bottom:1rem;padding-bottom:0.5rem;border-bottom:3px solid var(--ink);display:flex;justify-content:space-between;align-items:baseline}"
)

# Word - good size, small gap below
html = html.replace(
    "font-size:8rem;letter-spacing:.02em;line-height:1;margin-bottom:0.3rem;margin-top:0.5rem}",
    "font-size:8rem;letter-spacing:.02em;line-height:1;margin-bottom:0.4rem;margin-top:0.3rem}"
)

# Meta - pronunciation, tighter
html = html.replace(
    "font-size:1.6rem;color:var(--gold);margin-bottom:0.4rem;display:flex;gap:1rem;align-items:baseline}",
    "font-size:1.6rem;color:var(--gold);margin-bottom:0.8rem;display:flex;gap:1rem;align-items:baseline}"
)

# Etymology - more breathing room below
html = html.replace(
    "font-size:1.3rem;color:var(--muted);border-left:4px solid var(--gold);padding-left:0.8rem;margin-bottom:0.8rem;line-height:1.4}",
    "font-size:1.3rem;color:var(--muted);border-left:4px solid var(--gold);padding-left:0.8rem;margin-bottom:1.8rem;line-height:1.4}"
)

# Definition - more space below
html = html.replace(
    "font-size:2.8rem;line-height:1.35;margin-bottom:0.8rem;font-weight:bold}",
    "font-size:2.8rem;line-height:1.35;margin-bottom:1.5rem;font-weight:bold}"
)

# Example - good spacing
html = html.replace(
    "font-style:italic;font-size:2rem;color:var(--muted);border-left:4px solid var(--ink);padding-left:1rem;line-height:1.4;margin-bottom:0}",
    "font-style:italic;font-size:2rem;color:var(--muted);border-left:4px solid var(--ink);padding-left:1rem;line-height:1.4;margin-bottom:0}"
)

# Hide footer completely
html = html.replace(
    "font-family:'DM Mono',monospace;font-size:.9rem;color:var(--muted);letter-spacing:.1em;border-top:2px solid var(--ink);padding-top:0.8rem;margin-top:auto}",
    "display:none}"
)

# Fix canvas dimensions
html = re.sub(r'width:1080(?:,height:\d+)?(?=\})', 'width:1080,height:1350', html)

# Remove truncation calls
html = html.replace('word=truncateWord(word);displayWord(word)', 'displayWord(word)')
html = html.replace('word=truncateWord(word);word.humanCoined', 'word.humanCoined')

with open('index.html', 'w') as f:
    f.write(html)

print("Done! Breathing room added, footer removed.")
