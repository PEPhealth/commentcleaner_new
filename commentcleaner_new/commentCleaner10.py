# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 22:27:52 2018

@author: Alex
"""

def commentCleaner(x,y):

    # convert to lower case (yes something is lost but helps)
    #x[y] = x[y].str.lower()

    # Remove URLs
    #x[y] = x[y].replace(r"http\S+", "", regex=True)

    # Sort out multiple backslashes (two backslashes is the regex equivalent of a single backslash:
    # "\\" in the regex world = "\" is the normal text world)
    x[y] = x[y].replace("\\\\\\", "\\")
    x[y] = x[y].replace("\\\\","\\")
  
    # Remove HTML tags
    x[y] = x[y].replace(r"<.+?>", "",regex=True)
    
    # floating apostrophe / single quotation mark    
    x[y] = x[y].replace(" ' ","'", regex=True)
       
    # Cleaning the text
    x[y] = x[y].replace("&amp;", "&", regex=True)
    x[y] = x[y].replace('\&quot;','"', regex=True)
    x[y] = x[y].replace("\&#039;","'", regex=True)
    x[y] = x[y].replace("\&amp;","&", regex=True)
    x[y] = x[y].replace("\&lt;","<", regex=True)
    x[y] = x[y].replace("&lt", "<")
    x[y] = x[y].replace("\&gt;",">", regex=True)
    x[y] = x[y].replace("\&tilde;","˜", regex=True)
    x[y] = x[y].replace("\&ndash;","–", regex=True)
    x[y] = x[y].replace("\&mdash;","–", regex=True)

    x[y] = x[y].replace("\r"," ", regex=True)
    x[y] = x[y].replace(r"\\r"," ", regex=True)
    x[y] = x[y].replace("\n"," ", regex=True)
    x[y] = x[y].replace(r"\\n"," ", regex=True)
    x[y] = x[y].replace("\t"," ", regex=True)
    x[y] = x[y].replace(r"\\t"," ", regex=True)
    x[y] = x[y].replace('"',"", regex=True)


    # Emoticons (not emojis)
    x[y] = x[y].replace("<8","HEART", regex=True)
    x[y] = x[y].replace("8>","HEART", regex=True)
    x[y] = x[y].replace("<3","HEART", regex=True)
    x[y] = x[y].replace(":\)","HAPPY", regex=True)
    x[y] = x[y].replace(":-\)","HAPPY", regex=True)
    x[y] = x[y].replace(";\)","WINK", regex=True)
    x[y] = x[y].replace(";-\)","WINK", regex=True)
    x[y] = x[y].replace(":-\(","SAD", regex=True)
    x[y] = x[y].replace(":\(","SAD", regex=True)
    x[y] = x[y].replace("gr8","GREAT", regex=True)

    # pound sign
    x[y] = x[y].replace('&#163;','£',regex=True)
    
    # hard space (one that can't be broken by wrapping text) 
    x[y] = x[y].replace('&nbsp;',' ',regex=True)
    
    # Random patient opinion hard space:
    x[y] = x[y].replace('&#160;',' ',regex=True)
     
    ## Weird punctuation?
    x[y] = x[y].replace("’","'", regex=True)
   # x[y] = x[y].replace(r'(\w)(\?)(s)(\s)', r"\1's ", regex=True)
    
    ## no space after colon when a letter either side of it
    x[y] = x[y].replace(r'([a-zA-Z]\:)([a-zA-Z])', r'\1 \2', regex=True)
#    ## lowercase letter immediately followed by uppercase letter (i.e. no space) seperated with a fullstop
#    ## and space immediately after the lowercase letter
#    x[y] = x[y].replace(r'([a-z])([A-Z])', r'\1. \2', regex=True)
    ## words seperated by a back or forward slash and no spaces now seperate by spaces and a forwardslash
    x[y] = x[y].replace(r'([a-zA-Z])(\\)([a-zA-Z])', r'\1 / \3', regex=True)
    x[y] = x[y].replace(r'([a-zA-Z])(\/)([a-zA-Z])', r'\1 / \3', regex=True)
    ## brackets immediately preceded or followed by any letter (i.e. no space) seperated with a space
    x[y] = x[y].replace(r'([a-zA-Z])(\()', r'\1 \2', regex=True)
    x[y] = x[y].replace(r'(\))([a-zA-Z])', r'\1 \2', regex=True)

    x[y] = x[y].replace("\r","", regex=True)
    x[y] = x[y].replace("\n","", regex=True)
    x[y] = x[y].replace("\t","", regex=True)
    ##x[y] = x[y].replace('"',"", regex=True)



    # no space after colon when a letter either side of it
    #x[y] = x[y].replace(r'([a-zA-Z]\:)([a-zA-Z])', r'\1 \2', regex=True)

#    # lowercase letter immediately followed by uppercase letter (i.e. no space) seperated with a fullstop
#    # and space immediately after the lowercase letter
#    x[y] = x[y].replace(r'([a-z])([A-Z])', r'\1. \2', regex=True)

    # words seperated by a back or forward slash and no spaces now seperate by spaces and a forwardslash
    #x[y] = x[y].replace(r'([a-zA-Z])(\\)([a-zA-Z])', r'\1 / \3', regex=True)
    #x[y] = x[y].replace(r'([a-zA-Z])(\/)([a-zA-Z])', r'\1 / \3', regex=True)

    # brackets immediately preceded or followed by any letter (i.e. no space) seperated with a space
    #x[y] = x[y].replace(r'([a-zA-Z])(\()', r'\1 \2', regex=True)
    #x[y] = x[y].replace(r'(\))([a-zA-Z])', r'\1 \2', regex=True)

#    ## Getting rid of whatever you call these
##    x[y] = x[y].replace("i'm","i am",regex=True)
##    x[y] = x[y].replace("i\?m","i am",regex=True)
##    x[y] = x[y].replace("he's","he is",regex=True)
##    x[y] = x[y].replace("he\?s","he is",regex=True)
##    x[y] = x[y].replace("it's","it is",regex=True)
##    x[y] = x[y].replace("it\?s","it is",regex=True)
##    x[y] = x[y].replace("you're","you are",regex=True)
##    x[y] = x[y].replace("you\?re","you are",regex=True)
##    x[y] = x[y].replace("we're","we are",regex=True)
##    x[y] = x[y].replace("we\?re","we are",regex=True)
##    x[y] = x[y].replace("they're","they are",regex=True)
##    x[y] = x[y].replace("they\?re","they are",regex=True)
##    x[y] = x[y].replace("i\?ve ","i have ",regex=True)
##    x[y] = x[y].replace("iv ","i have ",regex=True)
##    x[y] = x[y].replace("i've","i have",regex=True)
##    x[y] = x[y].replace("you've","you have",regex=True)
##    x[y] = x[y].replace("you\?ve","you have",regex=True)
##    x[y] = x[y].replace("we've","we have",regex=True)
##    x[y] = x[y].replace("we\?ve","we have",regex=True)
##    x[y] = x[y].replace("they've","they have",regex=True)
##    x[y] = x[y].replace("they\?ve","they have",regex=True)
##    x[y] = x[y].replace("could've","could have",regex=True)
##    x[y] = x[y].replace("could\?ve","could have",regex=True)
##    x[y] = x[y].replace("should've","should have",regex=True)
##    x[y] = x[y].replace("should\?ve","should have",regex=True)
##    x[y] = x[y].replace("would've","would have",regex=True)
##    x[y] = x[y].replace("would\?ve","would have",regex=True)
##    x[y] = x[y].replace("can't","cannot",regex=True)
##    x[y] = x[y].replace("can\?t","cannot",regex=True)
##    x[y] = x[y].replace("won't","will not",regex=True)
##    x[y] = x[y].replace("won\?t","will not",regex=True)
##    x[y] = x[y].replace("don't","do not",regex=True)
##    x[y] = x[y].replace("don\?t","do not",regex=True)
##    x[y] = x[y].replace("doesn't","does not",regex=True)
##    x[y] = x[y].replace("doesn\?t","does not",regex=True)
##    x[y] = x[y].replace("wasn't","was not",regex=True)
##    x[y] = x[y].replace("wasn\?t","was not",regex=True)
##    x[y] = x[y].replace("isn't","is not",regex=True)
##    x[y] = x[y].replace("isn\?t","is not",regex=True)
##    x[y] = x[y].replace("aren't","are not",regex=True)
##    x[y] = x[y].replace("aren\?t","are not",regex=True)
##    x[y] = x[y].replace("shan't","shall not",regex=True)
##    x[y] = x[y].replace("shan\?t","shall not",regex=True)
##    x[y] = x[y].replace("shouldn't","should not",regex=True)
##    x[y] = x[y].replace("shouldn\?t","should not",regex=True)
##    x[y] = x[y].replace("wouldn't","would not",regex=True)
##    x[y] = x[y].replace("wouldn\?t","would not",regex=True)
##    x[y] = x[y].replace("couldn't","could not",regex=True)
##    x[y] = x[y].replace("couldn\?t","could not",regex=True)
##    x[y] = x[y].replace("haven't","have not",regex=True)
##    x[y] = x[y].replace("haven\?t","have not",regex=True)
##    x[y] = x[y].replace("didn't","did not",regex=True)
##    x[y] = x[y].replace("didn\?t","did not",regex=True)
##    x[y] = x[y].replace("weren't","were not",regex=True)
##    x[y] = x[y].replace("weren\?t","were not",regex=True)
#
    # Wrong use of apostrophe and it's a questions mark!
#    x[y] = x[y].replace("patient\?s","patient's",regex=True)
#    x[y] = x[y].replace("outpatient\?s","outpatient's",regex=True)
#    x[y] = x[y].replace("people\?s","people's",regex=True)
#    x[y] = x[y].replace("dr\?s","drs",regex=True)
#    x[y] = x[y].replace(" doc's "," drs ",regex=True)
#    x[y] = x[y].replace(" docs "," drs ",regex=True)
#
#    # The special case that is the multiple spellings of A&E
#    x[y] = x[y].replace(" a & e"," a&e", regex=True)    
#    x[y] = x[y].replace("a@e","a&e", regex=True)
#    x[y] = x[y].replace(" a& e"," a&e", regex=True)
#    x[y] = x[y].replace(" a and e"," a&e", regex=True)
#    x[y] = x[y].replace(" aande"," a&e", regex=True)
#    x[y] = x[y].replace(" a\+e"," a&e", regex=True)
#    x[y] = x[y].replace(" a\+ e"," a&e", regex=True)
#    x[y] = x[y].replace("a& e ","a&e ", regex=True)
#    x[y] = x[y].replace("a and e ","a&e ", regex=True)
#    x[y] = x[y].replace("aande ","a&e ", regex=True)
#    x[y] = x[y].replace("a\+e ","a&e ", regex=True)
#    x[y] = x[y].replace("a\+ e ","a&e ", regex=True)


    # Sort out the random spacing around question marks, exclamation marks and commas
    x[y] = x[y].replace("\?","? ",regex=True)
    x[y] = x[y].replace("\? ","? ",regex=True)
    x[y] = x[y].replace(" \?","?",regex=True)
    
    x[y] = x[y].replace("\?\s\s\s\)","?)",regex=True)
    x[y] = x[y].replace("\?\s\s\)","?)",regex=True)
    x[y] = x[y].replace("\?\s\)","?)",regex=True)
    
    x[y] = x[y].replace("\!","! ",regex=True)
    x[y] = x[y].replace("\! ","! ",regex=True)
    x[y] = x[y].replace(" \!","!",regex=True)

    x[y] = x[y].replace("\!\s\s\s\)","!)",regex=True)
    x[y] = x[y].replace("\!\s\s\)","!)",regex=True)
    x[y] = x[y].replace("\!\s\)","!)",regex=True)

    x[y] = x[y].replace("\,",", ",regex=True)
    x[y] = x[y].replace("\, ",", ",regex=True)
    x[y] = x[y].replace(" \,",",",regex=True)

    # Prevent % meaning lost when punctuation is stripped@
    x[y] = x[y].replace("%"," percent",regex=True)

    ## Sorting out the issues with fullstops:
    # Any fullstop not preceded by a number made into a fullstop followed by a space
    #x[y] = x[y].replace("(?<!(\d))\.",". ",regex=True)
    #x[y] = x[y].replace(r'(\w+)(\.)([a-zA-Z])', r'\1. \3', regex=True)

    # Replace any fullstop followed by two spaces (which all previous fullstops followed by a single space
    # now are following the above line) with a fullstop followed by a single space.
    x[y] = x[y].replace("\.\s\s",". ",regex=True)


    # Every day speech acronyms
#    x[y] = x[y].replace("e\. g\. ","eg ",regex=True)
#    x[y] = x[y].replace(" eg\. "," eg ",regex=True)
#    x[y] = x[y].replace(" e\.g "," eg ",regex=True)
#    x[y] = x[y].replace(" e\. g "," eg ",regex=True)
#    x[y] = x[y].replace(" e g "," eg ",regex=True)
#    x[y] = x[y].replace("i\. e\. ","ie ",regex=True)
#    x[y] = x[y].replace(" ie\. "," ie ",regex=True)
#    x[y] = x[y].replace(" i\.e "," ie ",regex=True)
#    x[y] = x[y].replace(" i\. e "," ie ",regex=True)
#    x[y] = x[y].replace(" i e "," ie ",regex=True)
#    x[y] = x[y].replace("etc\. ","etc ",regex=True)
#    x[y] = x[y].replace("esp\. ","esp ",regex=True)
#    x[y] = x[y].replace("p\. s\. ","ps ",regex=True)
#    x[y] = x[y].replace("p\. s","ps ",regex=True)
#    x[y] = x[y].replace("a\. s\. a\. p\. ","asap ",regex=True)
#
#    #x[y] = x[y].replace("A\. S\. A\. P\. ","asap ",regex=True)
#    # External parties acronyms
#    x[y] = x[y].replace("m\. p\. ","mp ",regex=True)
#    x[y] = x[y].replace("m\. p ","mp ",regex=True)
#    x[y] = x[y].replace("g\. p\. ","gp ",regex=True)
#    x[y] = x[y].replace("g\. p ","gp ",regex=True)
#    x[y] = x[y].replace("c\. q\. c\. ","cqc ",regex=True)
#    x[y] = x[y].replace("n\. h\. s\. ","nhs ",regex=True)
#    x[y] = x[y].replace("n\. h\. s ","nhs ",regex=True)
#
#    # General other noun acronyms
#    x[y] = x[y].replace("t\. v\. ","tv ",regex=True)
#
#    #x[y] = x[y].replace("T\. v\. ","TV ",regex=True)
#    x[y] = x[y].replace("t\. v ","tv ",regex=True)
#
#    # Hospital name acronyms
#    x[y] = x[y].replace("g\. w\. h\. ","gwh ",regex=True)

    # Hospital department acronyms
    x[y] = x[y].replace("a\. a\. u\. ","aau ",regex=True)
    x[y] = x[y].replace("a\. c\. a\. d\. ","acad ",regex=True)
    x[y] = x[y].replace("a\. m\. u\. ","amu ",regex=True)
    x[y] = x[y].replace("a\. t\. u\. ","atu ",regex=True)
    x[y] = x[y].replace("c\. c\. u\. ","ccu ",regex=True)
    x[y] = x[y].replace("c\. d\. u\. ","cdu ",regex=True)
    x[y] = x[y].replace("e\. c\. g\. ","ecg ",regex=True)
    x[y] = x[y].replace("e\. n\. t\. ","ent ",regex=True)
    x[y] = x[y].replace("e\. n\. t ","ent ",regex=True)
    x[y] = x[y].replace("e\. s\. a\. u\. ","esau ",regex=True)
    x[y] = x[y].replace("i\. c\. u\. ","icu ",regex=True)
    x[y] = x[y].replace("m\. r\. s\. a\. ","mrsa ",regex=True)
    x[y] = x[y].replace("s\. a\. u\. ","sau ",regex=True)
    x[y] = x[y].replace("s\. t\. i\. ","sti ",regex=True)

    # General terms that may benefit from consistency
    x[y] = x[y].replace("wi fi","wi-fi",regex=True)
    x[y] = x[y].replace("req'd","required",regex=True)
    x[y] = x[y].replace("req ","required ",regex=True)
    x[y] = x[y].replace("x ray","x-ray",regex=True)
    x[y] = x[y].replace("xray","x-ray",regex=True)
    x[y] = x[y].replace("ex ray","x-ray",regex=True)
    x[y] = x[y].replace("ex rays","x-rays",regex=True)
    x[y] = x[y].replace("x rays","x-rays",regex=True)
    x[y] = x[y].replace(r'(\d)(yr )', r'\1 \2', regex=True)
    x[y] = x[y].replace(r'(\d)(yrs )', r'\1 \2', regex=True)
    x[y] = x[y].replace(" yr "," year ",regex=True)
    x[y] = x[y].replace(" yrs "," years ",regex=True)
    x[y] = x[y].replace(r'(\d)(wk )', r'\1 \2', regex=True)
    x[y] = x[y].replace(r'(\d)(wks )', r'\1 \2', regex=True)
    x[y] = x[y].replace(" wk "," week ",regex=True)
    x[y] = x[y].replace(" wks "," weeks ",regex=True)
    x[y] = x[y].replace(r'(\d)(hr )', r'\1 \2', regex=True)
    x[y] = x[y].replace(r'(\d)(hrs )', r'\1 \2', regex=True)
    x[y] = x[y].replace(" hr "," hour ",regex=True)
    x[y] = x[y].replace(" hrs "," hours ",regex=True)
    x[y] = x[y].replace(" dr's "," drs ",regex=True)
    x[y] = x[y].replace(" dep "," department ",regex=True)
    x[y] = x[y].replace(" dept "," department ",regex=True)
    x[y] = x[y].replace(" deps "," departments ",regex=True)
    x[y] = x[y].replace(" depts "," departments ",regex=True)

    # Days of the week - NB 'sat' and 'sun' aren't amended as they are words in their own right
#    x[y] = x[y].replace(" mon "," monday ",regex=True)
#    x[y] = x[y].replace(" tue "," tuesday ",regex=True)
#    x[y] = x[y].replace(" tues "," tuesday ",regex=True)
#    x[y] = x[y].replace(" wed "," wednesday ",regex=True)
#    x[y] = x[y].replace(" weds "," wednesday ",regex=True)
#    x[y] = x[y].replace(" thu "," thursday ",regex=True)
#    x[y] = x[y].replace(" thurs "," thursday ",regex=True)
#    x[y] = x[y].replace(" fri "," friday ",regex=True)

    # Abbreviations found in text
    x[y] = x[y].replace(" hosp "," hospital ",regex=True)

    ## Phrases/words that can be spelt more than one way that nead to be homogenised to improve predicitions
    # 'spic and span' to become 'spick and span'
    x[y] = x[y].replace(" spic "," spick ",regex=True)
    x[y] = x[y].replace("Spic ","Spick ",regex=True)
    x[y] = x[y].replace(" mold "," mould ",regex=True)
    x[y] = x[y].replace(" moldy "," mouldy ",regex=True)
    x[y] = x[y].replace("canula","cannula",regex=True)

    ## Space between numbers and units removed, e.g. '10 pm' becomes '10pm'
    # any unit two digit unit ending in 'm', e.g. mm, cm, am, pm
#    x[y] = x[y].replace(r'(\d)( )([a-zA-Z]m\s)', r'\1\3', regex=True)
#    x[y] = x[y].replace(r'(\d)( )([a-zA-Z]m\.)', r'\1\3', regex=True)
#
#    # any unit two digit unit ending in 'g', e.g. mg, kg
#    x[y] = x[y].replace(r'(\d)( )([a-zA-Z]g\s)', r'\1\3', regex=True)
#    x[y] = x[y].replace(r'(\d)( )([a-zA-Z]g\.)', r'\1\3', regex=True)
#
#    # any unit two digit unit ending in 'l', e.g. ml
#    x[y] = x[y].replace(r'(\d)( )([a-zA-Z]l\s)', r'\1\3', regex=True)
#    x[y] = x[y].replace(r'(\d)( )([a-zA-Z]l\.)', r'\1\3', regex=True)
#    

    # Assorted unicode that seems to affect Facebook:
    x[y] = x[y].replace('\\ufffd','',regex=True)
    x[y] = x[y].replace('\\xa3','',regex=True)

    x[y] = x[y].replace(r"\\xa0", " ", regex=True)
    x[y] = x[y].replace(r"\\xa", " ", regex=True)
    
    x[y] = x[y].replace(r"\\xe9", "é", regex=True)
    x[y] = x[y].replace(r"\\xe8", "è", regex=True)
    x[y] = x[y].replace(r"\\xe4", "ä", regex=True)


    x[y] = x[y].replace("1f3fb", "", regex=True)
    

    # Remove multiple spaces
    x[y] = x[y].replace("          ", " ",regex=True)
    x[y] = x[y].replace("         ", " ",regex=True)
    x[y] = x[y].replace("        ", " ",regex=True)
    x[y] = x[y].replace("       ", " ",regex=True)
    x[y] = x[y].replace("      ", " ",regex=True)
    x[y] = x[y].replace("     ", " ",regex=True)
    x[y] = x[y].replace("    ", " ",regex=True)
    x[y] = x[y].replace("   ", " ",regex=True)
    x[y] = x[y].replace("  ", " ",regex=True)
    
    
    x[y] = x[y].replace("          ", " ")
    x[y] = x[y].replace("         ", " ")
    x[y] = x[y].replace("        ", " ")
    x[y] = x[y].replace("       ", " ")
    x[y] = x[y].replace("      ", " ")
    x[y] = x[y].replace("     ", " ")
    x[y] = x[y].replace("    ", " ")
    x[y] = x[y].replace("   ", " ")
    x[y] = x[y].replace("  ", " ")
    
    

    x[y] = x[y].replace('www. ', 'www.', regex=True)
    x[y] = x[y].replace('t.co / ', 't.co/', regex=True)

    
    
#    x[y] = x[y].replace("http:\/\/t\.\sco\s\/\s", "http://t.co/", regex=True)
#    x[y] = x[y].replace("https:\/\/t\.\sco\s\/\s", "https://t.co/", regex=True)
#    
#    x[y] = x[y].replace("http:\/\/t\.\sco\s\/", "http://t.co/", regex=True)
#    x[y] = x[y].replace("https:\/\/t\.\sco\s\/", "https://t.co/", regex=True)

    #x[y] = x[y].replace("t. co", "t.co")

    
    #tweetsDF['unicodeCommentCleaned'] = tweetsDF['unicodeCommentCleaned'].replace(r"\\u2018", "'", regex=True)
#tweetsDF['unicodeCommentCleaned'] = tweetsDF['unicodeCommentCleaned'].replace(r"\\u2019", "'", regex=True)
#tweetsDF['unicodeCommentCleaned'] = tweetsDF['unicodeCommentCleaned'].replace(r"\\'", "'", regex=True)
#
#tweetsDF['unicodeCommentCleaned'] = tweetsDF['unicodeCommentCleaned'].replace(r'\\\\u000', ' ', regex=True)
#tweetsDF['unicodeCommentCleaned'] = tweetsDF['unicodeCommentCleaned'].replace(r'\\\\u', ' ', regex=True)
#tweetsDF['unicodeCommentCleaned'] = tweetsDF['unicodeCommentCleaned'].replace(r'\\u000', ' ', regex=True)
#tweetsDF['unicodeCommentCleaned'] = tweetsDF['unicodeCommentCleaned'].replace(r'\\u', ' ', regex=True)
#
#tweetsDF['unicodeCommentCleaned'] = tweetsDF['unicodeCommentCleaned'].replace(r"\\\\xa0", " ", regex=True)
#tweetsDF['unicodeCommentCleaned'] = tweetsDF['unicodeCommentCleaned'].replace(r"\\\\xa", " ", regex=True)
#tweetsDF['unicodeCommentCleaned'] = tweetsDF['unicodeCommentCleaned'].replace(r"\\\\n", " ", regex=True)
#tweetsDF['unicodeCommentCleaned'] = tweetsDF['unicodeCommentCleaned'].replace(r"\\\\r", " ", regex=True)
#tweetsDF['unicodeCommentCleaned'] = tweetsDF['unicodeCommentCleaned'].replace(r"\\\\t", " ", regex=True)
#
#tweetsDF['unicodeCommentCleaned'] = tweetsDF['unicodeCommentCleaned'].replace(r"\\\\xe9", "e", regex=True)
#tweetsDF['unicodeCommentCleaned'] = tweetsDF['unicodeCommentCleaned'].replace(r"\\\\xe4", "a", regex=True)
#tweetsDF['unicodeCommentCleaned'] = tweetsDF['unicodeCommentCleaned'].replace(r"\\\\xa3", "£", regex=True)
#
#
## Switch to the unicodeCharacters database
#connection = pypyodbc.connect('Driver={SQL Server};'
#                              'Server=rdsstatica.c7hjsq9zmqeu.eu-west-2.rds.amazonaws.com;'
#                              'Database=unicodeCharacters;'
#                              'UID=griff;'
#                              'PWD=Wqsfbh01')
#
#SQLCommand = ("SELECT code, shortName FROM unicodeCharacters") 
#
#cursor.execute(SQLCommand)
#emojis = pd.DataFrame(cursor.fetchall())
#emojis.columns = ['code','shortName']
#
#emojis['code'] = emojis['code'].str.lower()
#
#for row in range(len(emojis)):
#    print('row '+str(row)+' of '+str(len(emojis)))
#    tweetsDF['comment'] = tweetsDF['comment'].replace(emojis['code'][row], str(' '+str(emojis['shortName'][row])+' '), regex=True)
#    
#tweetsDF['comment'] = tweetsDF['comment'].replace(" ' ","'", regex=True)
#
#tweetsDF['comment'] = tweetsDF['comment'].replace('  ', ' ', regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace('  ', ' ', regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace('  ', ' ', regex=True)
#
#
## Cleaning the text
#tweetsDF['comment'] = tweetsDF['comment'].replace(r"http\S+", "", regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace("&amp;", "&", regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace('\&quot;','"', regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace("\&#039;","'", regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace("\&amp;","&", regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace("\&lt;","<", regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace("&lt", "<")
#tweetsDF['comment'] = tweetsDF['comment'].replace("\&gt;",">", regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace("\&tilde;","˜", regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace("\&ndash;","–", regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace("\&mdash;","–", regex=True)
#
## Emoticons
#tweetsDF['comment'] = tweetsDF['comment'].replace("<8","HEART", regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace("8>","HEART", regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace("<3","HEART", regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace(":\)","HAPPY", regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace(":-\)","HAPPY", regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace(";\)","WINK", regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace(";-\)","WINK", regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace(":-\(","SAD", regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace(":\(","SAD", regex=True)
#tweetsDF['comment'] = tweetsDF['comment'].replace("gr8","GREAT", regex=True)
    
    
