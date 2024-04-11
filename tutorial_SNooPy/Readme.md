
# This is the 'official' webpage:
https://csp.obs.carnegiescience.edu/data/snpy

# Installations instructions:
https://csp.obs.carnegiescience.edu/data/snpy/installing_snoopy2

although the best is to clone and install from github:
https://github.com/obscode/snpy
especially if you want gen=3 version.

# To use the new Jinget al. template with new NIR K-corrections:

Jing forked the main SNooPy github and created her own with the new template: https://github.com/DeerWhale/snpy-test.git

Download/install as usual. When you create new SNooPy objects, the template will automatically be the new one. 
If you have existing SNooPy fits, then load them in and manually change the template:

```
s = get_sn('mySN.snpy')
s.k_version = "H3+L"
```

Then fit as usual. It will only really affect the NIR, since the optical template is still the same old Hsiao template.

# install extra filters 

from https://github.com/HOSTFLOWS/filters_snoopy/tree/main
