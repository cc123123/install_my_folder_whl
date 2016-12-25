import glob, os
from subprocess import call

# 安裝指定目錄下的套件包
dir_folder = "檔案目錄"
os.chdir(dir_folder)
for file in glob.glob("*.whl"):
    call(["pip", "install", dir_folder + "/" + file])
    print("install package "  + dir_folder + "/" + file)
