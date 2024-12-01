# Spinning The Wheel
This is a detail of what happens after a user presses the button to spin the wheel.

## If the user is NOT logged in
 1. Filters are applied to the list of scripts in order to gather all of the scripts that SHOULD be on the wheel. Each one has a starting weight of 1. This is written into a temporary object that persists through this single session.
 2. The "spin" happens, i.e. a random selection is made from a table containing each script ID a number of times equal to its weight.
 3. The algorithm is applied to the weights after the winner is selected, and those new weights are written into the temporary object.
 4. The winning script is displayed to the user, as well as an option to spin again.
 5. Once this current session ends, the temporary object is destroyed and all of the weights reset to 1 for the next user or next time this user returns.

## If the user IS logged in
1. First, the user's "Blocked scripts" list is consulted to remove all blocked scripts from the spin.
2. Then, the filters set on the spin page are applied to the remaining scripts to create the pool of scripts from which to spin.
3. The script goes to the weight database, and pulls the weights for each script to be included from the column associated with their account.
4. Then, a random selection is made from a table containing each script ID a number of times equal to its current weight.
5. The algorithm is applied to the weights of EVERY script, not just the filtered ones, after the winner is selected, and those weights are re-written into the database.
6. The winning script is displayed to the user, and the record of the spin (Date/time, User, and Script selected) is written to the Spins databse.
