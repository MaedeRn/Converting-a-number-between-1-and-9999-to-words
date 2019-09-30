def convert_number_to_words(n):
    
    number_th = n // 1000
    number_th_remainder = n % 1000

    number_hun = number_th_remainder // 100
    number_hun_remainder = number_th_remainder % 100

    number_tens = number_hun_remainder // 10
    number_tens_remainder = number_hun_remainder % 10

    word = ""

    if number_th != 0:
        if number_th == 1:
            word = word + " " + "one"
                        
        elif number_th == 2:
            word = word + " " + "two"
        elif number_th == 3:
            word = word + " " + "three"
        elif number_th == 4:
            word = word + " " + "four"
        elif number_th == 5:
            word = word + " " + "five"
        elif number_th == 6:
            word = word + " " + "six"
        elif number_th == 7:
            word = word + " " + "seven"
        elif number_th == 8:
            word = word + " " + "eight"
        elif number_th == 9:
            word = word + " " + "nine"

        word = word + " " + "thousand"
                    


    if number_hun != 0:
        if number_hun == 1:
            word = word + " " + "one"
                    
        elif number_hun == 2:
            word = word + " " + "two"
        elif number_hun == 3:
            word = word +" " +  "three"
        elif number_hun == 4:
            word = word + " " + "four"
        elif number_hun == 5:
            word = word + " " + "five"
        elif number_hun == 6:
            word = word + " " + "six"
        elif number_hun == 7:
            word = word + " " +"seven"
        elif number_hun == 8:
            word = word + " " + "eight"
        elif number_hun == 9:
            word = word + " " + "nine"

        word = word + " " + "hundred"

    if number_tens != 0:

        if number_tens == 2:
            word = word + " " + "twenty"
        elif number_tens == 3:
            word = word + " " + "thirty"
        elif number_tens == 4:
            word = word + " " + "forty"
        elif number_tens == 5:
            word = word + " " + "fifty"
        elif number_tens == 6:
            word = word + " " + "sixty"
        elif number_tens == 7:
            word = word + " " + "seventy"
        elif number_tens == 8:
            word = word + " " + "eighty"
        elif number_tens == 9:
            word = word + " " + "ninety"
                        
        elif number_tens == 1:
            if number_tens_remainder == 0:
                word = word + " " + "ten"
            elif number_tens_remainder == 1:
                word = word + " " + "eleven"
            elif number_tens_remainder == 2:
                word =  word + " " + "twelve"
            elif number_tens_remainder == 3:
                word = word + " " + "thirteen"
            elif number_tens_remainder == 4:
                word = word + " " + "fourteen"
            elif number_tens_remainder == 5:
                word = word + " " + "fifteen"
            elif number_tens_remainder == 6:
                word = word + " " + "sixteen"
            elif number_tens_remainder == 7:
                word = word + " " + "seventeen"
            elif number_tens_remainder == 8:
                word = word + " " + "eighteen"
            elif number_tens_remainder == 9:
                word = word + " " + "nineteen"
                    

    if number_tens != 1  and number_tens_remainder != 0:
        
        if number_tens_remainder == 1:
            word = word + " " + "one"
        if number_tens_remainder == 2:
            word = word + " " + "two"
        elif number_tens_remainder == 3:
            word = word + " " + "three"
        elif number_tens_remainder == 4:
            word = word + " " + "four"
        elif number_tens_remainder == 5:
            word = word + " " + "five"
        elif number_tens_remainder == 6:
            word = word + " " + "six"
        elif number_tens_remainder == 7:
            word = word + " " + "seven"
        elif number_tens_remainder == 8:
            word = word + " " + "eight"
        elif number_tens_remainder == 9:
            word = word + " " + "nine"
                        
    return word


