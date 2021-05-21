import os
filenames = os.listdir("diseases") # Obtain a list of the files in the folder
                                   # diseases
f = open("diseases/" + filenames[0]) # Open the first file in the folder diseases
text0 = f.read()
f.close()
print(text0[:2000])  # Output the first 2000 characters in the file we opened