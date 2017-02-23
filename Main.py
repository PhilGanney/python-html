#website html is basically just made up of strings, so we can use python variables and the format function to make up html that we could copy out and save as web pages
htmlP = "<p class=\"{0}\">{1}</p>"

def makeLink(href, text, target = False):
    optionalAttributes = ""
    if target:
        optionalAttributes += ", target=\"" + target + "\""
    return "<a href=\"" + href + "\""+ optionalAttributes  + ">" + text + "</a>" #_blank _parent _self _top"
htmlATest = makeLink("google.com", "click here", "fg")
htmlTemplate3 = "<!DOCTYPE html>\n<html>\n<head>\n<title>{0}</title>\n</head>\n<body>{1}</body>\n</html>"
openingParagraph = htmlP.format("content", "Hello and welcome to our awesome website")
#print(htmlTemplate3.format("Python generated Site", openingParagraph))
print(htmlATest)
