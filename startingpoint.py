import subprocess
import os
import sys

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Desktop', 'CaptureTheFlag','welcome.txt')



#parent_path=$( cd "$(CaptureTheFlag/welcome.txt "${BASH_SOURCE[0]}")"; pwd -P )
#os.system(filename)

os.system('"C:/Users/jlvel/Desktop/CaptureTheFlag/welcome.txt"')


sys.exit()
raise SystemExit
