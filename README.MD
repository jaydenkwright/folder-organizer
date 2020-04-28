## Specifications

### Organization

1. Get current directory
    - ``` path = os.getcwd()```

2. Get list of all files within the directory
    - Loop through a list of all files within directory

3. Get the file type for each file
    - Install "filetype" package
    - ``` pip install filetype ```
    - Use ``` guess() ``` attribute to find MIME type of file
    - - jpg - ``` image/jpeg ```
    - - mp4 - ``` video/mp4 ```
    - - mp3 - ``` audio/mpeg ```

4. Check if folder for given filetype has been created, if not, create it
    - "Images" folder
    - "Videos" folder
    - "Audio" folder
    - "Archive" folder
    - "Others" folder

5. Move each file from root directory to folder based on file type

6. Create subfolders within the filetype folders to organize files based on date
    - - ``` 2020 folder``` -> ``` April folder ``` -> ``` Mon April 27 folder ``` 

