from os import stat
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import numpy as np
import mysql.connector
import speech_recognition as sr
from pydub import AudioSegment
import requests
import json
import re
pd.options.mode.chained_assignment = None

def index(request):
    print('Request for index page received')
    return render(request, 'hello_azure/home.html')


@csrf_exempt
def hello(req):
    Aud = None
    if req.method == 'POST':
        try:
            Aud = req.FILES['file']
        except ValueError:
            pass
        if Aud != None:
            filename = Aud.name
            point = Changin2Wav(filename)
            if point == 0:
                return HttpResponse("Can't Process this type of file")
            try:
                if point == 2:
                    AudioSegment.from_file(Aud, 'mp3')
                    AudioSegment.export(Aud, format='wav')
                elif point == 3:
                    AudioSegment.from_file(Aud, 'mp4')
                    AudioSegment.export(Aud, format='wav')
                elif point == 4:
                    AudioSegment.from_file(Aud, 'm4a')
                    AudioSegment.export(Aud, format='wav')
                elif point == 5:
                    AudioSegment.from_file(Aud, 'wma')
                    AudioSegment.export(Aud, format='wav')
                elif point == 6:
                    AudioSegment.from_file(Aud, 'flac')
                    AudioSegment.export(Aud, format='wav')
                elif point == 7:
                    AudioSegment.from_file(Aud, 'aac')
                    AudioSegment.export(Aud, format='wav')
                elif point == 8:
                    AudioSegment.from_file(Aud, 'ogg')
                    AudioSegment.export(Aud, format='wav')
                elif point == 9:
                    AudioSegment.from_file(Aud, 'raw')
                    AudioSegment.export(Aud, format='wav')
            except:
                content = {"An error occured while reading this file, please check this file or upload another"}
                return HttpResponse(content, status=500)
#            fs = FileSystemStorage()
#            filename = fs.save(img_file.name, img_file)
#            path = fs.path(filename)
            url = "https://quranfind.azurewebsites.net/api/quran"
            files=[
            ('file',(filename,Aud.open(),'audio/wav'))
            ]
            headers = {}
            try:
                file = Translating(Aud)
                response = Processing(file)
                #response = requests.request("POST", url, headers=headers, files=files, timeout=50)
                #if response.status_code == 200:
                json_object = json.dumps(response, ensure_ascii=False)
                return HttpResponse(json_object, status = 200)
                if response.status_code == 500:
                    return HttpResponse( "An Error occured while Processing Request", status=500)
                else:
                    return HttpResponse("an error occured", status=400)
            except :
                return HttpResponse( "An Error occured while Processing Request", status=500)
#            except requests.Timeout:
#                    return HttpResponse( "An Error occured while Processing Request", status=500)
        else:
            return HttpResponse("This File is corrupted", status=500)
    else:
        return HttpResponse(
         "No Such WebPage",
         status=404
    )

@csrf_exempt
def translator(req):
    if req.method == 'POST':
        try:
            arabic = req.POST['arabic']
        except ValueError:
            pass
        if arabic != None:
    #            file = Translating(Aud)
            url = "https://quranfind.azurewebsites.net/api/quran"
            payload={'arabic_text': arabic}
            try:
                response = Processing(arabic)
                #response = requests.request("GET", url, params=payload, timeout=50)
                #if response.status_code == 200:
                json_object = json.dumps(response, ensure_ascii=False)
                return HttpResponse(json_object, status = 200)
                if response.status_code == 500:
                    return HttpResponse( "An Error occured while Processing Request", status=500)
                else:
                    return HttpResponse("an error occured", status=400)
            except :
                return HttpResponse( "An Error occured while Processing Request", status=500)
#            except requests.Timeout:
#                    return HttpResponse( "An Error occured while Processing Request", status=500)
        else:
            return HttpResponse("This File is corrupted", status=500)
    else:
        return HttpResponse(
         "No Such WebPage",
         status=404
    )



@csrf_exempt
def AndroidAudio(req):
    Aud = None
    if req.method == 'POST':
        try:
            Aud = req.FILES['file']
        except ValueError:
            pass
        if Aud != None:
            filename = Aud.name
            point = Changin2Wav(filename)
            if point == 0:
                return HttpResponse("Can't Process this type of file")
            try:
                if point == 2:
                    AudioSegment.from_file(Aud, 'mp3')
                    AudioSegment.export(Aud, format='wav')
                elif point == 3:
                    AudioSegment.from_file(Aud, 'mp4')
                    AudioSegment.export(Aud, format='wav')
                elif point == 4:
                    AudioSegment.from_file(Aud, 'm4a')
                    AudioSegment.export(Aud, format='wav')
                elif point == 5:
                    AudioSegment.from_file(Aud, 'wma')
                    AudioSegment.export(Aud, format='wav')
                elif point == 6:
                    AudioSegment.from_file(Aud, 'flac')
                    AudioSegment.export(Aud, format='wav')
                elif point == 7:
                    AudioSegment.from_file(Aud, 'aac')
                    AudioSegment.export(Aud, format='wav')
                elif point == 8:
                    AudioSegment.from_file(Aud, 'ogg')
                    AudioSegment.export(Aud, format='wav')
                elif point == 9:
                    AudioSegment.from_file(Aud, 'raw')
                    AudioSegment.export(Aud, format='wav')
            except:
                content = {"An error occured while reading this file, please check this file or upload another"}
                return HttpResponse(content, status=500)
#            fs = FileSystemStorage()
#            filename = fs.save(img_file.name, img_file)
#            path = fs.path(filename)
            url = "https://quranfind.azurewebsites.net/api/quran"
            files=[
            ('file',(filename,Aud.open(),'audio/wav'))
            ]
            headers = {}
            try:
                file = Translating(Aud)
                response = Processing(file)
                #response = requests.request("POST", url, headers=headers, files=files, timeout=50)
                #if response.status_code == 200:
#                json_object = json.dumps(response, ensure_ascii=False)
                json_object = JsonToString(response)
                return HttpResponse(json_object, status = 200)
                if response.status_code == 500:
                    return HttpResponse( "An Error occured while Processing Request", status=500)
                else:
                    return HttpResponse("an error occured", status=400)
            except :
                return HttpResponse( "An Error occured while Processing Request", status=500)
#            except requests.Timeout:
#                    return HttpResponse( "An Error occured while Processing Request", status=500)
        else:
            return HttpResponse("This File is corrupted", status=500)
    else:
        return HttpResponse(
         "No Such WebPage",
         status=404
    )

@csrf_exempt
def AndroidText(req):
    if req.method == 'POST':
        try:
            arabic = req.POST['arabic']
        except ValueError:
            pass
        if arabic != None:
    #            file = Translating(Aud)
            url = "https://quranfind.azurewebsites.net/api/quran"
            payload={'arabic_text': arabic}
            try:
                response = Processing(arabic)
                #response = requests.request("GET", url, params=payload, timeout=50)
                #if response.status_code == 200:
                json_object = JsonToString(response)
                return HttpResponse(json_object, status = 200)
                if response.status_code == 500:
                    return HttpResponse( "An Error occured while Processing Request", status=500)
                else:
                    return HttpResponse("an error occured", status=400)
            except :
                return HttpResponse( "An Error occured while Processing Request", status=500)
#            except requests.Timeout:
#                    return HttpResponse( "An Error occured while Processing Request", status=500)
        else:
            return HttpResponse("This File is corrupted", status=500)
    else:
        return HttpResponse(
         "No Such WebPage",
         status=404
    )

def JsonToString(response):
    data = ""
    json_object = json.dumps(response, ensure_ascii=False)
    x = json.loads(response)
    length = len(x)
    for i in range(length):
        i += 1
        i = str(i) 
        data += "Sura Chapter: " + str(x[i]["sura"]) + "\nSura Name: " + str(x[i]["Sura_Name"]) + "\nVerse Number: " + str(x[i]["aya"]) + "\nArabic Text: " + str(x[i]["text"]) +"\n\n"
    data += str(length) + " Results Found"
    return data

def Changin2Wav(filename):
    point = 0
    if filename.lower().endswith('wav'):
        point = 1
        return point
    elif filename.lower().endswith('mp3'):
        point = 2
        return point
    elif filename.lower().endswith('mp4'):
        point = 3
        return point
    elif filename.lower().endswith('m4a'):
        point = 4
        return point
    elif filename.lower().endswith('wma'):
        point = 5
        return point
    elif filename.lower().endswith('flac'):
        point = 6
        return point
    elif filename.lower().endswith('aac'):
        point = 7
        return point
    elif filename.lower().endswith('ogg'):
        point = 8
        return point
    elif filename.lower().endswith('raw'):
        point = 9
        return point
    else:
        return point

def Translating(AUDIO_FILE):
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
        # instead of `r.recognize_google(audio, show_all=True)`
        print("Translation in Progress")
        s_result = r.recognize_google(audio, language="ar-SA", show_all=True)
        print('Done Translating... Finding The Verse')
        return s_result['alternative'][0]['transcript']
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    


def connect():
    try:
        connection = mysql.connector.connect(
            host="quran-verse-server.mysql.database.azure.com",
            user="quranverserequestuser@quran-verse-server",
            password="Sanisbature17@",
#            host="localhost",
#            user="access",
#            password="88890573",
            database="quran",
        )
    except Exception as e:
        error = "An Error Occured while connecting to database"
        print(error)
        return error
    return connection

def Processing(s_result):
    connection = connect()
    Speech_Text = s_result
    Speech_Text = re.sub(' +', ' ', Speech_Text)
    answer = ''
    ans = {}
    sani = ''
    quran = pd.read_sql('SELECT qs.Sura_Name,qt.sura,qt.aya,qt.text FROM quran_text_simple qt LEFT JOIN quran_suras qs ON sura = qs.Sura_Chapter', connection)
#    quran_full = pd.read_sql('SELECT qs.Sura_Name,qt.sura,qt.aya,qt.text FROM quran_text_full qt LEFT JOIN quran_suras qs ON sura = qs.Sura_Chapter', connection)
    div = {}
    string = []
    one = Speech_Text
    em = quran
    em['text'] = em['text'].str.replace('إ|أ', 'ا', regex = True)
    em['text'] = em['text'].str.replace('إ|أ', 'ا', regex = True)
    for i in range(len(quran['text'])):
        div[i] = quran['text'][i].split()
        quran['text'][i] = ' '.join(item for item in div[i] if item.isalnum())
    if one in 'الف|1,000|1000|الفلاش|الفلافل|الفلا|الفل|على فلان لم|علي فلا لم|على فلاش لم|على لنا|علي لم|علي لما|علي|علي لم':
        string.append(em[em['text'].str.contains('بسم الله الرحمن الرحيم الم')])
        strin = pd.DataFrame(string[0])
        answer = strin.sort_values(['text'], ascending = True)
    else:
        if not em[em['text'].str.contains(Speech_Text)].empty:
            string.append(em[em['text'].str.contains(Speech_Text)])
        if 'ه' in Speech_Text:
            qs = Speech_Text
            qss = qs.replace('ه','ة')
            if not em[em['text'].str.contains(qss)].empty:
                string.append(em[em['text'].str.contains(qss)])
        if not string == []:
            string[0].index= np.arange(1, len(string[0]) + 1)
            answer = pd.DataFrame(string[0])
            verses = answer.to_json(force_ascii=False, orient="index")
            return verses
        else:
            quran_full = pd.read_sql('SELECT qs.Sura_Name,qt.sura,qt.aya,qt.text FROM quran_text_all qt LEFT JOIN quran_suras qs ON sura = qs.Sura_Chapter', connection)
            if not quran_full[quran_full['text'].str.contains(Speech_Text)].empty:
                string.append(quran_full[quran_full['text'].str.contains(Speech_Text)])
            if not string == []:
                string[0].index= np.arange(1, len(string[0]) + 1)
        #        string[0].reset_index(inplace = True)
                answer = pd.DataFrame(string[0])
                verses = answer.to_json(force_ascii=False, orient="index")
                return verses
            else:    
                try:
                    verse_find = {}
                    for i in range(len(Speech_Text)):
                        Store = Speech_Text
                        statement = """
                        SELECT MATCH (text) AGAINST (%s IN NATURAL LANGUAGE MODE) score,text,sura,aya,quran_suras.Sura_Name
                        FROM quran_text_simple LEFT JOIN quran_suras ON sura = Sura_Chapter
                        WHERE MATCH (text) AGAINST (%s IN NATURAL LANGUAGE MODE)
                        ORDER BY MATCH (text) AGAINST (%s IN NATURAL LANGUAGE MODE) DESC
                        """
                        verse_find[i] = pd.read_sql(statement, connection, params=(Store,Store,Store,))
                        connection.commit()
                    answer = verse_find[0]
                    score = answer['score'].iloc[0]
                    add = 1
                    for i in range(len(answer)-1):
                        if score * 0.85 < answer['score'].iloc[i+1] and score >= 5.0:
                            add = i
                    answer = verse_find[0]
                    answer = answer[["Sura_Name","sura","aya","text"]]
                    answer.index= np.arange(1, len(answer) + 1)
                    answer = answer.iloc[:add]
                    verses = answer.to_json(force_ascii=False, orient="index")
                    return verses
                    all_arr = verse_find[0]
                    count = []
                    data = {}
                    deta = {}
                    wordst = []
                    words_found = {}
                    words_found_all = {}
                    c = 0
                    zz = 0
                    zs = 0
                    cx = []
                    for k in range(len(Speech_Text)):
                        val = Speech_Text[k].split()
                        for m in range(len(all_arr['text'])):
                            cm = {}
                            cc = 0
                            ccc = 0
                            cccc = 0
                            val = Speech_Text[k].split()
                            val2= all_arr['text'][m].split()
                            for l in range(len(val)):
                                for j in range(len(val2)):
                                    cd = val[l]
                                    dd = val2[j]
                                    if val2[j] == val[l]:
                                        if j+1 < len(val2) and l+1 < len(val):
                                            if (val2[j+1] == val[l+1]):
                                                cc+=1
                                                if l ==0:
                                                    zz+=1
                                                wordst.append(val[l])
                                        elif (j+1 >= len(val2) and l+1 >= len(val)):
                                            ccc+=1
                                            if l ==0:
                                                zz+=1
                                            wordst.append(val[l])
                                    elif ('ا' in cd and 'أ|إ' in dd) and (len(cd) == len(dd)):
                                        for i in range(len(cd)):
                                            if (cd[i] =='ا' and dd[i] == 'أ|إ'):
                                                cccc+=1
                                                if l ==0:
                                                    zs+=1
                                                wordst.append(val[l])
                            llm = cc + ccc+ cccc
                            cx.append(llm)
                            cc = 0
                            cccc = 0
                            words_found[m] = wordst
                        words_found_all[k] = words_found
                        for t in range(len(all_arr)):
                            for i in range(len(val)):
                                if i == 0:
                                    ck = val[i] + " "
                                elif i == (len(val)-1):
                                    ck = " " + val[i]
                                else:
                                    ck = " " + val[i] + " "

                                if ck in all_arr['text'][t]:
                                    c+=1
                            count.append(c)
                            deta[t] = [t+1,cx[t],count[t],all_arr['text'][t],all_arr['score'][t],all_arr['sura'][t],all_arr['aya'][t],all_arr['Sura_Name'][t]]
                            c = 0
                        data[k] = deta
                    Speech_Text_Rotate = len(data)
                    row = len(data[0])
                    col = len(data[0][0])
                    dat = [[[data[0][j][i] for i in range(col)] for j in range(row)] for k in range(Speech_Text_Rotate)]
                    frame = []
                    all_data = {}
                    for i in range(len(dat)):
                        all_data[i] = pd.DataFrame(dat[i], columns = ['Suggestion','Number of Words in other','Word Count','text','Score','sura','aya','Sura_Name'])
                    for i in range(len(dat)):
                        frame.append(all_data[i])
                    all_data = pd.concat(frame , keys=['S/N'])
                    #        print(all_data['Number of Words in other'][0])
                    #        print(all_data['Word Count'][0])
                    all_data = all_data.sort_values(['Number of Words in other','Score','Word Count','text'], ascending = False)
                    answer = all_data.drop(['Suggestion','Number of Words in other','Word Count','Score'], axis = 1)
                    answer.index= np.arange(1, len(answer) + 1)
                    answer = answer[['Sura_Name','sura','aya','text']]
                    verses = answer.to_json(force_ascii=False, orient="index")
                    print(answer)
                    return verses
                    for i in range(len(answer)):
                        if answer['text'][i] in answer['text'][0]:
                            if i == 0:
                                ans[3] = answer['text'][i]
                                ans[0] = answer['Sura_Name'][i]
                                ans[1] = str(answer['sura'][i])
                                ans[2] = str(answer['aya'][i])
                                sani = sani + "Arabic Text: {3}\nSura Name: {0}\tSura Chapter: {1}\tAya: {2}\n".format(ans[0],ans[1],ans[2],ans[3])
                            else:
                                ans[0] = answer['Sura_Name'][i]
                                ans[1] = str(answer['sura'][i])
                                ans[2] = str(answer['aya'][i])
                                sani = sani + "Sura Name: {0}\tSura Chapter: {1}\tAya: {2}\n".format(ans[0],ans[1],ans[2],ans[3])
                    return sani
                except KeyError:
                    return "Cant Find, Make sure you are reciting correctly"
