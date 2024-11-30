# WheelOfScripts

So maybe I only came up with this idea because I was stoned as fuck when I was thinking about it, but part of this was inspired by the work that went into designing the algorithm for the wheel, and partially inspired by the fact that the current script repository site absolutely sucks.

Here's my vision for the final site:

# General Description
The landing page is the wheel of scripts itself, with the ability to spin immediately without logging in or anything. However, you can also log in.

Logging in does three main things:
* When you are logged in, you receive a personalized wheel, which remembers all of your previous spins and maintains a separate odds calculation for you.
* When you are logged in, you will have the ability to filter scripts *before* you spin.
    * Ideally there will be a way for players to indicate characters they DO want to see in scripts rolled, characters they do NOT want to see in scripts rolled, and the ability to not roll a homebrew script. Can probably also filter by teensy/not-teensy since I assume people will probably upload teensies.
* Allows you to submit scripts.
    * Scripts users submit will be included in their personal wheel, but not the general public wheel unless they opt in. 
    * The submission page will ask for the script's name, the author (if not being uploaded by the author), and it will ask if they would like the script to be considered for the wheel for the general public (which will default to yes, but will be easy to switch to no).
    * It will also have a text field where people can talk about the script and give any extra information (especially if the uploaded script is a homebrew or has a Stormcatcher or something like that)
    
The script submission handling will be how we can be a better version of the current script repository.

First, the handler should be able to count the number of characters on the script in order to determine whether the script is a Teensy or not.

Handling the jsons as they are uploaded, if they only contain official characters, they'll go into one database, and if it detects any non-official characters, it will go into a homebrew database. Additionally, if it is a homebrew script, the uploader will be prompted to upload an image file to display for the homebrew script so there is something to display on the wheel's results page.

Non-homebrew scripts will have the json read, and the list of characters in the script added to the database in their entry, to allow for filters. When a non-homebrew script is selected, I would like the results page to dynamically generate the image for the script, by using the official designations to have a system for pulling the correct text and assets.

There will be a button to download the json of that script after viewing the actual script on the site, as well as a place to select any fabled that they might want to add (it will already show fabled that are already on the script). Then, with all those selections, the page will dynamically generate a json file so that the correct title, author, and fabled are all added to the script, as well as putting all of the characters in the correct order, so that all the person downloading it has to do is upload it directly into the botc app.

Additionally, there would be a checkbox for a player to check if they never wanted that script to be rolled for them on the wheel ever.

In the event that more than one non-homebrew script is 100% identical, underneath the title of the script they rolled should have "Also known as 'blank' by 'blank'" for each other script that has exactly the same characters on it.

Using those results pages, it should therefore be easy to just allow people to browse the full list of scripts on the wheel, and then open the page directly and download it like that as well, and have access to search for scripts with particular characters, without particular characters, in a much better way than the current script repository site does.

# Different Pages

## The Wheel
* Main page of site, the wheel should be the most prominent thing on the page. Up at the top should be "The Wheel of Scripts", along with a horizontal list of links to the different pages on the site. Should also have the discord login button at the top right of the page.

## All Scripts
When this page is loaded, it should have a collapsed "Filter" area at the top of the page, and then display a list of scripts, probably by default sorted alphabetically by script name. I'm thinking the fields for the display should be:
* Script Name
* Author (with link to profile, if known)
* Uploader (with link to profile)
* Teensy (Y/N)

The list shouldn't make the page scroll, instead it should only display about 15 scripts per page, and then have buttons to change pages at the bottom of the list.

### Filter
* Full Only/Full + Teensy/Teensy Only
* Exclude Duplicates *(If two scripts have the exact same character list, this will only display the earliest-uploaded one in the list)*
* Characters To Include *(I'm picturing one of those fields where you can start typing a thing, it finds the full things that match them, and when you click it or press enter, it makes a little "object" of that thing in the box, and then you can keep typing, same for excluded characters)*
* Characters to Exclude
* Script Author *(text, maybe with suggestions as people type?)*

## Script Display Page
The page should display the title of the script at the top, along with the author. If there are any other scripts that are identical, in smaller text under the title, it will have "(Also known as X by Y, etc)" for each identical script in the database.
Underneath that, if the script has multiple versions, there should be a dropdown for the user to be able to select a different version, probably indicated by "Version X, Uploaded <datetime>".
Then using the character data, it will generate a script image with all the characters in the right order, any fabled, and any jinxes, as well as the description.
Underneath that, there will be an area where all the currently enabled Fabled are selected, and the player can use checkboxes to modify the fabled.
Then, another area with the same thing but for players to modify the travelers.
Finally, a button that when pressed, will generate a json file for the user to download that has the correct title, author, and characters.
Should probably also be an option to report a script for offensive content.

## Public User Profile
This page should display information about the user selected. Show their display name, show their profile picture, show their description, and then show a list of all the scripts that user has uploaded that are public. Should probably be a way to report a profile for offensive content.

## Private User Profile
This should be a user's view of their own profile. It will display the same information, but have the option to edit, as well as the option to upload, edit, or delete a script.
There should also be a "spin history" so they can look at their past spins.  And a way to reset all of their spins and get a fresh wheel.

## Script Upload/Edit Page
The upload/edit page will basically be the same, except that the edit page will come pre-filled with all of the current script's info and only the upload field will be left blank.
* Script Title
* A checkbox to indicate that the uploader is NOT the author, in which case a text box appears for them to specify the author
* Description of the Script
* json upload.

## Stats Page
I think the only thing I REALLY like from the current site is the stats page, so I'd like to have a version of that.

## Admin Pages
We need ways to check the backlog of scripts to be added to the public wheel, we need to be able to edit and delete users and scripts, and have ways to add new characters as they are added to the game, as well as make bulk additions/subtractions from the wheel.

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
