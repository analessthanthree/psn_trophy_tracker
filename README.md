# PSN Trophy Tracker

This code, built on top of the wonderful [PlayStation Network API
Wrapper in Python (psnawp)](https://github.com/isFakeAccount/psnawp), will help
you create an OBS source that will automatically keep track of the number of
trophies you have for a certain PlayStation game.

The current iteration of this code will track your trophies in a text file.

Future iterations of this code will run a web server that you can access via a
browser source instead. This will allow for the display of images and styling of
text.

# How to Use

## The Prerequisites

If you've already done the prerequisite steps, you can skip ahead to the Running
the Code section below.

### Install Python and Pip

You may already have python installed. To check, open a command prompt and type:
`python --version`, and `pip --version`.

- Install `python`, including it's package manager, `pip`

Note that this has only been tested with Python 3.10.12.

### Downloading the Code

- Click the green `<> Code` button at the top of this page
- `Download ZIP`
- Extract the ZIP file wherever strikes your fancy. You'll have a folder named
  `psn_trophy_tracker`.

### Creating the Virtual Environment

- Navigate to the `psn_trophy_tracker` folder
- Right click in any empty space and open a command prompt
- Create a venv in this directory named `venv` by typing the following command
  in the command prompt and hitting Enter
  `python -m venv venv`
- Activate the virtual environment, on the Windows command prompt, this is done
  by typing:
  `./venv/Activate.bat`
- Install the appropriate packages:
  `pip install -r requirements.txt`

### Getting your My PlayStation Sign in Code

As per the `psnawp` [docs](https://github.com/isFakeAccount/psnawp):

To get started you need to obtain npsso <64 character code>. You need to follow the following steps

1) Login into your My PlayStation account.
2) In another tab, go to https://ca.account.sony.com/api/v1/ssocookie
3) If you are logged in you should see a text similar to this

`{"npsso":"<64 character npsso code>"}`

This npsso code will be used in the api for authentication purposes. The refresh
token that is generated from npsso lasts about 2 months. After that you have to
get a new npsso token. The bot will print a warning if there are less than 3
days left in refresh token expiration.

---

***Do NOT give or show this code to anybody, as you would essentially be giving
them access to your PSN account***

Copy/paste this code into the line at the top of `psn_trophy_tracker.py` that
reads:
`npsso = "YourCodeGoesHere"`

Make sure you keep the double quotes, or else this won't work.

Keep in mind that, as per the `psnawp` docs referenced above, you may need to
generate a new code and replace it periodically.

### Running the Code

NOTE: When you are finished using this code, stop it from running from the
command prompt by typing "ctrl + c", and/or closing the command prompt window.
This will stop the code from constantly needlessly querying the PlayStation
servers for your info

---

- Make sure you've done all the prerequisites
- If you have not already done so, open a command prompt in the
  `psn_trophy_tracker` folder
- If you have not already done so, activate the virtual environment by typing
  the following into the command prompt:
  `./venv/Activate.bat`
- Finally, run the code with:
  `python psn_trophy_tracker.py`
- You will be given a list of all your games and asked to enter one to track.
  Type the appropriate number from the list and then hit "Enter".
- The code will interact with PSN to get your trophies for this game and update
  `trophies.txt` to show your total progress. Use this file as a text source in
  OBS.
