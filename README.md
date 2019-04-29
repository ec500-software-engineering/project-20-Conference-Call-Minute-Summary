# project-20-Conference-Call-Minute-Summary
It's a very convenient software for people to transfer audio to text.
## User Stories
For people who have had a conference call, they could transfer their call audio to a text file, then have a simple summary
about their conference call.
For people who need to have a different language version for their text, they could also get their translation with
 this software.
## Architecture
image
## Technology Selection
* IBM Speech to Text API
    * We use Speech to Text API to tranfer audio to text
* Google Translation API
    * We use Google Translation API to do the translation
* FFmpeg
    * Since to use the IBM API, we need to specify the type of input audio file(we chose ".wav" for this 
    software), so we have implemented the FFmpeg for people to transfer their audio file.
* PyQt 5
    * We use this powerful frame for the GUI of this software.
* jieba 
    * Library for text ranking.
## How to Use
This part introduces how to use the software.
### Requirements
Before using, you need to install libraries below for your Python:
* PyQt 5  
``pip install PyQt5``
* Portaudio  
for mac:  
``brew portaudio``  
for Windows:  
see http://www.portaudio.com/
* pyaudio  
``pip install pyaudio``
* IBM API  
``pip install ibm-watson``
* Google API  
``pip install google-cloud-translate``
* jieba  
``pip install jieba``
* FFmpeg  
``pip install ffmpeg``  
### GUI
image





