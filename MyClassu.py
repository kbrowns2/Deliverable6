
class User:
    def __init__(self, username="", userPassword="", firstName="",  lastName="", address="", officePhone="",
                 cellPhone="", emailAddress=""):
        self.__username = username
        self.__userPassword = password
        self.__firstName = firstName
        self.__lastName = lastName
        self.__address = address
        self.__officePhone = officePhone
        self.__cellPhone = cellPhone
        self.__emailAddress = email

    def getUsername(self):
        return self.__username

    def getuserPassword(self):
        return self.__password

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getAddress(self):
        return self.__address

    def getOfficePhone(self):
        return self.__officePhone

    def getCellPhone(self):
        return self.__cellPhone

    def getemailAddress(self):
        return self.__email

    def setUsername(self, username):
        self.__username = username

    def setuserPassword(self, password):
        self.__userPassword = password

    def setFirstName(self, firstName):
        self.__firstName = firstName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def setAddress(self, address):
        self.__address = address

    def setOfficePhone(self, officePhone):
        self.__officePhone = officePhone

    def setCellPhone(self, cellPhone):
        self.__cellPhone = cellPhone

    def setemailAddress(self, email):
        self.__emailAddress = email


class Manufacturer(User):
    def __init__(self, name="", Country=""):
        self.__Country = Country
        self.__name = name
        User.__init__(self, username="", userpassword="", firstName="",  lastName="", address="",
                      officePhone="", cellPhone="", emailaddress="")

    def getName(self):
        return self.__name

    def getCountry(self):
        return self.__Country

    def setName(self, name):
        self.__name = name

    def set(self, Country):
        self.__Country = Country

    def getContactPerson(self):
        return self.getFirstName(), self.getMiddleName(), self.getLastName()


class Product(Manufacturer):

        self.__length = length
        self.__width = width
        self.__weight = weight
        self.__cellArea = cellArea
        self.__modelNumber = modelNumber
        self.__cellTechnology = cellTechnology
        self.__systemVoltage = systemVoltage
        self.__manufacturingDate = manufacturingDate
        self.__pmp = pmp
        self.__man = man
        self.__totalNumberOfCells = totalNumberOfCells
        self.__numberOfCellsInSeries = numberOfCellsInSeries
        self.__numberOfSeriesStrings = numberofSeriesStrings
        self.__numberOfBypassDiodes = numberOfBypassDiodes
        self.__seriesFuseRating = seriesFuseRating
        self.__interconnectMaterial = interconnectMaterial
        self.__interconnectSupplier = interconnectSupplier
        self.__superstrateType = superstrateType
        self.__superstrateManufacturer = superstrateManufacturer
        self.__substrateType = substrateType
        self.__substrateManufacturer = substrateManufacturer
        self.__frameMaterial = frameMaterial
        self.__frameAdhesive = frameAdhesive
        self.__encapsulantType = encapsulantType
        self.__encapsulantManufacturer = encapsulantManufacturer
        self.__junctionBoxType = junctionBoxType
        self.__junctionBoxManufacturer = junctionBoxManufacturer
        self.__junctionBoxAdhesive = junctionBoxAdhesive
        self.__cableType = cableType
        self.__connectorType = connectorType
        self.__voc = voc
        self.__isc = isc
        self.__vmp = vmp
        self.__imp = imp
        self.__ff = ff
        Manufacturer.__init__(self, name="", registeredCountry="")

    class TestLab(User):
    def __init__(self, name="", address=""):
        self.__name = name
        self.__address = address
        User.__init__(self, username="", password="", firstName="",  lastName="", address="",
                      officePhone="", cellPhone="", emailAddress="")

    def getLabName(self):
        return self.__name

    def getLabAddress(self):
        return self.__address

    def setLabName(self, name):
        self.__name = name

    def setLabAddress(self, address):
        self.__address = address

    def getContactPerson(self):
        return self.getFirstName(),  self.getLastName()