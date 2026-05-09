import re

with open('index.html', 'r') as f:
    html = f.read()

# Replace all shareCardTarget CSS with new clean version
new_css = """  #shareCardTarget{position:fixed;left:-9999px;top:0;width:1080px;background:#f5efe3;padding:70px;font-family:'DM Serif Display',serif;color:#1a1208;display:flex;flex-direction:column;box-sizing:border-box}
  #shareCardTarget .sc-brand{font-family:'Bebas Neue',sans-serif;font-size:1.8rem;letter-spacing:.04em;padding-bottom:0.5rem;border-bottom:3px solid #1a1208;display:flex;justify-content:space-between;align-items:baseline;margin-bottom:1.2rem;flex-shrink:0}
  #shareCardTarget .sc-brand span{color:#d4421a}
  #shareCardTarget .sc-brand small{font-family:'DM Mono',monospace;font-size:.85rem;color:#7a6f5e;letter-spacing:.1em}
  #shareCardTarget .sc-word{font-family:'Bebas Neue',sans-serif;font-size:8rem;letter-spacing:.02em;line-height:1;margin-bottom:0.3rem;flex-shrink:0}
  #shareCardTarget .sc-meta{font-family:'DM Mono',monospace;font-size:1.8rem;color:#c9952a;margin-bottom:1rem;display:flex;gap:1rem;align-items:baseline;flex-shrink:0}
  #shareCardTarget .sc-meta .pos{color:#7a6f5e;font-style:italic;font-family:'DM Serif Display',serif;font-size:1.6rem}
  #shareCardTarget .sc-rule-gold{border:none;border-top:2px solid #c9952a;margin:0 0 1rem;flex-shrink:0}
  #shareCardTarget .sc-etymology{font-family:'DM Mono',monospace;font-size:1.3rem;color:#7a6f5e;border-left:4px solid #c9952a;padding-left:0.8rem;margin-bottom:1rem;line-height:1.4;flex-shrink:0}
  #shareCardTarget .sc-rule-gold2{border:none;border-top:2px solid #c9952a;margin:0 0 1.2rem;flex-shrink:0}
  #shareCardTarget .sc-definition{font-size:2.8rem;line-height:1.4;font-weight:bold;color:#1a1208;margin-bottom:1.2rem;flex-shrink:0}
  #shareCardTarget .sc-rule-ink{border:none;border-top:1px solid #1a1208;opacity:0.2;margin:0 0 1rem;flex-shrink:0}
  #shareCardTarget .sc-example{font-style:italic;font-size:2.2rem;color:#7a6f5e;line-height:1.5;flex-shrink:0}
  #shareCardTarget .sc-footer{display:none}"""

html = re.sub(
    r'  #shareCardTarget\{.*?#shareCardTarget \.sc-footer\{[^\n]+\}',
    new_css,
    html,
    flags=re.DOTALL
)

# Update share card HTML to add rule elements
old_html = '''<div id="shareCardTarget">
  <div class="sc-brand">WORD<span>GUNK</span><small>wordgunk.com</small></div>
  <div class="sc-word" id="sc-word"></div>
  <div class="sc-meta"><span class="pos" id="sc-pos"></span><span id="sc-pronunciation"></span></div>
  <div class="sc-etymology" id="sc-etymology"></div>
  <div class="sc-definition" id="sc-definition"></div>
  <div class="sc-example" id="sc-example"></div>
  <div class="sc-footer">wordgunk.com - New words for a broken world</div>
</div>'''

new_html = '''<div id="shareCardTarget">
  <div class="sc-brand">WORD<span>GUNK</span><small>wordgunk.com</small></div>
  <div class="sc-word" id="sc-word"></div>
  <div class="sc-meta"><span class="pos" id="sc-pos"></span><span id="sc-pronunciation"></span></div>
  <hr class="sc-rule-gold">
  <div class="sc-etymology" id="sc-etymology"></div>
  <hr class="sc-rule-gold2">
  <div class="sc-definition" id="sc-definition"></div>
  <hr class="sc-rule-ink">
  <div class="sc-example" id="sc-example"></div>
  <div class="sc-footer"></div>
</div>'''

html = html.replace(old_html, new_html)

with open('index.html', 'w') as f:
    f.write(html)

print("Done! Share card rebuilt with rule lines and top-aligned layout.")
