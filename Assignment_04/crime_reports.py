#! /bin/env python
from datetime import date, datetime
from urllib.request import urlopen
from json import loads

class CrimeReport:
    def __init__(self, data):
        """
        Creates a CrimeReport from the data as provided by the crimereports.com/v3 API. This is purely for convienent access (`thing.lat` over `thing["lat"]` and some type checking/safety.

        Attributes:
            - type (str): The incident type name.
            - date (datetime): The datetime of the incident.
            - organization (str): The organization name (always Vic PD in this case).
            - lat (float): The Latitude.
            - lng (float): The Longtitude.

        """
        self.type = str(data["incident_type_name"])
        self.date = datetime.strptime(data["incident_date_time"], "%Y-%m-%dT%H:%M:%SZ")
        self.organization = str(data["org_name"])
        self.address = str(data["address"])
        self.lat = float(data["lat"])
        self.lng = float(data["lng"])
    def __repr__(self):
        """
        Defines a pretty printing for a CrimeReport
        """
        return "CrimeReport(type=\""+self.type+"\", address=\""+self.address+"\", lat=\""+str(self.lat)+"\", lng=\""+str(self.lng)+"\", date=\""+str(self.date)+"\", organization=\""+self.organization+"\")"

def get_crime_reports(start=date(2015,1,1), end=date(2016,3,1)):
    """
    Gets a set of crime reports for the VicPD in roughly the Victoria area from start to end dates.

    Returns a list of CrimeReports.
    """
    # This covers most of Victoria
    rows = range(2831, 2834)
    cols = range(1286, 1291)
    
    start_param = start.strftime("%Y/%m/%d")
    end_param = end.strftime("%Y/%m/%d")

    crimes = []

    for row in rows:
        for col in cols:
            #print("Getting row "+str(row)+" col "+str(col))
            url = "https://www.crimereports.com/v3/crime_reports/map/search_by_tile.json?start_date="+start_param+"&end_date="+end_param+"&incident_type_ids=9,10,11,12,14,98,99,100,101,103,121,149,150,151,160,161,163,166,168,169,171,172,173,180&org_ids=1550&row="+str(row)+"&column="+str(col)+"&zoom=13&include_sex_offenders=false"
            raw_data = urlopen(url).read().decode("utf-8")
            this_data = loads(raw_data)
            if this_data["crimes"]:
                #print(str(len(this_data["crimes"]))+" crimes found on this tile")
                for item in this_data["crimes"]:
                    crimes.append(CrimeReport(item))
    return crimes

print(get_crime_reports()[0])

