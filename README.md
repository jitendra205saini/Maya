![](https://github.com/jitendra205saini/Maya/blob/main/maya/maya/media/splash.png?raw=true)



### 1. श्लोक :- ###

- माया मृगतृष्णा सदा चलिता, निजस्वरूप विस्मृति पलिता ।<br>
   आभासित जग मुख बदलाए,  सत्य वही जो अंत में पाए ।।


   - भावार्थ (हिंदी):-
      
      - इस श्लोक का अर्थ है कि माया (भ्रम) हमें एक मृगतृष्णा की तरह सदा भटकाती रहती है और हमारे असली स्वरूप 
       को विस्मृति में डाल देती है। जब हम चेहरों को बदलते हैं (face swap करते हैं), यह केवल एक आभासी परिवर्तन 
       होता है, क्योंकि अंततः सत्य वही होता है जो स्थायी और अंतिम होता है।



    - Translation (English):-
      
      - The meaning of this verse is that Maya (illusion) constantly leads us astray like a 
        mirage, causing us to forget our true nature. When we swap faces (face swapping), it is 
        merely an illusory change, as in the end, the truth is what remains permanent and real.
````
maya/
│
├── chehra(face)/      # Input faces (images)
│   ├── face2.jpg
│   └── face2.png
|
├── lakshya(target)/   # Input target (video / image)
│   ├── target_image.mp4
│   └── target_image.jpg
|
├── maya/
│   ├── __pycache__/
│   │   ├── Coordinator.cpython-310.pyc
│   │   ├── Coordinator.cpython-312.pyc
│   │   ├── Coordinator.cpython-38.pyc
│   │   ├── Dicts.cpython-310.pyc
│   │   ├── Dicts.cpython-38.pyc
│   │   ├── GUI.cpython-310.pyc
│   │   ├── GUI.cpython-38.pyc
│   │   ├── GUIElements.cpython-310.pyc
│   │   ├── GUIElements.cpython-38.pyc
│   │   ├── Models.cpython-310.pyc
│   │   ├── Models.cpython-38.pyc
│   │   ├── Styles.cpython-310.pyc
│   │   ├── Styles.cpython-38.pyc
│   │   ├── VideoManager.cpython-310.pyc
│   │   ├── VideoManager.cpython-38.pyc
│   │   └── rope.cpython-38.pyc
│   │
│   ├── external/
│   │   └── __pycache__/
│   │   |   ├── clipseg.cpython-310.pyc
│   │   |   └── clipseg.cpython-38.pyc
│   │   |
│   |   ├── cliplib/
│   │   |     ├── __init__.py
│   │   |     ├── bpe_simple_vocab_16e6.txt.gz
│   │   |     ├── clip.py
│   │   |     ├── model.py
│   │   |     ├── simple_tokenizer.py
│   │   ├── clipseg.py
│   │   └── resnet.py
│   │
│   └── media/
│   |    ├── OffState.png
│   |    ├── OnState.png
│   |    ├── Screenshot 2024-10-02 172025.png
│   |    ├── Screenshot 2024-10-02 172209.png
│   |    ├── _add_marker_hover.png
│   |    ├── _add_marker_off.png
│   |    ├── marker.png
│   |    ├── maya.png
│   |    ├── next_marker_hover.png
│   |    ├── next_marker_off.png
│   |    ├── play_hover.png
│   |    ├── play_off.png
│   |    ├── play_on.png
│   |    ├── previous_marker_hover.png
│   |    ├── previous_marker_off.png
│   |    ├── rec_hover.png
│   |    ├── rec_off.png
│   |    ├── rec_on.png
│   |    ├── remove_marker_hover.png
│   |    ├── remove_marker_off.png
│   |    ├── save.png
│   |    ├── splash.png
│   |    ├── stop_hover.png
│   |    ├── stop_off.png
│   |    ├── stop_on.png
│   |    ├── tL_beg_hover.png
│   |    ├── tL_beg_off.png
│   |    ├── tL_beg_on.png
│   |    ├── tL_left_hover.png
│   |    ├── tL_left_off.png
│   |    ├── tL_left_on.png
│   |    ├── tL_right_hover.png
│   |    ├── tL_right_off.png
│   |    └── tL_right_on.png
│   | 
│   ├── Coordinator.py
│   ├── Dicts.py
│   ├── GUI.py
│   ├── GUIElements.py
│   ├── Models.py
│   ├── Styles.py
│   └── VideoManager.py
│
├── parinaam(result)/  # Output (final swapped video/image)
│   ├── result_video.mp4
│   └── result_image.jpg
|
├── Maya.bat
├── Maya.py
├── models  
└── requirements.txt

````

### Maya installetion 😊 :-

**Hardware Requirements**:-

| Requirement Type | CPU | RAM | GPU | Storage | OS |
|------------------|-----|-----|-----|---------|----|
| **Minimum**      | Intel Core i5 (8th Gen, 4 cores, e.g., i5-8250U) or AMD Ryzen 5 (3rd Gen, e.g., Ryzen 5 3500U | 8 GB | NVIDIA GTX 1050 (2 GB VRAM) | 10 GB SSD | Windows 10/11 |
| **Recommended**  | Intel Core i7 (13th Gen, 6 cores, e.g., i7-13700H) or AMD Ryzen 7 (7th Gen, e.g., Ryzen 7 7840HS) | 16 GB | NVIDIA RTX 2060 (6 GB VRAM) | 20 GB NVMe SSD | Windows 11 |

----
1.requirements 👉 

(i) [python varsion 3.10]

(ii) [anaconda]

(iii) [FFMPEG]

(iv) [CUDO]

(v) [cuDNN]

(vi) [models]


- ***python varsion 3.10***
    
     - [Download python here](https://www.python.org/downloads/windows/)

- ***Anaconda***

     - [Download Anaconda here](https://www.anaconda.com/download/)

- ***models***

     - [Download Kaggle here](https://www.kaggle.com/models/jitendrakumarsaini25/maya_face_-swapping)
     - Place the downloaded model files in the ```maya/models``` folder
       ![](https://github.com/jitendra205saini/Maya/blob/main/maya/instruction_image_folder_not_use_this_code/kaggle.png?raw=true)

1. Select a folder, or create one (not /system32). Once you're in that folder, you can right-click it and select, 'Open in Terminal'

2. Clone the repository to your folder:
```
git clone https://github.com/jitendra205saini/Maya.git
cd Maya
```
or,

**Download the .zip from Github and unzip to your folder**

3. Set up a local venv. Inside CMD, make sure you are in the maya folder. you should have /maya, /models, as subfolders.

![](https://github.com/jitendra205saini/Maya/blob/main/maya/instruction_image_folder_not_use_this_code/cmd.png?raw=true)
   
```
# create the virtual environment
py -3.10 -m venv mayaEnv

# activate the local venv
.\mayaEnv\Scripts\activate

# check if you have installed the correct python version (Python 3.10)
python --version

# install the dependencies for maya
.\mayaEnv\Scripts\pip.exe install -r .\requirements.txt

```

or using anaconda3

![](https://github.com/jitendra205saini/Maya/blob/main/maya/instruction_image_folder_not_use_this_code/Anaconda.png?raw=true)

````
#open same loction D:/maya/ in anaconda terminal
cd /d D:\maya\maya --your folder location--

# create a conda venv with the correct python version
conda create -n Maya python=3.10

# activate the virtual environment
conda activate Maya

# install the dependencies
python -m pip install -r requirements.txt
````

Important: Make sure that you install the virtual environment with the correct python version. Rope only works with with any 3.10 version, nothing older or newer than that.

4.Download and install 3rd-party dependencies

- Install the external dependencies (if you haven't done so already)

   - ***FFMPEG***

      - [Download FFMPEG here](https://www.ffmpeg.org/download.html)
      
      - Watch the installation instructions by clicking the image below:

        [<img src="https://i.ytimg.com/vi/4jx2_j5Seew/maxresdefault.jpg" alt="FFMPEG Installation Instructions" width="300">](https://www.youtube.com/watch?v=4jx2_j5Seew)

  - ***CUDA Toolkit 12.4(needed if utilizing GPU)***

     - [Download](https://i.ytimg.com/vi/ZDCuVItpM4k/maxresdefault.jpg) the cudo toolkit
       
     - Watch the installation instructions by clicking the image below:
       
       [<img src="https://i.ytimg.com/vi/r7Am-ZGMef8/maxresdefault.jpg" alt="CUDA Installation Instructions" width="300">](https://youtu.be/ZDCuVItpM4k?si=mQ3t5isVQPfF6kRS)
    

    - Check if the installation was successful (run in the terminal)

    -  ```nvcc --version```
   - ***cuDNN = latest for CUDA 12.4 (needed if utilizing GPU)***

     - [Download](https://i.ytimg.com/vi/RY2mEbi7PJc/maxresdefault.jpg) the cuDNN = latest

     - Watch the installation instructions by clicking the image below:

       [<img src="https://i.ytimg.com/vi/GPBeiKYkuZE/maxresdefault.jpg" alt="cuDNN Installation Instructions" width="300">](https://youtu.be/RY2mEbi7PJc?si=-pCG19hzt4CdhCyg)
    
### How to update ###
   
   - To update the repository to its latest version, simply navigate to the maya directory and open the terminal.
```
# pull and apply the latest updates from Github
git fetch --all

# Reset the repository to its latest version
# local files like the venv remain untouched
git reset --hard origin/master
```
## How to use Maya ##

1. Choose your target video, source, and output directories.

2. Start the Maya backend by clicking on the button ```Start Maya```.

3. Select the Input Video.

4. Swap the face in the live preview:
   - Scroll to a frame with the face you want to swap.
   - Scan contained faces by clicking ```Find Faces```.
   - Select the desired face that was found.
   - Select an Input Face to assign to the Found Face that is highlighted.
     - Shift-click multiple Input Faces to use a blended version.
   - Click ```Swap Faces``` to see the changes in the video preview.
   - *(Optional)* Apply filters like the **Restorer model** to modify and improve the results.

5. Export the video to disk:
   - Go to the starting frame of your video.
   - Press ```Record``` to arm the ```Play``` button for recording.
   - Press the ```Play``` button to start the recording.
   - Press ```Play``` again to stop the recording, or wait for the video to reach the end.

---



Follow me on LinkedIn : [click](https://www.linkedin.com/in/jitendarkumarsaini25/)


**Disclaimer**: Modules like the GFPGAN, CLIP, Occluder, and Mouth Parser are not automatically loaded into memory until you activate them manually. This saves you precious memory and allows you to increase the amount of threads if you have lower memory.


  
