# JokeBot
An interactive bot made with Rasa that tells the user jokes. The bot is a friend trying to become a comedian and the user's role is to give feedback on their jokes. 

## How to Run
To run the bot, make sure you have `rasa` installed on `Anaconda` or any python virtual environment. For detailed instructions on the installation of Rasa please refer to the official documentation: [How to Install Rasa](https://rasa.com/docs/rasa/installation/).

Usually all you need to do to install rasa is run the following command:
```pip3 install rasa```
If the above doesn't work, refer to the documentation linked above.


Once Rasa has been installed, navigate to the root folder of the project, and do the following:
 - run `rasa run --m ./models --endpoints endpoints.yml --port 5002 -vv --enable-api --cors "*"` and wait for it to launch. **Note:** This may take a while depending on your system.
 - _**VERY IMPORTANT**_ : In a **separate** terminal window/tab, run the command `rasa run actions`, to run a custom actions server for the bot to be able to work properly.
- If there is an error about `spaCy` model not being able to loaded, run the following command, and it should work: `python -m spacy download en_core_web_md`

Once the commands finish running, in another **separate** terminal (That's 3 in total), navigate to the `GUIWebsite` folder using something like `cd GUIWebsite` from the root folder.
Then type the following into the console to start up the server: `python -m http.server 8000`

Once that is done, type `localhost:8000` into your browser's URL field, and you should be greeted
with this page:

![JokeBot chat window](images/botchat.png)

Have fun talking to our bot!

## New Features for A3
 - ### Graphical User interface
   
 - ### Extra Topic
   For A3, We decided to include an extra topic for our joke bot in the form of memes. Since "memes" are another form of jokes that are part of a rapidly
   advancing movement that brings humour to the internet, we included them as an extra topic for our bot. When the user asks for memes, the bot will deliver by 
   showing them a link to a few galleries filled with some memes, which are 
 - ### Out of Scope Message Handling
 - ### Synonym Recognition
 - ### Named Entity Recognition
 - ### Sentiment Analysis
