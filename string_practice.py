text = """
    David told his son Solomon that he would be 
    successful only as long as he obeyed Jehovah God. 
    Sadly, later in life Solomon turned to other gods. 
    Jehovah withdrew his favor, and Solomon lost the 
    wisdom to govern in righteousness and justice. 
    (1 Ki. 11:9, 10; 12:4) What is the lesson for us? 
    Obedience leads to success. (Ps. 1:1-3) 
    Of course, Jehovah has not promised to give us 
    the riches and the glory of Solomon. 
    But if we obey our God, he will give us wisdom 
    that will enable us to make sound decisions. 
    (Prov. 2:6, 7; Jas. 1:5) His principles can guide 
    us in such practical matters as employment, education, 
    entertainment, and money. 
    Applying godly wisdom will protect us from lasting harm. 
    (Prov. 2:10, 11) We will cultivate strong friendships. 
    And we will have the guidance we need for a happy 
    family life. w24.11 10-11 ¶11-12
"""

# 1. Extract all the bible verses in this text
# 2. Replace names (Solomon, David) with (Albert, Einstein)
# 3. Count all the occurence of "Jehovah" in the text
# 4. Extract all words longer than 5 characters to a new list
# 5. We want to encript this text, mask all occurrence of "will" with asterisk "****"

text = """
    David told his son Solomon that he would be 
    successful only as long as he obeyed Jehovah God. 
    Sadly, later in life Solomon turned to other gods. 
    Jehovah withdrew his favor, and Solomon lost the 
    wisdom to govern in righteousness and justice. 
    (1 Ki. 11:9, 10; 12:4) What is the lesson for us? 
    Obedience leads to success. (Ps. 1:1-3) 
    Of course, Jehovah has not promised to give us 
    the riches and the glory of Solomon. 
    But if we obey our God, he will give us wisdom 
    that will enable us to make sound decisions. 
    (Prov. 2:6, 7; Jas. 1:5) His principles can guide 
    us in such practical matters as employment, education, 
    entertainment, and money. 
    Applying godly wisdom will protect us from lasting harm. 
    (Prov. 2:10, 11) We will cultivate strong friendships. 
    And we will have the guidance we need for a happy 
    family life. w24.11 10-11 ¶11-12 """
# new_text = text.replace("will", "****")
# new_text = new_text.replace("Solomon", "Albert") 
# new_text = new_text.replace("David", "Einstein")
# print(new_text)
# name = "Jehovah"
# counts = text.count (name)
# print(f"number of times {name} appears in the String is {counts} times")

word_list = text\
				.replace(".", "")\
				.replace(",", "")\
				.replace("¶", "")\
				.replace("0", "")\
				.replace("1", "")\
				.replace("2", "")\
				.replace("3", "")\
				.replace("4", "")\
				.replace(":", "")\
				.replace("-", "")\
				.replace(")", "")\
				.replace("(", "")\
				.split()

words_above_5_chars = []

# 1. Go though each word: Done
# 2. Count how many chars are in each word: Done
# 3. Compare the count/length with 5 (len > 5), if true append to new list
# 4. Filter out unwanted chars 

#  for, while

# for word in word_list:
# 	length = len(word)

# 	if length >= 5:
# 		words_above_5_chars.append(word)

# 	# print(f"{word.upper()}: {len(word)}")

# print(words_above_5_chars)
