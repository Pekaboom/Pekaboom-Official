from datetime import date

class CompanyInfo():

    name:str
    shortName: str
    founder: str
    yearFounded: date
    RCNumber: str
    companyType: str
    headquarter: object
    About: str
    RegisteredLocations: object
    website: str
    links: object

    def __init__(self):
        self.name = "Pekaboom Enterprise Limited"
        self.shortName = "Pekaboom Ent. &reg;"
        self.founder = "Abel O. Akponine"
        self.yearFounded = date(2023,8,21)
        self.RCNumber = "7104544"
        self.companyType = "Private Company Limited by Shares"
        self.headquarter = {
            "location": {
                "address": "30 Imoniruvwe Street, Off Alegbo Road, Effurun",
                "County": "Delta State",
                "Country": "Nigeria",
                "PostCode": "330102"
            }
        }
        self.About = "Pekaboom Enterprise Limited is a Start-up Tech Company Originally registered in Nigeria by the Corporate Affairs Commission (CAC) in 21<sup>st</sup> August 2023. It was founded by "+self.founder+" with the intent to research, build, develop, manage and implement advanced technologies to contribute to the global advancement of technologies world wide"
        self.RegisteredLocations = {
            "sites": [{
                "location": self.headquarter["location"],
                "operationType": "Headquarter"
            }]
        }
        
    
    def getName(self) -> str:
        return self.name

    def getShortName(self) -> str:
        return self.shortName
    
    def setName(self, name):
        self.name = name

    def setShortName(self, shortName):
        self.shortName = shortName

    def getInfo(self):
        return self