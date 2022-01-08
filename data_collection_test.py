from sense_hat import SenseHat
import csv

sense = SenseHat()

log = []

rows = []

cont = True

sense.show_message("PROGRAM ACTIVE", text_colour=(0, 205, 0))

print("Data is being collected. Please wait.")

def collect_data():
      
    pressure = round(sense.get_pressure(), 2)

    temperature_C = round(sense.get_temperature(), 2)

    temperature_F = round((temperature_C * (9/5) + 32), 2)

    humidity = round(sense.get_humidity(), 2)
        
    data = pressure, temperature_C, temperature_F, humidity

    log.append(data)
         
    
def export_data_to_csv():
            
    rows = log[:]
            
    filename = "data_log.csv"
            
    with open(filename, "a") as csvfile:
                
        csvwriter = csv.writer(csvfile)
                
        csvwriter.writerows(rows)
                    
while cont:
    
    collect_data()   
    
    if len(log) % 10000 == 0:
        
        resume = input("\nContinue to collect data? y/n: ")
        
        resume.lower()
    
        if resume == "n":
                  
            cont = False
                  
            export_data_to_csv() 
            
            print("\nData collection will now end.\n")
                
            print("The data_log.csv has been created. It can be accessed in the SenseHat folder. This program will now end.")
            
            sense.show_message("PROGRAM ENDED", text_colour=(255, 0, 0))
            
        elif resume == "y":
            
            print("\nData collection will now continue.")
            
            sense.show_message("PROGRAM ACTIVE", text_colour=(0, 205, 0))
            
            collect_data()
            
        
        elif resume != "n" and resume != "y":
            
            cont = False
            
            print("\nYou have entered an invalid response. Please restart the program again.")
            
            sense.show_message("ERROR", text_colour=(255, 255, 0))
            

