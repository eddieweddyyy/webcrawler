import re

'''
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group
'''
is_in = re.search('abc', 'abcqwasdf')
startswith = re.findall('^a', 'abcdefg')
endswith = re.findall('g$', 'abcdefg')
find_spcl_chr = re.findall('\$', 'abss$avbge') #Use \
is_or = re.findall('[abc]', 'abcdedfg') #a or b or c
is_low = re.findall('[a-z]', 'qwefasd') #Find lowercase
is_up = re.findall('A-Z', 'ADSFQW') #Find uppercase
is_kr = re.findall('[가-힣ㄱ-ㅎ]', 'asdfqwerdk안녕하세요ㄷㅂㅈ') #Find Korean

is_num = re.findall('[0-9]', 'qdfa13asdf')
is_num2 = re.findall('\d', 'qdfa13asdf') #\d = digit
is_num3 = re.findall('\d\d', 'qdfa13asdf') #2 digits
is_num4 = re.findall('\d{3}', 'qdfa13asd12354432f') #'{}' = multiplication

not_num = re.findall('\D', 'ab12cd34ff') #Anything but numbers
whitespace = re.findall('\s', 'ab12cd34ff  asdf asd') #All white spaces
not_whitespace = re.findall('\S', 'ab12cd34ff  asdf asd') #Anything but white space
repeat = re.findall('a+', 'asdfqwefaaaaaaaaa')
ignorecase = re.findall('abc', 'abcABCabCBAbc', re.IGNORECASE) #Case insensitive

change = re.sub('\-', '.', '2022-1-1')
change2 = re.sub('\d', '', 'AB39370237asd2asdk238vk2') #Remove numbers
change3 = re.sub('\D', '', 'AB39370237asd2asdk238vk2') #Remove anything but numbers

# '^' = 'not' when used in []
isnt_num = re.findall('[^0-9]', 'qdfa13asdf') #find numbers that aren't 0-9

result = re.findall('.+@+.+\.', 'abc@example.com')
print(result)

# print(change3)