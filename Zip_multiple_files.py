import zipfile

# name of the new Zip file
zip_file_name = 'new_zip_file.zip'

# names of the source files
file_names = ['file_to_compressed1.txt',
              'file_to_compressed2.txt',
              'file_to_compressed3.txt'
             ]

# Create a ZipFile Object
zip_object = zipfile.ZipFile(zip_file_name, 'w')

# Add multiple files to the zip file
for file_name in file_names:
    zip_object.write(file_name, compress_type=zipfile.ZIP_DEFLATED)

# Close the Zip File
zip_object.close()
