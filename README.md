# VietSubLabView
B1: extract rc2 from exe file 
B2: use readRSRC.py tool to extract resource
B3: unzip file 'resource'.bin from B2
B4: copy file .vi to translate folder and use tool Translate.py to translate
B5: copy back translated .vi file to original folder
B6: zip folder in B3
B7: use tool pkzip to comment file MAIN.VI : "toplevel"
B8: use readRSRC.py tool to create resource from B2
B9: replace resource file in exe file in B1