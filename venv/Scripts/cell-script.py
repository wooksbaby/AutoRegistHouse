#!"C:\Users\h\PycharmProjects\auto worker\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'cell==0.0.3','console_scripts','cell'
__requires__ = 'cell==0.0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('cell==0.0.3', 'console_scripts', 'cell')()
    )
