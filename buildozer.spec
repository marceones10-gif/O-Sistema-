[app]
title = LelexApp
package.name = lelexapp
package.domain = org.lelex
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json,wav,mp3
version = 0.1
requirements = python3,kivy==2.3.1,kivymd==1.2.0,pillow
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
