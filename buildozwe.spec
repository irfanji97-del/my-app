[app]
title = My Python App
package.name = mypythonapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas
version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.accept_sdk_license = True
