[app]
title = TestApp
package.name = testapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

icon.filename = icon.png
presplash.filename = splash.png

[buildozer]
log_level = 2

[android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a

android.allow_backup = True
android.gradle_dependencies =

android.enable_androidx = True
android.add_src =

android.private_storage = True
android.accept_sdk_license = True

android.ignore_path = .git,__pycache__,.github

