import sys
import os
from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = ['--onefile', '--windowed']
    run(['main.py'] + opts)
