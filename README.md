### Maya installetion ###

1.requirements :- 

(i) python varsion 3.10

(ii) [anaconda](https://www.anaconda.com/download/)

(iii) FFMPEG

(iv) CUDO

(v) cuDNN

(vi) [model](https://github.com/Hillobar/Rope/releases/tag/Sapphire)

1. Select a folder, or create one (not /system32). Once you're in that folder, you can right-click it and select, 'Open in Terminal'

2. Clone the repository to your folder:
```
git clone https://github.com/Hillobar/Rope
cd Rope
```
or,

Download the .zip from Github and unzip to your folder

3. Set up a local venv. Inside CMD, make sure you are in the Rope folder. you should have /rope, /models, as subfolders.
```
# create the virtual environment
python.exe -m venv venv

# activate the local venv
.\venv\Scripts\activate

# check if you have installed the correct python version (Python 3.10.X)
python --version

# install the dependencies for Rope
.\venv\Scripts\pip.exe install -r .\requirements.txt
or using anaconda3
```

or using anaconda3
```
# create a conda venv with the correct python version
conda create -n Rope python=3.10.13

# activate the virtual environment
conda activate Rope

# install the dependencies
python -m pip install -r requirements.txt

```
Important: Make sure that you install the virtual environment with the correct python version. Rope only works with with any 3.10 version, nothing older or newer than that.

Download and install 3rd-party dependencies
Install the models

To get access to all the features of Rope, you need to download [the models from here](https://github.com/Hillobar/Rope/releases/tag/Sapphire). You need all of the files.

Place the downloaded model files in the Rope/models folder

Install the external dependencies (if you haven't done so already)

FFMPEG

Download FFMPEG here
CUDA Toolkit 11.8 (needed if utilizing GPU)

Follow these instructions to install CUDA Toolkit v11.8

Check if the installation was successful (run in the terminal)

nvcc --version
cuDNN >= v8.5 for CUDA 11.x (needed if utilizing GPU)

Download the cuDNN >= v8.5

Follow these instructions to install cuDNN

###How to update
To update the repository to its latest version, simply navigate to the Rope directory and open the terminal.
```
# pull and apply the latest updates from Github
git fetch --all

# Reset the repository to its latest version
# local files like the venv remain untouched
git reset --hard origin/master
```
How to use Rope
Choose your target video, source and ouput directories

Start the Rope backend by clicking on the button Start Rope

Select the Input Video

Swap the face in the live preview

Scroll to a frame with the face you want to swap

Scan contained faces by clicking Find Faces

Select the desired face that was found

Select an Input Face to assign to the Found Face that is highlighted

Shift-click multiple Input Faces to use a blended version
Click Swap Faces to see the changes in the video preview

(Optional) Apply filters like the Restorer model to modify and improve the results

Export the video to disk

Go to the starting frame of your video

Press Record to arm the Play button for recording

Press the Play button to start the recording

Press Play again to stop the recording, or wait for the video to reach the end

Disclaimer: Modules like the GFPGAN, CLIP, Occluder, and Mouth Parser are not automatically loaded into memory until you activate them manually. This saves you precious memory and allows you to increase the amount of threads if you have lower memory.

  
