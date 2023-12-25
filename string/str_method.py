# find() method: --------------->

speech = "If you born poor, it is not your mistake. But if you die poor, it is your mistake"
search = speech.find("die poor")
# print(search)

statement = "I am genius. Everything is possible to me. I can do everything"
search = statement.find("can do")
# print(search)

# replace() method: ------------>

country = "Virgin Island"
new_country = country.replace("Virgin", "Fucked")
# print(new_country)

text = "this is a test. this is another test. this is final test"
new_text = text.replace("this", "This")
# print(new_text)

speech = "Don't chase fucking girls, chase your goals. And fucking girls chase you automtiaclly"
new_speech = speech.replace("fucking", "any")
# print(new_speech)

greet = "Hello"
new_greet = greet.replace("Hello", "hello")
# print(new_greet)

# strip(), lstrip(), rstrip() methods: -------------->

text = "     This is a string.  I am so surprised!"
new_text = text.strip()
# print(new_text)

another_text = "         Her opinion is shit. And she also a shit person"
new_another_text = another_text.lstrip()
# print(new_another_text)

final_text = "Messi is the GOAT. No one plays like him.    "
new_final_text = final_text.rstrip()
# print(new_final_text)

# upper(), lower() and capitalize() methods: ----------->

request = "Hey bitch, what are you doing? I don't want to fuck you. So please don't suck my dick"
request_upper = request.upper()
# print(request_upper)

statement = "A MAN BECOMES MORE POWERFUL WHEN HE LEARNED HOW TO CONTROL HIS EMOTIONS AND IGNORE GIRLS"
statement_lower = statement.lower()
# print(statement_lower)

order = "take this shirt and wash it properly. and it should be cleaned"
cap_order = order.capitalize()
# print(cap_order)

# split() method: ----------->

speech = "I am a programmer and a software engineer"
words = speech.split()
# print(words)

# for word in words:
    # print(word)

# count() method: ---------->

proverb = "If you born poor, it is not your mistake. But if you die poor, it is your mistake"
result = proverb.count("not")
# print(result)

nothing = 'ha ha oh oh oh pa pa pa le le le no no no ah ah ah ah ah ah bla bla bla bla. oh my god. what a nice pussy you have!'
result = nothing.count("pussy")
print(result)