# Handling Script Uploading
Here is the process I'm envisioning for uploading a script:
1. The user is brought to a page with just an upload box for a json script and a submit button.
2. The json is read.
    * First, it checks if it is a valid json file, and then a valid BotC script. If not, it rejects it and sends the player back to the upload form.
    * If there is a script name, that is pre-filled into the field on the next page
    * If there is an author, that is pre-filled into the field on the next page.
    * If there is a logo url, that is pre-filled
    * If there is a background url, that is pre-filled
    * If there is a predefined night order, that is passed through invisibly to the next page.

4. After all of the read information is pre-filled into the form, the user can see the form. It has the following fields:
    * Script Title
    * Checkbox to verify they are the script's author, default checked. If not, the Author field becomes visible.
    * On the left side of the page, a script image will be put in place using the json info to display all of the characters in the right order.
    * On the right side of the page will be a large textbox for the user to input the description of the script.
    * Underneath that will be two boxes, one on the left and one on the right. The left will be for Fabled, the Right will be for Travelers.
        * The Fabled box starts pre-filled with any fabled originally on the script. The user can type in the box, and it will find the closest match, and then once they select it, a bubble with that fabled will appear that can be removed by clicking on it. The ones originally on the script can also be modified that way.
        * The Travelers box is the same as the Fabled box, and starts with pre-selected Travelers. The user will have the option to edit these and include up to 5.
    * Finally, right above the submit button, will be a checkbox that defaults to selected if the user wishes to submit that script to the full wheel, rather than just include it privately.

   4. After all of that information is collected, it is written to the database - the character list from the json will be extracted and converted to a list of Character IDs for storage.
