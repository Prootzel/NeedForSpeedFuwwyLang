# translates the text and directly writes it to a file named "furry.csv"
# in post, you need to replace the garbage leftovers using Frosty's mod editor yourself
# cause I couldn't figure out how to make it work

# replace it with the raw file name
rawFile = "rawFile.csv"

furryFile = "furry.csv"

with open(rawFile, "r") as untranslated, open(furryFile, "w") as translated:
    # open the untranslated file
    bigText = untranslated.read()

    # replace all the symbols with corresponding furry ones
    # TODO: multi-symbol replacements, e.g. "?" with " owo?"; it caused random characters to appear so far
    bigText = bigText.replace("l", "w").replace("L", "W").replace("r", "w").replace("R", "W")

    # write the translated text to file
    translated.write(bigText)




