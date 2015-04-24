__author__ = 'sci-lmw1'

filename = "/Users/sci-lmw1/GoogleDrive/CP1406/CP1406 CP2010 2015-1/CP1406 2015-1/Assignments/TownsvilleStudents.csv"
linkBase = "<li><a href=\"http://ditwebtsv.jcu.edu.au/~"
topSection = """<!doctype html>
<html>
<head>
<title>CP1406/CP2010 - 2015 - Assignment 1 Links</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
    <style type="text/css">
        body { font-family: Arial; margin-left: 3em; }
        h1, h2 { margin-left: -1em; }
        h2 { margin-top: 1.5em; margin-bottom: 0.5em; }
    </style>
</head>

<body>
    <h1>CP1406/CP2010 - 2015 - Assignment 1 Links</h1>
    <ol>\n"""
bottomSection = """</ol>
</body>
</html>\n"""

inFile = open(filename, 'r')
outFile = open("TownsvilleA1links.html", 'w')

outFile.write(topSection + "\n")
for line in inFile:
    parts = line.split(",")
    # print(parts)
    linkLine = linkBase + parts[2].strip() + "/a1/plan.html\" target=\"_blank\">" + parts[1] + " " + parts[0] + " (" + parts[2].strip() + ")</a></li>"
    outFile.write(linkLine + "\n")
outFile.write(bottomSection)
inFile.close()
outFile.close()
