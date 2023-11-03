import os
from moviepy.editor import VideoFileClip

def convert_files():
    input_folder = "before/video"
    output_folder = "after/video"

    print("Fichiers disponibles pour la conversion :")
    files = os.listdir(input_folder)
    for index, file in enumerate(files):
        print(f"{index+1}. {file}")

    file_index = int(input("Entrez le numéro du fichier à convertir : ")) - 1

    if file_index >= 0 and file_index < len(files):
        input_file = os.path.join(input_folder, files[file_index])
        output_file = os.path.join(output_folder, files[file_index].split(".")[0] + ".mp4")

        try:
            clip = VideoFileClip(input_file)
            clip.write_videofile(output_file, codec="libx264")
            print("Conversion réussie!")
        except Exception as e:
            print(f"Une erreur s'est produite : {str(e)}")
    else:
        print("Index de fichier invalide!")


convert_files()
