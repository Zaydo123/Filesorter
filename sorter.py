import os, sys, colorama, shutil
from colorama import init, Fore, Back
init(autoreset=False)
print(Back.RED+"STARTING"+Back.RESET)

#filetypes definition
Filetypes = {
    "Main":{"General":["exe","lnk"]},
    "Developer":{
        "Python":["py","pyw","py3","pyc","pyo","pyx","pyd","pxd","pyi","pyz","pywz","rpy","pyde","pyp","pyt","ipynb"],
        "Java":["jar","java","class"],
        "C":["c","cpp","cs"],
        "Web":["html","htm","php","aspx","asp","jsp","odt"],
        "CMD+SHELL":["sh","csh","bat","ps1"],
        "Database":["sql","db"]
        },
    "Compressed":{
        "All":["zip","tar","rar","7z","tgz","gzip","iso"]
    },
    "Documents":{
        "Text":["txt","log"],
        "General":["doc","docx","xls","xlsx","csv","ods","ppt","pptx","pdf"],
    },

    "Engineering":{
        "Autodesk":["ipt","iam","ipn",'idw',"dwg","dxf","f3z","f3d","cam360"],
        "ETC":["3dxml","3ds","max","cad","stl","step"]
    },

    "Media":{
        "Photo":["jpg","jpeg","png","gif","tiff","bmp","raw"],
        "Music":["aac","mp3",'wav',"wma"],
        "Video":["mpeg-1","mpeg-2","avi","mp4","mov","h264","h265","avchd"],
        "Adobe":["psd","aep","aet","prproj","ai"]
    }
}

cwd = os.getcwd()
current_file = __file__[len(cwd)+1:len(__file__)]

for directory in Filetypes.keys():
    if os.path.exists(directory)!=True:
        for subdir in Filetypes[directory].keys():
            os.makedirs(f"{cwd}/{directory}/{subdir}")

local_files = []
for file in os.listdir():
    if str(file).find(".")!=-1:
        local_files.append(file)

for file in local_files:
    if file == current_file:
        continue
    type = os.path.splitext(file)[1];type=type[1:len(type)]
    for cat in Filetypes.keys():
        for subcat in Filetypes[cat].keys():
                if type in list(Filetypes[cat][subcat]):
                    shutil.move(cwd+"\\"+file, cwd+f"\\{cat}\\{subcat}\\"+file)
                    print("MOVED")
