import os

def create_folder_and_files():
    path_folder = os.path.join(os.getcwd(), "files")
    file1 = os.path.join(path_folder, "arquivo1.txt")
    file2 = os.path.join(path_folder, "arquivo2.txt")
    
    if not os.path.exists(path_folder):
        os.mkdir(path_folder)
        print(f"Pasta '{path_folder}' criada com sucesso.")
    
    with open(file1, "w") as f1:
        f1.write("Este é o arquivo 1.")
        print(f"Arquivo '{file1}' criado com sucesso.")
    
    with open(file2, "w") as f2:
        f2.write("Este é o arquivo 2.")
        print(f"Arquivo '{file2}' criado com sucesso.")

