# -*- mode: python ; coding: utf-8 -*-
# Spec file for pyinstaller to compile

block_cipher = None

assets = [
    ( 'assets/levels', 'assets/levels/' ),
    ( 'assets/music', 'assets/music/' ),
    ( 'assets/sprites', 'assets/sprites/' ),
    ( 'assets/managers/font', 'assets/managers/font/' ),
    ( 'assets/managers/menu_ui', 'assets/managers/menu_ui/' ),
    ( 'README.md', '.' )
]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=assets,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets\\sprites\\ui\\icon.ico'],
)
