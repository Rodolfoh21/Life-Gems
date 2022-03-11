Hey Guys, Rodolfo Here.

Some important things to clarify first. Please check the requirements.txt and install that version of Django and upgrade pip to that version. Once you have cloned this repository into whatever directory you wanted, make sure to create a virtual environment within the folder "Life Gems". In order to create a virtual environment, use the command line:
  python -m venv venv

You should see a folder named "venv" that has been created. Now we have to activate the environment, if you are on windows, open Powershell and navigate to the "Life Gems" directory. then use this command line:
  ./venv/Scripts/activate

If it was successful, you should see this in front of your directory:
  (venv) PS C:/Users

Once that is done, you'll have to install django again and upgrade pip again as well. In order for us to work well, we have to reproduce a similar virtual environment for all of us, so please check the requirements.txt and install the dependencies needed. An example of getting the same version is:
  pip install django==4.0.3

If you are to install anything else within the virtual environment, PLEASE update the requirements.txt file so that we can all keep track of the dependencies needed. You can update the requirements.txt file by using the command line:
  python -m pip freeze > requirements.txt

Please do not upload your venv file onto GitHub. We all have different machines, and quite frankly I'm not even sure of the problems that can occur if we were to accidently download the file. We could possibly hit a roadblock and be trying to fix whatever mess that caused. So to avoid any problems with that, just don't upload it. 

Remember to review any Django tutorials if you have any problems. If you work on an app, don't forget to apply the migrations so your work is saved. The command line is:
  python manage.py migrations

Please make sure to read up on migrations. That way we can avoid either erasing each others work. Remember to check discord in the updates section, so that we can do the appropriate pulls and commits needed. It doesn't matter if you didn't finish what you're working on. If you have to go or do something else, Commit it, and just leave a comment on where you left off of. This is so everyone is aware of who's working on what. 

If you are going to make another app, use the command line:
  cd apps
  django-admin startapp <app_label>

In order to have better organization, all apps are in the apps folder. Please read up on apps and their uses. Its going to be extremely important, especially if we don't want to clutter our code or be confused with what's where.
