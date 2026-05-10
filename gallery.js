var galleryOffset=0,galleryLoaded=false;
async function loadGallery(){
  if(galleryLoaded)return;
  document.getElementById('galleryLoading').style.display='block';
  try{
    var res=await fetch('/api/get-words?limit=50&offset=0');
    var words=await res.json();
    galleryOffset=words.length;
    renderGallery(words,false);
    document.getElementById('loadMoreBtn').style.display=words.length===50?'block':'none';
    galleryLoaded=true;
  }catch(e){console.error(e);}
  finally{document.getElementById('galleryLoading').style.display='none';}
}
async function loadMore(){
  try{
    var res=await fetch('/api/get-words?limit=50&offset='+galleryOffset);
    var words=await res.json();
    galleryOffset+=words.length;
    renderGallery(words,true);
    document.getElementById('loadMoreBtn').style.display=words.length===50?'block':'none';
  }catch(e){console.error(e);}
}
function renderGallery(words,append){
  var grid=document.getElementById('galleryGrid');
  var html=words.map(function(w,i){
    return '<div class="archive-card" style="animation-delay:'+(i*0.04)+'s"><div class="word-main"><div class="word-title">'+w.word+'</div><div class="word-pos">'+w.pos+'</div></div><div class="word-definition">'+w.definition+'</div></div>';
  }).join('');
  if(append)grid.innerHTML+=html;else grid.innerHTML=html;
}


