content = open('index.html').read()

content = content.replace('grid-template-columns:1fr 1fr', 'grid-template-columns:1fr 1fr 1fr')

content = content.replace(
    "onclick=\"switchTab('coin',this)\">&#9997; Coin a Word</button>",
    "onclick=\"switchTab('coin',this)\">&#9997; Coin a Word</button><button class=\"tab\" onclick=\"switchTab('gallery',this);loadGallery()\">&#128218; Gallery</button>"
)

panel = '<div class="panel" id="panel-gallery"><div class="archive-header">The Full Dictionary</div><div class="loading-state" id="galleryLoading">LOADING <span class="loading-dots"></span></div><div class="archive-grid" id="galleryGrid"></div><button class="btn btn-outline" id="loadMoreBtn" onclick="loadMore()" style="margin-top:1rem;display:none">Load More</button></div>'

content = content.replace('</div>\n<div class="share-modal"', panel + '\n</div>\n<div class="share-modal"')

js = open('gallery.js').read()
content = content.replace("window.addEventListener('load',", js + "window.addEventListener('load',")

open('index.html', 'w').write(content)
print('Done!')
