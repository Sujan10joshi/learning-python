import os, shutil

dict_extensions = {
    'audio_extensions' : ('.mp3', '.m4a', '.wav'),
    'video_extensions' : ('.mp4', '.mkv', '.mpeg'),
    'document_extensions' : ('.pdf', '.docx', '.txt'),
    'image_extensions' : ('.jpg', '.png', '.gif')
}

folderpath = input("Enter folder path: ")

def file_finder(folder_path, folder_extension):
    # files = []
    # for file in os.listdir(folder_path):
    #     for extension in folder_extension:
    #         if file.endswith(extension):
    #             files.append(file)
    return [file for file in os.listdir(folder_path) for extension in folder_extension if file.endswith(extension)]

for extension_type, extension_tuple in dict_extensions.items():
    folder_name = extension_type.split('_')[0] + 'Files'
    folder_path = os.path.join(folderpath, folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath, extension_tuple):
        item_path = os.path.join(folderpath, item)
        item_new_path = os.path.join(folder_path, item)
        shutil.move(item_path, item_new_path)

