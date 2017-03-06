#code released on github as "python-html" (with a MIT liscence) and sololearn code playground as "(add to me) python writing html" (plus a version number). Use, alter, "fork" and save as however you please, but don't claim credit for the stuff I've done

import re #regex comparisons used for checking frame names are valid

#website html is basically just made up of strings, so we can use python variables and the format function to make up html that we could copy out and save as web pages
htmlP = "<p class=\"{0}\">{1}</p>"

#does some validation before calling makeLink (for HTML5 valid links)
def makeLinkVal(href, text, target = False):
    
    if target:
        #check that the target is a viable choice: while there is a list of targets, one option is a framename - and this can be anything with no whitespace, and that covers all other possibilities
        regexForFrameNames = r"^[\S]+$" #in html5 only restriction is no whitespace -html4 specified other rules,
        
        if re.match(regexForFrameNames, target):
            print("a target was input, and is valid for HTML5")
        else:
            print("Invalid HTML warning: Whitesapce found in input: Valid HTML5 anchor targets need either _blank, _parent, _self, _top or a framename - and framenames can't have whitespace")
    return makeLink(href, text, target)
    
#like makeLinkVal this does some validation before calling makeLink, however hyperlinks require different validation in HTML4
def makeLinkValHTML4(href, text, target = False):
    
    if target:
        #check that the target is a viable choice: either an exact match in the list of targets or a name of an html frame on the page that it can go to
        regexForFrameNames = r"^[A-Za-z][\w\-\:\.]*$" #HTML4 specifies first char is a letter, rest is a letter or number or - dash : colon . full stop
        
        targetOptions = ["_blank", "_parent","_self", "_top"]
#code released on github as "python-html" (with a MIT liscence) and sololearn code playground as "(add to me) python writing html" (plus a version number). Use, alter, "fork" and save as however you please, but don't claim credit for the stuff I've done

import re #regex comparisons used for checking frame names are valid

#website html is basically just made up of strings, so we can use python variables and the format function to make up html that we could copy out and save as web pages
htmlP = "<p class=\"{0}\">{1}</p>"

#does some validation before calling makeLink (for HTML5 valid links)
def makeLinkVal(href, text, target = False):
    
    if target:
        #check that the target is a viable choice: while there is a list of targets, one option is a framename - and this can be anything with no whitespace, and that covers all other possibilities
        regexForFrameNames = r"^[\S]+$" #in html5 only restriction is no whitespace -html4 specified other rules,
        
        if re.match(regexForFrameNames, target):
            print("a target was input, and is valid for HTML5")
        else:
            print("Invalid HTML warning: Whitesapce found in input: Valid HTML5 anchor targets need either _blank, _parent, _self, _top or a framename - and framenames can't have whitespace")
    return makeLink(href, text, target)
    
#like makeLinkVal this does some validation before calling makeLink, however hyperlinks require different validation in HTML4
def makeLinkValHTML4(href, text, target = False):
    
    if target:
        #check that the target is a viable choice: either an exact match in the list of targets or a name of an html frame on the page that it can go to
        regexForFrameNames = r"^[A-Za-z][\w\-\:\.]*$" #HTML4 specifies first char is a letter, rest is a letter or number or - dash : colon . full stop
        
        targetOptions = ["_blank", "_parent","_self", "_top"]
        if target not in targetOptions:
            #check the frame name is possibly a frame name
            if re.match(regexForFrameNames, target):
                print("target is valid HTML4 for a frame name")
            else:
                print("target provided is not _blank, _parent, _self, _top or a valid framename for HTML4, regex used for testing framenames is: " + regexForFrameNames)
    return makeLink(href, text, target)    

#use directly if you don't want any validation, otherwise use makeLinkVal for HTML5 compliance validation or makeLinkValHTML4 for HTML4 compliance validation
def makeLink(href, text, target = False): 
    #print("makeLink called: href {}, text {}, target {}".format(href, text, target))
    optionalAttributes = ""
    if target:
    #targets: _blank, _parent, _self, _top, framename
        # put the target and the attribute "target" into a string for adding into the main anchor tag
        optionalAttributes += ", target=\"" + target + "\""
    return "<a href=\"" + href + "\""+ optionalAttributes  + ">" + text + "</a>" #_blank _parent _self _top"
    
####ONLY TEST AND DEMO CODE BELOW THIS   
##
##
#Everything below here is only run when this file is called as a script
#This files purpose is as a module, so everything beneath here is for testing the module
if __name__=="__main__":
    htmlATest = makeLinkValHTML4("google.com", "click here", "_Frame1_2")
    htmlTemplate3 = "<!DOCTYPE html>\n<html>\n<head>\n<title>{0}</title>\n</head>\n<body>{1}</body>\n</html>"
    openingParagraph = htmlP.format("content", "Hello and welcome to our awesome website")
    #print(htmlTemplate3.format("Python generated Site", openingParagraph))
    print(htmlATest)
    #following function to be used as a second part of assert conditions only (asserts aren't usually run in live public code so we dont want this to print when no assert has happened)
    def assertSuccess(msg='assert OK'): 
        print (msg)
        return True

    expectedString = "<a href=\"google.com\", target=\"Frame1_2\">click here</a>"
    assert htmlATest == expectedString and assertSuccess("Anchor tag code with target is created as expected"), "Result from function \n {} \n does not match up with expectation \n {}".format(str(htmlATest), expectedString)
