import requests
import unidecode
import itertools

skgrammarDic = {
    'č' : 'c',
    'ý' : 'y'
}

def isStubaPerson(input):
    url = "https://is.stuba.sk/uissuggest.pl"
    name = ' '.join(input[0:])
    payload = "_suggestKey=" + unidecode.unidecode(name) + "&upresneni_default=aktivni_a_preruseni,absolventi,zamestnanci,externiste&_suggestMaxItems=25&&lang=%73%6B&subjekt=%32%31%30%31%30&subjekt=%32%31%30%32%30&subjekt=%32%31%30%33%30&subjekt=%32%31%30%34%30&subjekt=%32%31%30%35%30&subjekt=%32%31%30%36%30&subjekt=%32%31%30%37%30&subjekt=%32%31%39%30%30&subjekt=%32%31%39%34%30&subjekt=%32%31%39%35%30&subjekt=%32%31%39%36%30&subjekt=%32%31%39%37%30&subjekt=%32%31%39%38%30&upresneni=%61%6B%74%69%76%6E%69%5F%61%5F%70%72%65%72%75%73%65%6E%69&upresneni=%7A%61%6D%65%73%74%6E%61%6E%63%69&vzorek=&_suggestHandler=lide&lang=sk"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Postman-Token': "d1c4d891-9cb2-4df9-9d98-e6a420598886"
    }
    listInput = []
    for x in input:
        if x.lower() in skgrammarDic:
            listInput.append(skgrammarDic[x.lower()])
        else:
            listInput.append(x)
    listOfPermutations = []
    for x in list(itertools.permutations(listInput, len(listInput))):
        listOfPermutations.append(unidecode.unidecode(" ".join(x).lower()))
    response = requests.request("POST", url, data=payload, headers=headers)
    for person in response.json()['data']:
        newPerson = person[0].replace(".","")
        newPerson = newPerson.replace(",", "")
        newPerson = newPerson.replace("Bc", "")
        newPerson = newPerson.replace("Ing", "")
        newPerson = newPerson.replace("Mgr", "")
        newPerson = newPerson.replace("doc", "")
        newPerson = newPerson.replace("PhD", "")
        unaccented_string = unidecode.unidecode(newPerson)
        if unaccented_string.strip().lower() in listOfPermutations:
            return True

    return False
