dict = {'4': 'ZMonday', '2': 'Tuesday', '3': 'AWednesday', '1':'chalbey'}



#Get value from key
def getValue(kwargs):
    key = input('provide the key')
    print(kwargs.get(key))


#Get key from value
def getKey (kwargs,value):
    for i in dict.keys():
        if dict.get(i) == value:
            return i
    print('No matching value found')


#Add new pair
def addNewPair(kwargs):
    key,value = input('give key and value').split(',')
    kwargs[key] = value
    print(kwargs.items())


#Remove a pair
def removePair(k):
    key = input('give key ')
    k.pop(key)
    print(k.items())

#Update a pair
def updatePair(kwargs):
    key, value = input('give key and value').split()
    kwargs[key] = value
    print(kwargs.items())


#reverse a dict
def reverseDictionary(kwargs):
    x = (list(reversed((kwargs.items()))))
    print(x)

#sort a dict by keys
def sortDictionaryByKeys(kwargs):
    keys = kwargs.keys()
    keys = sorted(keys)
    for key in keys:
        dict[key] = kwargs.get(key)
    kwargs = dict
    print(kwargs.items())


#sort a dict by values
def sortDictionarybByValues(kwargs):
    values = kwargs.values()
    values = sorted(values)
    print(values)
    for value in values:
        key = getKey(kwargs,value)
        dict[key] = value
        print(key,' ',value)



#find n'th pair in a dict
def findNthPair(kwargs):
    n = int(input('give nth number'))
    keys = list(kwargs.keys())
    key = (keys[n-1])
    print(kwargs.get(key))


#Concatenate two dict
#def concatTwoDictionaries(dict1, dict2):


