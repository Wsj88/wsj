# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['start窗口.py'],
    pathex=[],
    binaries=[],
    datas=[('/Users/edy/Desktop/接口测试/jiekouceshi/qingtest','qingtest'),
    ('/Users/edy/Desktop/接口测试/jiekouceshi/element','element'),
    ('/Users/edy/Desktop/接口测试/jiekouceshi/testcase','testcase')],
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
    [],
    exclude_binaries=True,
    name='start窗口',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='start窗口',
)
