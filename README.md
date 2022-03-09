# Hand-Tracking
This repository includes programs that tracks the user's hand with a live feed from their webcam on their computer.

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




