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
