#import madule and global variables

from pathlib import Path
import shutil
base_dir =  Path(r"D:\backup\desktop")
target_dir = base_dir /  "sorted"


#declare categories and  extensions 
FILE_CATEGORITS = {
    "image":[".webp",".svg",".tiff",".bmp",".gif",".jpg",".jpeg",".png"],
    "documents":[".pdf",".doc",".docx",".txt",".xls",".xlsx",".ppt",".pptx"],
    "video":[".mp4",".mkv",".avi",".mov",".wmv"],
    "audio":[".mp3",".wav",".aac",".flac",".ogg"],
    "archives":[".zip",".rar",".tar",".gz",".7z"],

}



# create directories based on categories
def create_category_directories():
    for category,_ in FILE_CATEGORITS.items():
        (target_dir/category).mkdir(parents=True,exist_ok=True)



#searching categorizing files 
def search_and_categorize_files():
    for file  in base_dir.rglob("*"):
        for category,extensions in FILE_CATEGORITS.items():
            if file.suffix in extensions:
                try:
                    shutil.copy(file,target_dir/category)
                except shutil.SameFileError:
                    pass
                




#run  the application
print(base_dir)
print(target_dir)