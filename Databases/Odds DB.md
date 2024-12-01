## Odds Database
* The first column will be the Script ID for each script.
* Then each subsequent column will be that script's odds for the user whose ID lines up with that column (which is why USER IDs start at 1).
* Whenever a new User is added, another column is created and every script currently in that column receives a 1 as their value for that column.
* Whenever a new Script is added, the data for the odds for each user is filled with the average odds among all scripts for that user.
