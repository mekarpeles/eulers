HUNDRED = "hundred"
ONE_THOUSAND = len("onethousand")

#106 letters in 1 - 19
#7 * 106 + 20
def calc_letters_in_1000():
    ones = ["", "one", "two", "three", "four", "five",
            "six", "seven", "eight", "nine"]
    elevenup = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
                "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty",
            "seventy", "eighty", "ninety"]

    total = 0
    for hundred in ones:
        lh = len(hundred) + len(HUNDRED) + len("and") if hundred else 0

        # 1 - 9
        total += len(reduce(lambda a, b: a + b, ones))
        # there are 9 cases "" case (one hundred) has no and
        total += (lh * len(ones))
       
        # 10-19
        total += len(reduce(lambda a, b: a + b, elevenup))
        total += (lh * len(elevenup))
        
        for ten in tens:
            lt = len(ten)
            for one in ones:
                total += lh + lt + len(one)
                
    # Subtract extra "and"s
    # there are len(ones) case where hundreds, no tens, no ones
    # (e.g. one hundred) -- contains no word 'and'
    total -= len("and") * 9

    return total + ONE_THOUSAND

if __name__ == "__main__":
    print calc_letters_in_1000() #21124
