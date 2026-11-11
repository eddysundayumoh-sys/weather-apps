[app]
title = Weather App
package.name = weatherapp
package.domain = org.eddy
source.dir = .
source.include_exts = py
version = 0.1
requirements = python3,kivy,requests,urllib3,chardet,idna,certifi
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
