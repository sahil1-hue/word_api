from django.http import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.
def word_api(request):

    if (request.method=='POST'):
        q = request.POST['search']

        try:
            #api access
            url = "https://wordsapiv1.p.rapidapi.com/words/"+q

            headers = {
                'x-rapidapi-key': "48d47be160msh4dac1e45406ab7bp1429e6jsn82089e8f40be",
                'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers)


            #converting to json
            results = response.json()
            #for getting the word
            word = []
            word.append(results['word'])


            #getting the defintion
            definition = []
            definition.append(results['results'][0]['definition'])

            # for synonyms
            synonyms = []

            if (('synonyms' in ((results['results'][0])))):
                for i in range(len(results['results'][0]['synonyms'])):
                    synonyms.append(results['results'][0]['synonyms'][i])

                s = ' , '.join(synonyms)
                synonyms = []
                synonyms.append(s)
            else:
                synonyms.append("No synonyms")


            # for partOfSpeech
            partOfSpeech = []
            partOfSpeech.append(results['results'][0]['partOfSpeech'])

            # for examples
            example = []
            if (('examples' in ((results['results'][0])))):
                for i in range(len(results['results'][0]['examples'])):
                    example.append(results['results'][0]['examples'][i])
                # print('yes')
                s = ""
                s = ' , '.join(example)
                example = []
                example.append(s)

            else:
                example.append("No examples")

            # for typeOf
            typeOf = []
            if (('typeOf' in ((results['results'][0])))):
                for i in range(len(results['results'][0]['typeOf'])):
                    typeOf.append(results['results'][0]['typeOf'][i])
            else:
                typeOf.append("does not have type of")

            # for syllable numbers
            syllablesNumber = []
            syllablesNumber.append(results['syllables']['count'])

            # for syllable List
            syllablesList = []
            for i in range(len(results['syllables']['list'])):
                syllablesList.append(results['syllables']['list'][i])
            s = " "
            s = " , ".join(syllablesList)
            syllablesList = []
            syllablesList.append(s)

            # for part of speech
            partOfspeech = []
            partOfspeech.append(results['results'][0]['partOfSpeech'])



            wordInfo = zip(word, definition, partOfspeech, synonyms, example, typeOf, syllablesNumber, syllablesList)

            context = {

                'wordInfo': wordInfo
            }



        except:
            return HttpResponse("please search for new term")
        return render(request, 'word/index.html', context)
    return render(request,'word/index.html')