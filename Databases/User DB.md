## User Database
* User ID *(starts with 1)*
* Whatever's needed for discord auth
* Is Admin *(Y/N)*
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
