#!/usr/bin/env python3

from datetime import datetime

class DarkSkyHour:
    # sigh...all these try excepts are necessary because locations don't always provide the same data
    # TO-DO:
    #   Make this better
    def __init__(self,params):
        try:
            self.time=datetime.utcfromtimestamp(int(params["time"])-(8*60*60)) # subtract 8 hrs from UNIX time and convert to PST
        except KeyError:
            pass
        try:
            self.summary=params["summary"]
        except KeyError:
            pass
        try:
            self.icon=params["icon"]
        except KeyError:
            pass
        try:
            self.precipIntensity=params["precipIntensity"]
        except KeyError:
            pass
        try:
            self.precipProbability=params["precipProbability"]
        except KeyError:
            pass
        try:
            self.precipType=params["precipType"]
        except KeyError:
            pass
        try:
            self.temperature=params["temperature"]
        except KeyError:
            pass
        try:
            self.apparentTemperature=params["apparentTemperature"]
        except KeyError:
            pass
        try:
            self.dewPoint=params["dewPoint"]
        except KeyError:
            pass
        try:
            self.humidity=params["humidity"]
        except KeyError:
            pass
        try:
            self.pressure=params["pressure"]
        except KeyError:
            pass
        try:
            self.windSpeed=params["windSpeed"]
        except KeyError:
            pass
        try:
            self.windGust=params["windGust"]
        except KeyError:
            pass
        try:
            self.windBearing=params["windBearing"]
        except KeyError:
            pass
        try:
            self.cloudCover=params["cloudCover"]
        except KeyError:
            pass
        try:
            self.uvIndex=params["uvIndex"]
        except KeyError:
            pass
        try:
            self.visibility=params["visibility"]
        except KeyError:
            pass
        try:
            self.ozone=params["ozone"]
        except KeyError:
            pass


    # this needs logic to make sure it can't be run if variable is null
    def getTime(self):
        return self.time

    def getSummary(self):
        return self.summary

    def getIcon(self):
        return self.icon

    def getPrecipIntensity(self):
        return self.precipIntensity

    def getPrecipProbability(self):
        return self.getPrecipProbability

    def getPrecipType(self):
        return self.precipType

    def getTemperature(self):
        return self.temperature

    def getApparentTemperature(self):
        return self.apparentTemparature

    def getDewPoint(self):
        return self.dewPoint

    def getHumidity(self):
        return self.humidity

    def getPressure(self):
        return self.pressure

    def getWindSpeed(self):
        return self.windSpeed

    def getWindGust(self):
        return self.windGust

    def getWindBearing(self):
        return self.windBearing

    def getCloudCover(self):
        return self.cloudCover

    def getUVIndex(self):
        return self.uvIndex

    def getVisibility(self):
        return self.visibility

    def getOzone(self):
        return self.ozone
