A voice operated calculator
==========================
This library is an extended version of the speech_recognition library. This library provides a speech recogniser supporting multiple speech input methods. For this extension, only the microphone input was tested, which you can provide by simply talking into your laptop's microphone, or the microphone of any headphones you might have plugged in. Before you can give input the first time, you have to wait a bit, because it measures the amount of noise, and sets an energy threshold to cancel that noise out. This allows for usage in different environments. However, when there is a lot of noise, you yourself will have to talk louder to get above the threshold, so it works best in a quiet environment. Further tweaking can be done in setting the threshold, but also for example in setting the dialect that you speak, for optimal results. Further information on this can be found in the **Troubleshooting** section of the original README file.

##### Requirements
The versions of **python** that you can run this code on are python 2.7 and above.
The **numpy** and **pyaudio** libraries should also be installed. The exact versions that work were not tested, but if you run ``pip install numpy`` and ``pip install pyaudio``, it will automatically install a version that is suitable for your python version.
Windows users might run into problems with this. If so, you can try the following:
* Make sure that your python is added to PATH (easiest through a checkbox upon installation)
* ``pip install pipwin``
* ``pipwin install pyaudio``

The original repository allows multiple ways of speech input, but the extension was only tested with microphone input, so this file will only explain that usage. For other usage, you can refer to the original README.rst file, also in this repository. Also refer to this file if you are missing any libraries or modules. Even though you only need **numpy** and **pyaudio** for the using the calculator through the microphone, it might be that for other functionality you need some other packages as well.

##### Starting the calculator
For this project, the **quickstart** of the original project was used.
In order to start the calculator, you need to set your working directory to the directory or folder where you have stored this project. You can use the ``cd <path to project folder>`` command for this.
To then start the program, use the command ``python –m speech_recognition``. All the main code used for running the calculator can be found in ``speech_recognition/__main__.py`` (for the recognition and interaction part), and ``speech_recognition/calculator.py`` (for the calculating part).

##### Extension to the original repository
The original repository was exceptionally good at recognising numbers. From this, the idea of creating a voice operated calculator was formed. After trying out some operations, it was clear that it could even recognise the operations that are quite long when spoken out, and convert them into mathematical symbols. This confirmed the idea that the origninal repository would be very useful for making a voice operated calculator.

Since python can evaluate strings, the task at hand was trying out different ways to say equations out loud, and implementing a way to convert these utterances to a string that python can evaluate. We tried to include as much of the most common functionalities of a calculator as possible. The final version of the calculator can do the following things:
Functionality | Spoken command
--------------|----------------
Additions     | plus
Subtractions  | minus
Multiplications | times
Divisions | divided by
Square root | the square root of
Exponents | to the power (of)
Opening bracket | open
Closing bracket | close
Logarithm (ln) | log
Natural number | e
Exiting the program | stop

These commands are converted to python operators or numpy functions. It is possible to use brackets to create a longer equation within e.g. a square root. This way you can make more complicated equations. Further tidying is done by converting to lowercase, converting '1 million' to '1000000', and removing spaces.

If the string cannot be evaluated by python, it will return this to the speech recogniser, which will ask you to try again.
To exit the program, you can say 'stop', or, if it does not catch your voice anymore, use ``ctrl+c`` or ``cmd+c``.

##### Challenges
One challenge of this project was the energy threshold. When you are testing the calculator in a noisy environment, like the Campus Fryslân building, it will have trouble recognising that you are speaking. Very often, it would work once, but after that it would not pick up on anything anymore. We tried readjusting the energy level threshold more often, but this did not improve it. Something that could make it easier to work with this, is to ask the user for typed input indicating whether or not to exit the program after a certain time of no input. This was not implemented in the current project, but could be used in future extensions.

Another challenge was that the recogniser gave the impression of being consistent in the text that it would convert the commands into, but we found out that this would differ between sessions. The first few times of testing it would for example sometimes display the input 'minus' as 'Minus' instead of '-'. Another example is that the recogniser would recognise 'close' as 'clothes' in certain contexts, especially in more complex equations.

The final challenge is the way of implementation. With regex we allow for some flexibility, but other than that, we have different checks for each operation. Expanding the calculator would therefore eventually lead to code that becomes difficult to read and debug. For this simple calculator, it is not a problem yet.

##### Source and licensing
The orignial library is the following:
Zhang, A. (2017). Speech Recognition (Version 3.8) [Software]. Available from https://github.com/Uberi/speech_recognition#readme.

The original library was made available under the 3-clause BSD license. For more information about this, read the LICENSE.txt file from the original library, also included in this project's root.
