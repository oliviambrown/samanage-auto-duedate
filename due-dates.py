#! usr/bin/env Python3
#due-dates.py

import requests, json

samanageURL = 'https://api.samanage.com/incidents.json'

#variable for keeping track of current page
pageNumber = 1

#most amount of incidents on page
maxEntry = 100

userToken = 'b2Jyb3duQHN1bW1pdHJkdS5jb20=:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjoxODQxNDEyLCJnZW5lcmF0ZWRfYXQiOiIyMDE4LTAxLTE2IDE1OjI4OjE1In0.jceCALvimJAr6Yn1s7UnsW0KWxnc2ag4V_Vrjpz7wnj2bxQjDXCAoBi0I9MCnRTJ1-a4rAlaHh_jI-0in8pteg'
samHead = {'X-Samanage-Authorization' : 'Bearer ' + userToken}
 
r = requests.get(samanageURL)
numOfPages = r.headers['X-Total-Pages']
#--------------------------------------------------------------------------------------------

#function that gets the page, puts in credentials, and tranforms the data
def getPageInfo(pArg):

    samanageURLPage = samanageURL + '?page=' + str(pArg)
    pagingSamanage = requests.get(samanageURLPage,headers=samHead)
    #response object, the central location of info, made from reading the url
    samData = pagingSamanage.text
    #assign the data from the request to samData, in JSON format
    pyData = json.loads(samData)
    return pyData

#checking for it incidents
#after issue with the list going out of range, turns out that my request
#STOP - learned samange deals with data sets in pages and will have to navigate
#as such, set to 100 and then will have to develop a way to change pages (maybe)
#check for incidents that belong to IT

nuPyData = getPageInfo()

for i in range(maxEntry):
    #check for nonetype, print the id number so I can check
     #put a try-catch to let it stop gracefully
    if nuPyData[i]['category']['id'] == 98611:
        gprint('#' + str(i+1) + ' ' + nuPyData[i]['name'] + '\nID: ' + str(nuPyData[i]['id']))

        #change the page and start over again
        

    













#TODO - modify due date based on priority level

#TODO - email the assigned when due date approaches

#TODO - email super when due date passed=s

#TODO - send info back to system
