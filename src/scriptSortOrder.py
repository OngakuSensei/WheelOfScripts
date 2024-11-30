def scriptSortOrder(input_str):
    # Strip leading/trailing spaces from the input string
    input_str = input_str.strip()

    # Check shortest conditions first, then nest longer conditions within
    if input_str.startswith("If"):
        if input_str.startswith("If you"):
            if input_str.startswith("If you are “mad”"):
                return 23
            elif input_str.startswith("If you die"):
                return 21
            elif input_str.startswith("If you died"):
                return 22
            else:
                return 24
        elif input_str.startswith("If the Demon"):
            if input_str.startswith("If the Demon dies"):
                return 25
            elif input_str.startswith("If the Demon kills"):
                return 26
            else:
                return 27
        elif input_str.startswith("If both"):
            return 28
        elif input_str.startswith("If there are 5 or more players alive"):
            return 29
        else:
            return 30
    elif input_str.startswith("All"):
        if input_str.startswith("All players"):
            return 31
        else:
            return 32
    elif input_str.startswith("The"):
        if input_str.startswith("The 1st time"):
            return 33
        else:
            return 34
    elif input_str.startswith("You"):
        if input_str.startswith("You start knowing"):
            return 1
        elif input_str.startswith("You think"):
            return 12
        elif input_str.startswith("You are"):
            return 13
        elif input_str.startswith("You have"):
            return 14
        elif input_str.startswith("You do not know"):
            return 15
        elif input_str.startswith("You might"):
            return 16
        else:
            return 17
    elif input_str.startswith("Each"):
        if input_str.startswith("Each night"):
            if input_str.startswith("Each night*"):
                return 3
            else:
                return 2
        elif input_str.startswith("Each day"):
            return 4
    elif input_str.startswith("Once per game"):
        if input_str.startswith("Once per game, at night"):
            if input_str.startswith("Once per game, at night*"):
                return 7
            else:
                return 6
        elif input_str.startswith("Once per game, during the day"):
            return 8
        else:
            return 9
    elif input_str.startswith("Once per day"):
        return 5
    elif input_str.startswith("On your 1st"):
        if input_str.startswith("On your 1st night"):
            return 10
        elif input_str.startswith("On your 1st day"):
            return 11
    elif input_str.startswith("When"):
        if input_str.startswith("When you die"):
            return 18
        elif input_str.startswith("When you learn that you died"):
            return 19
        else:
            return 20
    elif input_str.startswith("Minions"):
        return 35
    else:
        return 36