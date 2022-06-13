import sys

EXT_PATH = sys.argv[1]

with open(EXT_PATH + '/background.js', 'r') as f:
    bgJSContent = f.read()

bgJSContent_patched = bgJSContent.replace(
    'function setChromePasswordSavingEnabled(e){',
    'function setChromePasswordSavingEnabled(e){ return;'
)

assert bgJSContent_patched != bgJSContent

with open(EXT_PATH + '/background.js', 'w') as f:
    f.write(bgJSContent_patched)
