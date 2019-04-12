# CSAW CTF 2018

## ES1337

The patch (`csaw.patch`) should apply cleanly to latest at the time of writing (`11/6/2018`) which is **Chromium** `70.0.3538.77` and **v8** `7.0.276.32`. (See https://omahaproxy.appspot.com/ for version info).


### Files

To obtain files for this challenge. See https://github.com/osirislab/CSAW-CTF-2018-Finals/tree/master/pwn/ES1337


If you want to build your own copy of **v8** do the following:

```bash
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
export PATH=$PATH:$(pwd)/depot_tools
fetch v8 && cd v8
git checkout 7.0.276.32.
gclient sync
patch -p1 < ../csaw.patch
./tools/dev/v8gen.py x64.debug
ninja -C out.gn/x64.debug
```

If you would like to build a debug **Chrome**, see https://chromium.googlesource.com/chromium/src/+/HEAD/docs/linux_build_instructions.md

**Chrome** should be run with `./chrome --no-sandbox` inside **Ubuntu 18.04 Desktop**.
