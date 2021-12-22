# #########################
# The original Morse Code 
# was invented in 1838 for 
# use in telegraphs by 
# Samuel F.B. Morse. It 
# uses dots and dashes to 
# represent alphanumerical 
# characters.
# 
# Code written for Code 
# Golf (As short as 
# possiple) and 
# entertainment.
# ######################### 

t=lambda x:''.join([' '+['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...','---..','----.','.-.-.-','--..--','..--..','.----.','-.-.--','-..-.','-.--.','-.--.-','.-...','---...','-.-.-.','-...-','.-.-.','-....-','..--.-','...-..-','.--.-.','/']["abcdefghijklmnopqrstuvwxyz0123456789.,?'!/()&:;=+-_$@ ".index(q.lower())]if q!='"'else'.-..-.'for q in x])
print(t(input()))