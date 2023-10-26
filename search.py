import csv
import csv ,operator
class Search:


    def searchcollege() :
        print("University Search\n")
        line = input("Enter the name of the university you're interested in:\n")
        csv_file = csv.DictReader(open('university-data.csv'))
        csv_file = sorted(csv_file, key = operator.itemgetter("INSTNM"))

        possibleUniversities = []
        for row in csv_file:
            if line.lower() in row["INSTNM"].lower():
                possibleUniversities.append(row)
        if len(possibleUniversities) == 0:
                print("No Results Found")    
        elif len(possibleUniversities) == 1:
            for row in possibleUniversities:
                print(row["INSTNM"]+"\n")
                print("Address: "+row["CITY"]+", "+row["STABBR"]+" "+row["ZIP"]+"\n")
                print("Website: "+row["INSTURL"]+"\n")
                print("TUITION FEE IN STATE: "+row["TUITIONFEE_IN"]+"\n")
                print("TUITION FEE OUT STATE: "+row["TUITIONFEE_OUT"]+"\n")
                print("Average SAT: "+row["SAT_AVG"]+"\n")
                print("Admission rate: "+row["ADM_RATE"]+"\n")
                print("TOP 25 SAT score: "+row["SATVR25"]+"\n")
                print("Latitude: "+row["LATITUDE"]+"\n")
                print("Longitude: "+row["LONGITUDE"]+"\n")
                print("Pre degree: "+row["PREDDEG"]+"\n")
                print("High Degree: "+row["HIGHDEG"]+"\n")
        elif len(possibleUniversities) <= 20:
            print('Multiple results found for "' + line + '".')
            count = 1
            for i in possibleUniversities:
                print('[' + str(count) + ']' + " " + i["INSTNM"])
                count+=1
            num = input("Select [1-" + str(count-1) + "]")
            finalUni = possibleUniversities[int(num)-1]
            FINU = []
            FINU.append(finalUni)
            if len(FINU) == 1:
                for row in FINU:
                    print(row["INSTNM"]+"\n")
                    print("Address: "+row["CITY"]+", "+row["STABBR"]+" "+row["ZIP"]+"\n")
                    print("Website: "+row["INSTURL"]+"\n")
                    print("TUITION FEE IN STATE: "+row["TUITIONFEE_IN"]+"\n")
                    print("TUITION FEE OUT STATE: "+row["TUITIONFEE_OUT"]+"\n")
                    print("Average SAT: "+row["SAT_AVG"]+"\n")
                    print("Admission rate: "+row["ADM_RATE"]+"\n")
                    print("TOP 25 SAT score: "+row["SATVR25"]+"\n")
                    print("Latitude: "+row["LATITUDE"]+"\n")
                    print("Longitude: "+row["LONGITUDE"]+"\n")
                    print("Pre degree: "+row["PREDDEG"]+"\n")
                    print("High Degree: "+row["HIGHDEG"]+"\n")
        else :
            while len(possibleUniversities)>20:
                possibleUniversities = []
                s = input("Please be more specific")
                for new_row in csv_file:
                    if s.lower() in new_row["INSTNM"].lower():
                        possibleUniversities.append(new_row)
            if len(possibleUniversities) == 0:
                print("No Results Found")
            elif len(possibleUniversities) == 1:
                for row in possibleUniversities:
                    print(row["INSTNM"]+"\n")
                    print("Address: "+row["CITY"]+", "+row["STABBR"]+" "+row["ZIP"]+"\n")
                    print("Website: "+row["INSTURL"]+"\n")
                    print("TUITION FEE IN STATE: "+row["TUITIONFEE_IN"]+"\n")
                    print("TUITION FEE OUT STATE: "+row["TUITIONFEE_OUT"]+"\n")
                    print("Average SAT: "+row["SAT_AVG"]+"\n")
                    print("Admission rate: "+row["ADM_RATE"]+"\n")
                    print("TOP 25 SAT score: "+row["SATVR25"]+"\n")
                    print("Latitude: "+row["LATITUDE"]+"\n")
                    print("Longitude: "+row["LONGITUDE"]+"\n")
                    print("Pre degree: "+row["PREDDEG"]+"\n")
                    print("High Degree: "+row["HIGHDEG"]+"\n")
            elif len(possibleUniversities) <= 20:
                print('Multiple results found for "' + s + '".')
                count = 1
                for i in possibleUniversities:
                    print('[' + str(count) + ']' + " " + i["INSTNM"])
                    count+=1
                num = input("Select [1-" + str(count-1) + "]")
                finalUni = possibleUniversities[int(num)-1]
                FINU = []
                FINU.append(finalUni)
                if len(FINU) == 1:
                    for row in FINU:
                        print(row["INSTNM"]+"\n")
                        print("Address: "+row["CITY"]+", "+row["STABBR"]+" "+row["ZIP"]+"\n")
                        print("Website: "+row["INSTURL"]+"\n")
                        print("TUITION FEE IN STATE: "+row["TUITIONFEE_IN"]+"\n")
                        print("TUITION FEE OUT STATE: "+row["TUITIONFEE_OUT"]+"\n")
                        print("Average SAT: "+row["SAT_AVG"]+"\n")
                        print("Admission rate: "+row["ADM_RATE"]+"\n")
                        print("TOP 25 SAT score: "+row["SATVR25"]+"\n")
                        print("Latitude: "+row["LATITUDE"]+"\n")
                        print("Longitude: "+row["LONGITUDE"]+"\n")
                        print("Pre degree: "+row["PREDDEG"]+"\n")
                        print("High Degree: "+row["HIGHDEG"]+"\n")

       
        
        
    searchcollege()