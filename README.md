# JokeBot
An interactive bot made with Rasa that tells the user jokes. The bot is a friend trying to become a comedian and the user's role is to give feedback on their jokes. 

## How to Run
 To run the bot, make sure you have `rasa` installed on `Anaconda`or any python virtual environment. For detailed instructions on the installation of Rasa please refer to the official documentation: [How to Install Rasa](https://rasa.com/docs/rasa/installation/).
Once Rasa has been installed, navigate to the root folder of the project, and do the following:
 - run `rasa train` and wait for it to train the model. **Note:** This may take a while depending on your system.
 - _**VERY IMPORTANT**_ : In a **separate** terminal window/tab, run the command `rasa run actions`, to run a custom actions server for the bot to be able to work properly. 
 - Then once it has been trained and the action server is running, enter `rasa shell --endpoints endpoints.yml` to talk to the bot on the CLI! At anytime you can enter `/stop` to stop the CLI and end the current session.

## Updates
 The bot now has a GUI, it also generates photo based memes, and responds to invalid user inputs.
