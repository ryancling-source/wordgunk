import re

with open('index.html', 'r') as f:
    html = f.read()

# Define the three themes as a JS variable to inject
themes_js = """var wcThemes={
  cream:{bg:'#f5efe3',text:'#1a1208',muted:'#7a6f5e',gold:'#c9952a',brand:'#1a1208',brandAccent:'#d4421a',rule:'#c9952a',ruleInk:'#1a1208',url:'#7a6f5e',canvasBg:'#f5efe3'},
  ink:{bg:'#1a1208',text:'#f5efe3',muted:'#ede5d0',gold:'#c9952a',brand:'#f5efe3',brandAccent:'#d4421a',rule:'#c9952a',ruleInk:'#f5efe3',url:'#7a6f5e',canvasBg:'#1a1208'},
  red:{bg:'#d4421a',text:'#1a1208',muted:'#ede5d0',gold:'#c9952a',brand:'#f5efe3',brandAccent:'#f5efe3',rule:'#c9952a',ruleInk:'#1a1208',url:'#ede5d0',canvasBg:'#d4421a'}
};
var wcCurrentTheme='cream';

function applyTheme(key){
  wcCurrentTheme=key;
  var t=wcThemes[key];
  var sc=document.getElementById('shareCardTarget');
  sc.style.background=t.bg;
  sc.querySelectorAll('.sc-word,.sc-definition').forEach(function(el){el.style.color=t.text;});
  sc.querySelectorAll('.sc-meta').forEach(function(el){el.style.color=t.gold;});
  sc.querySelectorAll('.sc-etymology,.sc-example').forEach(function(el){el.style.color=t.muted;});
  sc.querySelectorAll('.sc-brand').forEach(function(el){el.style.borderBottomColor=t.text;el.style.color=t.brand;});
  sc.querySelectorAll('.sc-brand span').forEach(function(el){el.style.color=t.brandAccent;});
  sc.querySelectorAll('.sc-brand small').forEach(function(el){el.style.color=t.url;});
  sc.querySelectorAll('.sc-rule-gold,.sc-rule-gold2').forEach(function(el){el.style.borderTopColor=t.rule;});
  sc.querySelectorAll('.sc-rule-ink').forEach(function(el){el.style.borderTopColor=t.ruleInk;});
  sc.querySelectorAll('.sc-etymology').forEach(function(el){el.style.borderLeftColor=t.rule;});
  document.querySelectorAll('.wc-swatch').forEach(function(s){
    s.style.boxShadow=s.dataset.theme===key?'0 0 0 2px #fff, 0 0 0 4px '+t.bg:'none';
    s.style.transform=s.dataset.theme===key?'scale(1.2)':'scale(1)';
  });
}

async function regenerateCard(){
  var t=wcThemes[wcCurrentTheme];
  var cardEl=document.getElementById('shareCardTarget');
  var cardHeight=Math.max(cardEl.scrollHeight,1080);
  var canvas=await html2canvas(cardEl,{scale:1,useCORS:true,backgroundColor:t.canvasBg,logging:false,width:1080,height:cardHeight});
  shareCardDataUrl=canvas.toDataURL('image/png');
  document.getElementById('sharePreviewImg').src=shareCardDataUrl;
}"""

# Inject themes JS before the switchTab function
html = html.replace('function switchTab(name,el){', themes_js + '\nfunction switchTab(name,el){')

# Update shareCurrentWord to apply cream theme by default and generate card
old_share_start = "document.getElementById('sc-word').textContent=currentWord.word;"
new_share_start = """applyTheme('cream');
  document.getElementById('sc-word').textContent=currentWord.word;"""
html = html.replace(old_share_start, new_share_start)

# Update html2canvas call to use theme
old_canvas = "var canvas=await html2canvas(document.getElementById('shareCardTarget'),{scale:1,useCORS:true,backgroundColor:'#f5efe3',logging:false,width:1080,height:cardHeight});"
new_canvas = "var t=wcThemes[wcCurrentTheme];var canvas=await html2canvas(document.getElementById('shareCardTarget'),{scale:1,useCORS:true,backgroundColor:t.canvasBg,logging:false,width:1080,height:cardHeight});"
html = html.replace(old_canvas, new_canvas)

# Add color swatch UI to share modal - insert before save button
old_save_btn = '<button class="btn btn-accent" id="saveBtn" onclick="saveCard()">Save Image</button>'
new_save_btn = """<div style="display:flex;gap:12px;align-items:center;margin-bottom:1rem">
    <span style="font-family:\'DM Mono\',monospace;font-size:0.6rem;letter-spacing:0.15em;text-transform:uppercase;color:var(--muted)">Colorway</span>
    <button class="wc-swatch" data-theme="cream" onclick="applyTheme(\'cream\');regenerateCard()" style="width:28px;height:28px;border-radius:50%;background:#f5efe3;border:2px solid #1a1208;cursor:pointer;transition:all 0.15s;box-shadow:0 0 0 2px #fff, 0 0 0 4px #f5efe3"></button>
    <button class="wc-swatch" data-theme="ink" onclick="applyTheme(\'ink\');regenerateCard()" style="width:28px;height:28px;border-radius:50%;background:#1a1208;border:2px solid #1a1208;cursor:pointer;transition:all 0.15s"></button>
    <button class="wc-swatch" data-theme="red" onclick="applyTheme(\'red\');regenerateCard()" style="width:28px;height:28px;border-radius:50%;background:#d4421a;border:2px solid #d4421a;cursor:pointer;transition:all 0.15s"></button>
  </div>
  <button class="btn btn-accent" id="saveBtn" onclick="saveCard()">Save Image</button>"""
html = html.replace(old_save_btn, new_save_btn)

with open('index.html', 'w') as f:
    f.write(html)

print("Done! Color swatches added to share modal.")
