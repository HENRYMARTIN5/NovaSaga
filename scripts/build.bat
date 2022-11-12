@echo off
echo [NovaBuild] Deleting old build directory...
rmdir /s /q build
rmdir /s /q dist
echo [NovaBuild] Building executable...
pyinstaller main.spec
echo [NovaBuild] Build complete!
echo [NovaBuild] Copying assets...
Xcopy /E /I /Y assets dist\assets
echo [NovaBuild] Assets copied, cleaning up...
del /Q /S dist\assets\*.py
del /Q /S dist\assets\*.pyc
del /Q /S dist\assets\util
echo [NovaBuild] Built Nova Saga to /dist successfully!