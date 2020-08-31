PX = 10
PY = 10
BTN_W = 10

GEN_IMG_EXTS = ['bmp', 'png', 'tiff', 'tif', 'jpeg', 'jpg']
LYT_LFP_EXTS = ['lfp', 'lfr', 'raw']
LYT_CAL_EXTS = ['tar', 'raw']
ALL_EXTS = ['*.*']

# blank icon
ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64
