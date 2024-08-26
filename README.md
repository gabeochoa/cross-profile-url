# cross-profile-url



## To install/Setup

### frontend 
- Create a new profile for your chat apps.
- Go to extension settings and enable developer mode
- Load unpacked extension and choose the cloned repo

### backend 
- Clone this repo somewhere 
- Update the path and extension ID in the json file
- Copy the json config file into your chrome install
`cp com.gabeochoa.openinprofile.json ~/Library/Application\ Support/Google/Chrome/NativeMessagingHosts/`

- Open oip.py in a text editor and update the profile from "Default" to the profile you want the links to open in. (You can find the profile names at the file location mentioned in the python file) 

- Open a new tab with links and cmd+click a link to make sure it worked

### Likely issues
- "Access is forbidden" 
    - you need to update the extension ID host in the json file. You can find the id of your local extension in the details section in chrome. (dont forget to recopy the json over) 
- "Specified Host not found" 
    - Check the path in the json and make sure its where the oip.py file is found
- Just does nothing
    - Check the python version in the #env at the top of oip.py and update for your local installation
