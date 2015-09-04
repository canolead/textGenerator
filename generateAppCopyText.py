#!/usr/bin/python
# -*- coding: utf-8 -*-
print "Content-Type: application/json\n";

import json
import random
import MySQLdb as mdb
import re

HOST = 'localhost'
USER = 'root'
PASSWORD = 'root'
DATABASE = 'text_generator'

DOWNLOAD_THRESHOLD = 10000;

indecesList = [
	{"appCategory":10,"appType":0,"appFeature1":3,"appFeatureText1":2,"appFeature2":2,"appFeatureText2":5,"appPrice":0,"targetUser":4,"download":0,"textType":"informal"},
	{"appCategory":9,"appType":0,"appFeature1":0,"appFeatureText1":6,"appFeature2":3,"appFeatureText2":1,"appPrice":0,"targetUser":0,"download":4,"textType":"informal"},
	{"appCategory":5,"appType":8,"appFeature1":1,"appFeatureText1":2,"appFeature2":2,"appFeatureText2":10,"appPrice":0,"targetUser":0,"download":7,"textType":"informal"},
	{"appCategory":11,"appType":0,"appFeature1":1,"appFeatureText1":4,"appFeature2":0,"appFeatureText2":7,"appPrice":0,"targetUser":4,"download":2,"textType":"informal"},
	{"appCategory":10,"appType":1,"appFeature1":3,"appFeatureText1":0,"appFeature2":1,"appFeatureText2":5,"appPrice":0,"targetUser":5,"download":4,"textType":"informal"},
	{"appCategory":11,"appType":2,"appFeature1":0,"appFeatureText1":2,"appFeature2":2,"appFeatureText2":8,"appPrice":0,"targetUser":4,"download":5,"textType":"informal"},
	{"appCategory":2,"appType":3,"appFeature1":4,"appFeatureText1":0,"appFeature2":4,"appFeatureText2":2,"appPrice":0,"targetUser":2,"download":2,"textType":"informal"},
	{"appCategory":7,"appType":1,"appFeature1":0,"appFeatureText1":0,"appFeature2":3,"appFeatureText2":2,"appPrice":0,"targetUser":5,"download":5,"textType":"informal"},
	{"appCategory":3,"appType":1,"appFeature1":1,"appFeatureText1":5,"appFeature2":3,"appFeatureText2":1,"appPrice":0,"targetUser":0,"download":7,"textType":"informal"},
	{"appCategory":6,"appType":1,"appFeature1":2,"appFeatureText1":5,"appFeature2":4,"appFeatureText2":0,"appPrice":0,"targetUser":4,"download":5,"textType":"informal"},
	{"appCategory":3,"appType":2,"appFeature1":1,"appFeatureText1":2,"appFeature2":0,"appFeatureText2":7,"appPrice":0,"targetUser":5,"download":2,"textType":"informal"},
	{"appCategory":9,"appType":2,"appFeature1":3,"appFeatureText1":3,"appFeature2":3,"appFeatureText2":1,"appPrice":0,"targetUser":0,"download":6,"textType":"informal"},
	{"appCategory":12,"appType":0,"appFeature1":3,"appFeatureText1":0,"appFeature2":1,"appFeatureText2":5,"appPrice":0,"targetUser":3,"download":7,"textType":"informal"},
	{"appCategory":2,"appType":6,"appFeature1":4,"appFeatureText1":2,"appFeature2":0,"appFeatureText2":10,"appPrice":0,"targetUser":3,"download":5,"textType":"informal"},
	{"appCategory":11,"appType":0,"appFeature1":3,"appFeatureText1":1,"appFeature2":0,"appFeatureText2":9,"appPrice":0,"targetUser":5,"download":1,"textType":"informal"},
	{"appCategory":6,"appType":1,"appFeature1":3,"appFeatureText1":1,"appFeature2":4,"appFeatureText2":1,"appPrice":0,"targetUser":2,"download":1,"textType":"informal"}
]

def generateText(index, option, data): 

	adjectiveArray = ["とても","とっても","とにかく"]
	numToStr = {0: "0", 1000:"1000", 5000:"5000", 10000:"１万", 50000:"５万", 100000:"１０万", 500000:"５０万", 1000000:"１００万"}

	appFeatureObj1 = data["appFeatureObj1"]
	appPriceTextObj = random.choice(data["appPriceTextList"])
	appTargetUserTextObj = random.choice(data["appTargetUserTextList"])
	appAdjectiveTextObj = random.choice(data["appAdjectiveList"])
	appDownloadTextObj = random.choice(data["appDownloadTextList"])
	appCopyListDefaultObj = random.choice(data["appCopyListDefault"])
	appCopyListObj = random.choice(data["appCopyList"])
	appCopyObj = random.choice(data["appCopyList"])

	exampleList = []
	text = ""
	if index==0:
		text = appTargetUserTextObj["text"].encode("utf-8")+random.choice(adjectiveArray)+appFeatureObj1["labelNormal"].encode("utf-8")+"、"+appAdjectiveTextObj["text"].encode("utf-8")+appPriceTextObj["text"].encode("utf-8")
		if len(appTargetUserTextObj["examples"]):
			phrase = re.sub(r"<numList>|<user>|<apptype>|\*", "○○", appTargetUserTextObj["text"].encode("utf-8"))		
			exampleList.append({"text":phrase, "appId": appTargetUserTextObj["examples"]})
		if len(appAdjectiveTextObj["examples"]):
			phrase = re.sub(r"<numList>|<user>|<apptype>|\*", "○○", appAdjectiveTextObj["text"].encode("utf-8"))
			exampleList.append({"text":phrase, "appId": appAdjectiveTextObj["examples"]})
		if len(appPriceTextObj["examples"]):
			phrase = re.sub(r"<numList>|<user>|<apptype>|\*", "○○", appPriceTextObj["text"].encode("utf-8"))
			exampleList.append({"text":phrase, "appId": appPriceTextObj["examples"]})

	elif index==1:
		text = appCopyListDefaultObj["text"].encode("utf-8")+appFeatureObj1["textComma"].encode("utf-8")+appFeatureObj1["labelPeriod"].encode("utf-8")+"！"
		if len(appCopyListDefaultObj["examples"]):
			phrase = re.sub(r"<numList>|<user>|<apptype>|\*", "○○", appCopyListDefaultObj["text"].encode("utf-8"))
			exampleList.append({"text":phrase, "appId": appCopyListDefaultObj["examples"]})
		if len(appFeatureObj1["examples"]):
			phrase = re.sub(r"<numList>|<user>|<apptype>|\*", "○○", appFeatureObj1["textComma"].encode("utf-8"))
			exampleList.append({"text": phrase, "appId": appFeatureObj1["examples"]})

	elif index==2:
		text = appCopyListObj["text"].encode("utf-8")+appFeatureObj1["textComma"].encode("utf-8")+"、"+appFeatureObj1["labelNormal"].encode("utf-8")+appType.encode("utf-8")+"アプリ。"+appPriceTextObj["text"].encode("utf-8")
		if len(appCopyListObj["examples"]):
			phrase = re.sub(r"<numList>|<user>|<apptype>|\*", "○○", appCopyListObj["text"].encode("utf-8"))
			exampleList.append({"text":phrase, "appId": appCopyListObj["examples"]})
		if len(appFeatureObj1["examples"]):
			phrase = re.sub(r"<numList>|<user>|<apptype>|\*", "○○", appFeatureObj1["textComma"].encode("utf-8"))
			exampleList.append({"text":phrase, "appId": appFeatureObj1["examples"]})
		if len(appPriceTextObj["examples"]):
			phrase = re.sub(r"<numList>|<user>|<apptype>|\*", "○○", appPriceTextObj["text"].encode("utf-8"))
			exampleList.append({"text":phrase, "appId": appPriceTextObj["examples"]})

	else:		
		text = appTargetUserTextObj["text"].encode("utf-8")+random.choice(adjectiveArray)+appFeatureObj1["labelNormal"].encode("utf-8")+"、"+appAdjectiveTextObj["text"].encode("utf-8")+appPriceTextObj["text"].encode("utf-8")
		if len(appTargetUserTextObj["examples"]):
			phrase = re.sub(r"<numList>|<user>|<apptype>|\*", "○○", appTargetUserTextObj["text"].encode("utf-8"))
			exampleList.append({"text":phrase, "appId": appTargetUserTextObj["examples"]})
		if len(appAdjectiveTextObj["examples"]):
			phrase = re.sub(r"<numList>|<user>|<apptype>|\*", "○○", appAdjectiveTextObj["text"].encode("utf-8"))
		if len(appPriceTextObj["examples"]):
			phrase = re.sub(r"<numList>|<user>|<apptype>|\*", "○○", appPriceTextObj["text"].encode("utf-8"))
			exampleList.append({"text":phrase, "appId": appPriceTextObj["examples"]})

	if option["addDownload"]:
		text = appDownloadTextObj["text"].encode("utf-8")+text
		if len(appDownloadTextObj["examples"]):
			phrase = re.sub(r"<numList>|<user>|<apptype>|\*", "○○", appDownloadTextObj["text"].encode("utf-8"))
			exampleList.append({"text":phrase, "appId": appDownloadTextObj["examples"]})	

	outputText = text.replace("<numList>",numToStr[appDownload]).replace("<user>",appTargetUser.encode("utf-8")).replace("<apptype>",appType.encode("utf-8")).replace("*","○○")

	return {"text": outputText, "examples": exampleList}


indices = random.choice(indecesList)
#indices = {"appCategory":9,"appType":0,"appFeature1":4,"appFeatureText1":2,"appFeature2":3,"appFeatureText2":0,"appPrice":0,"targetUser":0,"download":4, "textType":"informal"}
dataset = []
with open('appTexts.json') as data_file:
    appTextObj = json.loads(data_file.read(), "utf-8")

category = appTextObj["appCategory"][indices["appCategory"]]
categoryLabel = category["category"]
appType = category["types"][indices["appType"]]

appTextSeed = {}

appFeature1 = appTextObj["appFeature"][indices["appFeature1"]]
appTextSeed["appFeatureObj1"] = {
	"labelNormal": appFeature1["labelForms"]["normal"],
	"labelPeriod": appFeature1["labelForms"]["period"],
	"textNormal": appFeature1["textList"][indices["appFeatureText1"]]["normal"],
	"textComma": appFeature1["textList"][indices["appFeatureText1"]]["comma"], 
	"examples": appFeature1["textList"][indices["appFeatureText1"]]["examples"]
}

appPrice = appTextObj["price"][indices["appPrice"]]
appPriceTextList = appPrice["textList"]["all"]
appPriceTextList +=  appPrice["textList"][indices["textType"]]
appTextSeed["appPriceTextList"] = appPriceTextList

appTargetUser = appTextObj["targetUser"]["userList"][indices["targetUser"]]
appTargetUserTextList = appTextObj["targetUser"]["textList"]["all"]
appTargetUserTextList += appTextObj["targetUser"]["textList"][indices["textType"]] 
appTextSeed["appTargetUserTextList"] = appTargetUserTextList

appAdjectiveList = appTextObj["appAdjective"]["all"]
appAdjectiveList += appTextObj["appAdjective"][indices["textType"]]
appTextSeed["appAdjectiveList"] = appAdjectiveList

appDownload = appTextObj["download"]["numList"][indices["download"]]
appDownloadTextList = appTextObj["download"]["textList"]["all"]
appDownloadTextList += appTextObj["download"]["textList"][indices["textType"]]
appTextSeed["appDownloadTextList"] = appDownloadTextList

appCopyListDefault = []
appCopyListDefault += appTextObj["appCopy"]["default"]["all"]
appCopyListDefault += appTextObj["appCopy"]["default"][indices["textType"]]
appTextSeed["appCopyListDefault"] = appCopyListDefault

appCopyList = []
if indices["appCategory"]==0:
	appCopyList += appTextObj["appCopy"]["all"]["all"]
	appCopyList += appTextObj["appCopy"]["all"][indices["textType"]]
	appCopyList += appTextObj["appCopy"]["games"]["all"]
	appCopyList += appTextObj["appCopy"]["games"][indices["textType"]]
elif indices["appCategory"]==2:
	appCopyList += appTextObj["appCopy"]["all"]["all"]
	appCopyList += appTextObj["appCopy"]["all"][indices["textType"]]
	appCopyList += appTextObj["appCopy"]["information"]["all"]
	appCopyList += appTextObj["appCopy"]["information"][indices["textType"]]
else:
	appCopyList += appTextObj["appCopy"]["all"]["all"]
	appCopyList += appTextObj["appCopy"]["all"][indices["textType"]]
appTextSeed["appCopyList"] = appCopyList

#random choices

textOption = {}
generatedTexts = []
appExampleList = []

if appDownload > DOWNLOAD_THRESHOLD:  
	textOption["addDownload"] = True
else:
	textOption["addDownload"] = False

for i in range(3):
	outputText = generateText(i%3, textOption, appTextSeed)
	generatedTexts.append({"text":outputText["text"], "examples":[]})

	for phrase in outputText["examples"]:
		for appId in phrase["appId"]:
			appExampleList.append({"index":i, "text":phrase["text"], "appId": appId})


con = mdb.connect(HOST, USER, PASSWORD, DATABASE)
with con:
    cur = con.cursor()
    for ex in appExampleList:
	    cur.execute("SELECT id, title, description FROM google_play_data WHERE id="+str(ex["appId"]))
	    rows = cur.fetchall()
	    if len(rows):
	    	ex["appTitle"] = rows[0][1]
	    	ex["description"] = rows[0][2]
	
	    	generatedTexts[ex["index"]]["examples"].append({"appId":ex["appId"], "text":ex["text"] , "appTitle":rows[0][1], "description": rows[0][2]})

print(json.dumps(generatedTexts))

