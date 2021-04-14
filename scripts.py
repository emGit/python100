import os
import zipfile

START = 34
END = 101

for folder in os.listdir(r"C:\Users\NQMC\Desktop\srt\100 Days of Code - The Complete Python Pro Bootcamp for 2021"):
    print(folder)
    day = int(folder[:folder.index('.')])
    if START <= day <= END:
        for file in os.listdir(os.path.join(r"C:\Users\NQMC\Desktop\srt\100 Days of Code - The Complete Python Pro Bootcamp for 2021", folder)):
            if file.endswith(".zip"):
                # print(os.path.join(r"C:\Users\NQMC\Desktop\srt\100 Days of Code - The Complete Python Pro Bootcamp for 2021\34. Day 34 - Intermediate+ API Practice - Creating a GUI Quiz App", file))
                print(file)
                with zipfile.ZipFile(os.path.join(r"C:\Users\NQMC\Desktop\srt\100 Days of Code - The Complete Python Pro Bootcamp for 2021", folder, file), 'r') as zip_ref:
                    zip_ref.extractall(rf"C:\z\inc\dev\projects\python100\p{day}\{file}")