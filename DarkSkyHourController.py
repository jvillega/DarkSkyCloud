#!/bin/usr/env python3

from DarkSkyHour import DarkSkyHour
import WebScraper as WS
import time

class DarkSkyHourController:
    urlAndAPI='https://api.darksky.net/forecast/API-KEY-HERE/'
    exclusions='?exclude=currently,daily,alerts,minutely'
    latAndLongURL='https://www.travelmath.com/cities/'

    # Requires lat and long of location you want your data for
    def __init__(self,*args):
        self.darkSkyHours=[]
        self.firstVar=args[0]
        self.secondVar=args[1]

    def __createDarkSkyHours(self):
        hourlyJSON=WS.getHTML(self.urlAndAPI+str(self.firstVar)+','+str(self.secondVar)+self.exclusions)
        hourlyObjs=WS.parseJSON(hourlyJSON);

        for hourlyObj in hourlyObjs:
            self.darkSkyHours.append(DarkSkyHour(hourlyObj))

    def __getLatAndLong(self):
        html=WS.getHTML(self.latAndLongURL+self.firstVar+',+'+self.secondVar)

        if (html[1].find('City Maps - Find any city in the world')>0):
            print('Couldn\'t find '+self.firstVar+', '+self.secondVar+'!')
            return False

        latAndLongHTML=WS.searchHTML(html, 'strong> -*\\d+')
        latAndLong=WS.parseString(latAndLongHTML, '/strong> ', '</p', len('/strong> '), -len('</p'))

        self.firstVar=latAndLong[0]
        self.secondVar=latAndLong[1]

        return True

    def getDarkSkyHours(self,length=18):
        #self.createDarkSkyHours()

        if (length==-1): # check if variable was initialized
            length=len(self.darkSkyHours)

        if (isinstance(self.firstVar, str) and isinstance(self.secondVar, str)): # check if passed city and state
            found=self.__getLatAndLong()

        if (found): # check if city and state were found
            self.__createDarkSkyHours()
            return self.darkSkyHours[:length]

        else:
            return False


# create

wilsonvilleORLat, wilsonvilleORLong='45.3', '-122.7725'
darkSkyHourController=DarkSkyHourController('hillsboro', 'or')
darkSkyHours=darkSkyHourController.getDarkSkyHours(12)

#
if (darkSkyHours):
    for x in darkSkyHours:
        print(x.getTemperature())
