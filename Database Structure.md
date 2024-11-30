# Initial Database Design

**User Database**
* User ID *(starts with 1)*
* Whatever's needed for discord auth
* Username *(probably copy from discord auth?)*
* User Display Name *(defaults to username unless otherwise specified)*
* User email address
* User Profile Pic *(default import from discord, have option to upload?)*
* User About *(fill in their own profile, maybe allow markdown if possible?)*
* User Links *(Allow the user to add links to their profile, i.e. to a twitch or youtube account, probably contained as a csv list)*
* Uploaded Scripts *(a csv list of the Script ID of every script this user has uploaded)*
* Blocked Scripts *(a csv list of the Script ID of every script this user has chosen to exclude from their wheel on every spin)*
* Favorite Scripts *(csv list of scripts that the user has favorited)*
* Personal Wheel Odds
    * Recency Bias *(0-10000 scale, the higher the number, the more biased against the most recent winner the wheel will be)*
    * Frequency Bias *(0-10000 scale, the higher the number, the more biased against all previous winners the wheel will be)*
    * Author Bias *(0-10000 scale, the higher the number, the more biased against other scripts by the same script author the wheel will be for the next spin)*.

**Non-Homebrew Script Database** *(The first version of this will not accept homebrew scripts, just until we can get a proof of concept working.)*
* Script ID
* Script Uploader *(User ID)*
* Script Title
* Script Author *(text)*
* Script Author ID *(User ID, if known - I wonder if there's a way to parse this automatically by comparing what the uploader puts in the Author field to the display names and discord names of all users?)*
* Submitted to Public *(Y/N)*
* Added to Public wheel *(Y/N)*
* Teensy *(Auto-detected, determines whether the script is for a full game or for teensy)*
* Description *(Any info about the script should go here - Any stormcatcher protections, any bootlegger rules, etc)*
* Character List *(the upload function should parse the json file and pull all of the characters from the script out of it, and put all characters from the script in a csv in this field)*
* Fabled List *(Same as above, but for Fabled)*
* Traveler List *(If any defined travelers are invluded, they are added here as a csv)*
* Date Last Modified *(When the uploader/author edits the script, this stores when the latest changes were made)*
* Version *(counts how many times the script has been updated)*

**All Version Database** *(A database to keep track of the previous versions of all scripts so on a script's info page, each version can be looked at from a dropdown)* 
* Script ID
* Version *(Auto-calculated)*
* Date Uploaded
* Character List
* Fabled List
* Traveler List
* Description

**Spins Database**
* User ID of spinner
* Script ID of selected script
* Timestamp of the spin.

**Odds Database**
The first column will be the Script ID for each script.
Then each subsequent column will be that script's odds for the user whose ID lines up with that column (which is why USER IDs start at 1).
Whenever a new User is added, another column is created and every script currently in that column receives a 1 as their value for that column.
Whenever a new Script is added, the data for the odds for each user is filled with the average odds among all scripts for that user.

***These next two databases are necessary for the website to properly generate script images when we display scripts***

**Character Database**
* Character ID
* Character Identifier *(How it's identified in jsons)*
* Character Name
* Character Image *(Wedge has a good list for his Wiki project that is copyright-free)*
* Character Type *(Townsfolk, Outsider, Minion, Demon, Traveler, Fabled)*
* Character Description

**Jinx Database**
* Jinx ID
* Character ID 1
* Character ID 2
* Description of Jinx
