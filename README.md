# Hand-Tracking
Before you can execute the code, there are a few programs/applications and program extensions that need to be installed on your computer: 
1. python (high-level programming language)
2. anaconda (allows for data science package installation in python)
3. homebrew (package manager for macOS)
4. pip (package installer for python)

Here are the steps to follow in order to correctly set up your computer to run the hand-tracking program.

1. Firstly, python must be installed. However, we don't have to directly install it from the python website. Instead, we can install python and pip, quickly and efficiently, both with homebrew.

2. To install homebrew, open your terminal and type in the following command.

        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    Further instructions will be provided in your terminal to assist you in installing homebrew. 

3. To check if homebrew is installed correctly, type the following command into your terminal.
 
        brew help
    
    If an error does not appear, that means homebrew has been successfully installed and you are ready for the next steps.
    If an error appears, repeat step 2 and make sure you followed the instructions provided in your terminal correctly.
    
4. Once homebrew has been installed, we can install both python and pip with entering the following command into your terminal.
 
        brew install python
    
    This command installs the latest version of python, pip, and necessary packages for set up all for you without you needing to do anything. Simply sit back and 
    wait for homebrew to finish installing all the programs and packages for you.
    
5. To test out if python has been correctly installed, type the following command into your terminal.

        python3
    
    If an error does not appear, python has successfully been installed!
    If an error does appear, repeat steps 3-4.

6. Now that python has been installed, it's time to install anaconda which will allow for data science packages to be imported into python. Use the following link to install the latest version of anaconda.

    https://www.anaconda.com/products/individual
    
    Follow the instructions provided by the anaconda installation package and install anaconda on your computer.

7. To check if anaconda has been installed properly, open the anaconda application. The interface should say anaconda navigator and have various options of what IDE to launch.

    If anaconda does not open, reinstall the application (possibly with a different version).

8. Once anaconda has been installed, launch jupyter notebook and a new tab on your browser will be opened. It should look similar to the picture below.
<img width="1145" alt="Screen Shot 2022-03-09 at 8 35 13 AM" src="https://user-images.githubusercontent.com/91576538/157349691-ad95c212-6de1-4f2c-8c7b-139b2470e00b.png">
    
9. Select the location in which you would like to store your python files. Once you have reached the folder/location you would like to store your file, create a new jupyter notebook (On the top left corner, click new, and then click python3). <img width="1156" alt="Screen Shot 2022-03-09 at 9 02 40 AM" src="https://user-images.githubusercontent.com/91576538/157352417-4922dbff-ef54-40de-a57d-6ef63fe3ee02.png">

10. Once your notebook has been created, click on the link below to see the source code to the hand-tracking program (explanations to the code are included as comments in the source code).

        https://github.com/chenw7/Hand-Tracking/blob/main/Hand%20Tracking%20(FPS)

        https://github.com/chenw7/Hand-Tracking/blob/main/Hand%20Tracking%20(LR)
        
11. Install the necessary libraries to run the program using pip (in your terminal). Enter the following commands in your terminal.

        pip install opencv-python==3.4.8.29
       
        pip install opencv-contrib-python==3.4.8.29
        
        pip install mediapipe
        
12. Now that all necessary libraries and accessories for the program have been installed, check whether they have been installed correctly by typing the following command into jupyter notebook and executing the command (execute the command by clicking command+enter).

        import cv2
        import mediapipe
        import time
        
       If an error message does not appear, you can proceed onto the next step.
        
13. Copy the code (provided in step 10) into jupyter notebook and run the program. A new window should appear from your terminal and track your hand movements using your computer's web cam.

14. If errors regarding cv2 or any of the other modules still exist, search for solutions on stackoverflow (most solutions to your problems can be found).

Here are the outputs to the 2 programs. 

The first one should display results similar to these. 

<img width="665" alt="Screen Shot 2022-05-13 at 11 36 04 AM" src="https://user-images.githubusercontent.com/91576538/168206543-93044c3f-cb05-471e-a8a1-8d834218f235.png">

<img width="584" alt="Screen Shot 2022-05-13 at 11 36 21 AM" src="https://user-images.githubusercontent.com/91576538/168206605-94fb4b90-50a0-407b-98a4-d79eae9cb366.png">




The second one should display results similar to these.

<img width="564" alt="Screen Shot 2022-05-13 at 11 24 25 AM" src="https://user-images.githubusercontent.com/91576538/168205491-12eaac8b-869c-450b-b09c-6bc8a9d51059.png">

<img width="843" alt="Screen Shot 2022-05-13 at 11 25 26 AM" src="https://user-images.githubusercontent.com/91576538/168205515-b083ae16-51b6-4b77-ac00-4c1cb014972d.png">

<img width="1119" alt="Screen Shot 2022-05-13 at 11 26 26 AM" src="https://user-images.githubusercontent.com/91576538/168205598-60f94059-7c50-4efd-b90c-9263e90a8404.png">


Note that both prgrams have a limitation of tracking two hands simultaneously due to the processing speed of the computer and the structure of the program which sets a maximum capacity of detecting two hands in the webcam at once.
