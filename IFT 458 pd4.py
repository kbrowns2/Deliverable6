import csv
import mysql.connector
from MyClasses import Product

db = MySQLdb.connect(host="localhost",
    user="Arturo Pichardo"
    passwd="Stant3636!
    db="pd4")

cur = db.cursor()
#Creating mds tables
cur.execute("CREATE TABLE mds (Manufacturer VARCHAR(255), Location VARCHAR(255), Contact VARCHAR(255), "
                 "Address VARCHAR(255), Email VARCHAR(255), Phone VARCHAR(255), Model_Number VARCHAR(255), "
                 "Module_total_length VARCHAR(255), Module_weight VARCHAR(255), Individual_Cell_Area "
                 "VARCHAR(255), Cell_technology VARCHAR(255), Cell_Manufacturer VARCHAR(255), "
                 "Cell_manufacturing_location VARCHAR(255), Total_number_of_cells VARCHAR(255), "
                 "Number_of_cells_in_series VARCHAR(255), Number_of_series_strings VARCHAR(255), "
                 "Number_of_bypass_diodes VARCHAR(255), Bypass_diode_rating VARCHAR(255), "
                 "Bypass_diode_max_junction_temp VARCHAR(255), Series_fuse_rating VARCHAR(255), "
                 "Interconnect_material_and_supplier_model_num VARCHAR(255), Interconnect_materials VARCHAR(255), "
                 "Superstrate_Type VARCHAR(255), Superstrate_Manufacturer VARCHAR(255), "
                 "Substrate_Type VARCHAR(255), Substrate_Manufacturer VARCHAR(255), Frame_Type VARCHAR(255), "
                 "Frame_Adhesive VARCHAR(255), Encapsulant_Manufacturer VARCHAR(255), Junction_Box_Type VARCHAR(255), "
                 "Junction_Box_Manufacturer VARCHAR(255), Junction_Potting_Material VARCHAR(255), "
                 "Junction_Adhesive VARCHAR(255), Junction_Box_Use VARCHAR(255), "
                 "Cable_Connector_Type VARCHAR(255), Max_System_Voltage VARCHAR(255), Voc VARCHAR(255), "
                 "Isc VARCHAR(255), Vmp VARCHAR(255), Pmp VARCHAR(255), FF VARCHAR(255), Imp VARCHAR(255))") 


cur.execute("CREATE TABLE results (Model VARCHAR(255), Test_Sequence VARCHAR(255), Test_Condition VARCHAR(255), "
                 "Testdate VARCHAR(255))")

cur.exectue("CREATE TABLE results2 (Isc VARCHAR(255), Voc VARCHAR(255), Imp VARCHAR(255), Vmp VARCHAR(255), "
                 "FF VARCHAR(255), Pmp VARCHAR(255))")

cur.execute("CREATE TABLE data (Manufacturer VARCHAR(255), Contact_name VARCHAR(255), Contact_email VARCHAR(255), "
                 "Cell_Technology VARCHAR(255), Rated_Power VARCHAR(255))"))


def fileIO():
    with open('test_results.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                    print('{",".join(row)}')
                    line_count += 1
            if row["Test Sequence"] == "Baseline":

                print('test_results.csv')

def mds():
    user = {
        "Manufacturer": "",
        "Loction": "",
        "Contact": "",
        "Address": "",
        "Email": "",
        "Phone": "",
        "Model Number": "",
        "Module total length x width (cm x cm)": "158 x 80.8",
        "Module weight (kg)": "15",
        "Individual cell Area (cm2)": "148.58",
        "Cell technology (mono-Si, poly-Si, a-Si, CIS, CdTe, etc.)": "Mono-Si",
        "Cell manufacturer and part #": "Motech",
        "Cell manufacturing location": "Taiwan",
        "Total number of cells": "72",
        "Number of cells in series": "72",
        "Number of series strings": "3",
        "Number of bypass diodes": "3",
        "Bypass diode rating (A) - attatch diode datasheet": "10 / 10SQ050",
        "Bypass diode max junction temperature (C)": "200",
        "Series fuse rating (A)": "10",
        "Interconnect material and supplier model no.": "Ulbrich Stainless Steels & Special Metals Ltd",
        "Interconnect dimensions (mm x mm)": "0.2mm x1.5mm , 0.2mm x 5mm"
        "Superstrate type (eg - strengthened glass etc)"
        "Substrate manufacturer and part #": "Dongguan CSG Solar Class Co., Ltd./ 3.2mm",
        "Substrate type": "TPT/0.35 mm",
        "Substrate manufacturer and part #": "ISOVOLTA",
        "Frame type/material": "Aluminum alloy",
        "Frame adhesive": "Dow Corning 7091",
        "Enacapsulant type": "EVA/0.5mm",
        "Encapsulant manufacturer and part #": "Bridge Stone Corporation",
        "Junction box type": "PV-RH0502B",
        "Junction box manufacturer and part #": "Cixi Renhe Photovolatic Electrical Appliance Co., Ltd." ,
        "Junction box potting material, if any": "NA",
        "Junction box adhesive": "Dow Corning 7091",
        "Is junction box intended for use with Conduit?": "NA",
        "Cable & Connector type": "2 pfg 1169 1x4 mm2, 05-6",
        "Maximum system voltage (V)": "1000V",
        "Voc (V)": "44.2",
        "ISC (A)": "5.25",
        "Vmp (V)": "35.2",
        "Imp (A)": "4.97",
        "Pmp (W)": "175",
        "FF (%)": "75"
    }

    for key in user:
        count = 0
        if count <= 7:
            value = input("Enter recquired information in realtion to " + key + " field: ")
            user[key] = value
            count = count + 1
    return user


def register():
    registration = {
        "username": "",
        "password": "",
        "first name": "",
        "last name": "",
        "company name": "",
        "company type": "",
        "address": "",
        "office phone number": "",
        "cell phone number": "",
        "email address": ""
    }

    for key in registration:
        value = input("Enter recquired information in realtion to " + key + " field: ")
        reistration[key] = value


        return registration

    }

def main()
    data = mds()
    p = Product()
    p.setName(data['Manufacturer'])
    p.setFirstName(data['Contract'])
    p.set.Email(data['Email'])
    p.setModelNumber(data['Model Number'])
    p.setCellTechnology(data['Cell Technology (mono-Si, poly-Si, a-Si, CIS, CdTe, etc.) ' ])
    p.setSystemVoltage(data['Maximum system voltage (V)'])
    p.setPMP(data[' Pmp (W)'])

    '''
    sql = "INSERT INTO results(Model, Test_Sequence, Test_Condition, Test_Date) VALUES (%S, %S, %S, %S)"
    sql = "INSERT INTO results2(Isc, Voc, Imp, Vmp, FF, Pmp) VALUES (%S, %S, %S, %S, %S, %S)"
    rec = file()
    cur.executemany(sql, rec)
    cur.comit


    sql = "INSERT INTO data (Manufacturer, Contact_Name, Contact_Email, Cell_Technology, Rated_Power) VALUES (%S, %S, %S, %S, %S)

    rec [p.getName(), p.getEmail(), p.getCellTechnology()]

    cur.executemany(sql, rec)
    cur.comit()

    '''



    print("\n\nProduct 1:\nManufacturer Name: {} \nContact Name: {} \nContact Email: {} \nModel Number: {} \nCell "
    "Technology: {} \nSystem Voltage: {} \nRated Power(PMP): {} \n\n".format (p.getName(), p.getFirstName(), p.getEmail(),
    p.getModelNumber(), p.getCellTechnology(), p.getSystemVoltage(), p.getPMP()))

    print(fileIO())

main()
