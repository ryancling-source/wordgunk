import re

with open('index.html', 'r') as f:
    html = f.read()

# Fix cream theme on red - all cream, no gold conflicts
old_red = "{bg:'#d4421a',text:'#1a1208',muted:'#ede5d0',gold:'#c9952a',brand:'#f5efe3',brandAccent:'#f5efe3',rule:'#c9952a',ruleInk:'#1a1208',url:'#ede5d0',canvasBg:'#d4421a'}"
new_red = "{bg:'#d4421a',text:'#f5efe3',muted:'#f5efe3',gold:'#f5efe3',brand:'#f5efe3',brandAccent:'#f5efe3',rule:'#f5efe3',ruleInk:'#f5efe3',url:'#ede5d0',canvasBg:'#d4421a'}"
html = html.replace(old_red, new_red)

# Fix ink theme - etymology border left color should be gold not split
# The issue is sc-etymology has both color and border-left-color set
# Make sure gold applies to both pronunciation AND etymology border on ink
old_ink = "{bg:'#1a1208',text:'#f5efe3',muted:'#ede5d0',gold:'#c9952a',brand:'#f5efe3',brandAccent:'#d4421a',rule:'#c9952a',ruleInk:'#f5efe3',url:'#7a6f5e',canvasBg:'#1a1208'}"
new_ink = "{bg:'#1a1208',text:'#f5efe3',muted:'#c9952a',gold:'#c9952a',brand:'#f5efe3',brandAccent:'#d4421a',rule:'#c9952a',ruleInk:'#f5efe3',url:'#7a6f5e',canvasBg:'#1a1208'}"
html = html.replace(old_ink, new_ink)

with open('index.html', 'w') as f:
    f.write(html)

print("Done! Red fixed to all cream, ink etymology fixed to all gold.")
