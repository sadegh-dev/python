"""
    Text translation with google translate API in python
"""
# pip install googletrans


from googletrans import Translator, LANGUAGES


####################################
#### list of support language ######
####################################

print(LANGUAGES)




#####################
#### translate ######
#####################

## EX1 #######################

gt = Translator()


# destination : 'fa'
# source : 'en'
result = gt.translate('سلام', 'en', 'fa')


print(result.src)
print(result.extra_data)
print(result.text)


## EX2 #######################

gt = Translator()

texts = [
    'سلام ، من حالم خوب است',
    'من برنامه نویس هستم',
    'من فوتبال را دوست دارم'
]

result = gt.translate(texts)

for x in result :
    print(x)


## EX3 #######################
# translate file text

gt = Translator()

with open('text.txt','r') as p :
    result = gt.translate(p.read())

print(result)

