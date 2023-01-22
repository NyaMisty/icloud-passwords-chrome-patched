import sys

EXT_PATH = sys.argv[1]

with open(EXT_PATH + '/background.js', 'r') as f:
    bgJSContent = f.read()

bgJSContent_patched = bgJSContent


# old
bgJSContent_patched = bgJSContent_patched.replace(
    'function setChromePasswordSavingEnabled(e){',
    'function setChromePasswordSavingEnabled(e){ return;'
)

# new
import re
def replaceSetter1(text, propname):
    return re.sub(r'this\.[^()]+?\(%s,!1\)' % (propname), r'null', text)

bgJSContent_patched = replaceSetter1(bgJSContent_patched, 'chrome.privacy.services.passwordSavingEnabled')
bgJSContent_patched = replaceSetter1(bgJSContent_patched, 'chrome.privacy.services.autofillCreditCardEnabled')
bgJSContent_patched = replaceSetter1(bgJSContent_patched, 'chrome.privacy.services.autofillAddressEnabled')

assert bgJSContent_patched != bgJSContent

with open(EXT_PATH + '/background.js', 'w') as f:
    f.write(bgJSContent_patched)
