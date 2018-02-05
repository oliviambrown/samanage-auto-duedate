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

genSam = requests.get(samanageURL, headers=samHead)
numOfPages = genSam.headers['x-total-pages']

#it team dictionary - current members and id num
itTeam = {'peeps' : ['Alex Choi', 'Olivia Brown', 'IT'], 'id' : 98611}
    

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
#learned samange deals with data sets in pages and will have to navigate
#as such, set to 100 and then will have to develop a way to change pages (maybe)

#long explanation - I struggled with the logic here because i didn't realize that some tickets came with empty categories
#and therefore gave me the error that i cannot iterate a none type

#check for incidents that belong to IT
nuPyData = getPageInfo(1)

for i in range(maxEntry):

    #NEXT TODO - check for open incidents
    if nuPyData[i]['state'] != 'Closed' and nuPyData[i]['state'] != 'Resolved':
    
        #Check category first for IT id, if category is null then check the assignee, me, alex, or IT
        if nuPyData[i]['category'] is not None and nuPyData[i]['category']['id'] == itTeam['id']:
            print(nuPyData[i]['name']+ ' ' + str(nuPyData[i]['id']) +' ' +nuPyData[i]['state'])
        
        elif nuPyData[i]['assignee'] is not None and nuPyData[i]['assignee']['name'] in itTeam['peeps']:
            print(nuPyData[i]['name'] + ' ' + str(nuPyData[i]['id']) +' ' +nuPyData[i]['state'])

        #how the heck do i deal with ones that have neither the assignee or the id? should be rare right?
        #but that raises the option of what if it's facilities or production, i will stop here, now lets deal with paging
        elif nuPyData[i]['assignee'] is None:
             print('STRAY TICKET: ' + nuPyData[i]['name']+ ' ' + str(nuPyData[i]['id']) + ' ' + nuPyData[i]['state'])



#NEXT TODO - change the page and start over again, questioning if this is necessary..yes, in theory
             

        

#TODO - modify due date based on priority level

#TODO - email the assigned when due date approaches

#TODO - email super when due date passed=s

#TODO - send info back to system
