# PetCare

## Despre proiect

Dispozitivul Pet Care te ajuta sa scapi de grija mancarii si a apei pentru animalutele tale. Tot ce trebuie sa faci este sa adaugi o data la saptamana in valva dispozitivului bilutele preferate ale animalutului tau si sa adaugi apa in pompa. Apa si mancarea poti fi programate cu ajutorul unui timer, cat si eliberate manual. De asemenea, are incorporat un timer care il va anunta pe animalutul tau ca a sosit ora de somn. Tot ce trebuie sa faci tu este sa mergi cu el la plimbarile zilnice, de restul ne ocupam noi! 

### Framework-uri / Librarii utilizate:
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Python](https://www.python.org/)

### Document de analiza

[Aici]

### Analiza cerintelor clientului , planning poker & MoSCoW Prioritization

[Aici](https://github.com/AdrianCatrinoiu/PetCare/blob/main/Analiza%20cerintelor%20clientului.docx)


## Set up

### Python & Flask

- Python v 3.6 (minim)
- Flask
 ```
 pip install Flask
 ```
 
 ### Instalare
 1. Repo
 ```
 git clone git@github.com:AdrianCatrinoiu/PetCare.git
 ```
 
 2. Python & Flask
 ```
 pip install -e
 ```
 
 ### Rulare
 
 In terminal:
 ```
 cd be-flask && python app.py
 ```
 
 ### Senzori
 
 1. Check water sensor status
 ```
 POST http://127.0.0.1:5000/water/get-sensor-status
 ```
 2. Starting water sensor
 ```
 POST http://127.0.0.1:5000/water/start-water-sensor
 ```
 3. Make water level empty (for testing)
 ```
 POST http://127.0.0.1:5000/water/make-water-empty
 ```
 4. Push manual water
 ```
 POST http://127.0.0.1:5000/water/push-water-manual
 ```
 5. Check food sensor status
 ```
 POST http://127.0.0.1:5000/food/get-sensor-status
 ```
 6. Starting food sensor
 ```
 POST http://127.0.0.1:5000/food/start-food-sensor
 ```
 7. Make food level empty (for testing)
 ```
 POST http://127.0.0.1:5000/food/make-food-empty
 ```
 8. Push manual food
 ```
 POST http://127.0.0.1:5000/food/push-food-manual
 ```
 9. Set current temperature
 ```
 POST http://127.0.0.1:5000/set-current-temperature
 ```
 10. Check thermometer status
 ```
 POST http://127.0.0.1:5000/get-sensor-status
 ```
 11. Start thermometer
 ```
 POST http://127.0.0.1:5000/start-thermometer
 ```
 
 ## Functionalitati
 
-	Permite stăpânului să nu aibă grija animalelor de casă cu excepția plimbărilor.
-	Hrănirea și hidratarea animalelor de casă după un plan zilnic.
-	Supravegherea confortului termic din încăperea dispozitivului.
-	Fixarea unui timer pentru ora de somn a animalului.
-	Anuntarea animalului cand bolurile de apa si mancare sunt umplute.
-	Customizarea clopotelului aplicatiei pe night mode.
- Termomentru pentru aflarea temperaturii din camera in care sta animalutul

## HTTP
Pentru HTTP, folosim Flask

### Swagger
Principalele rute sunt:
```
/get-temperature
```
```
/start-thermometer
```
```
/stop-thermometer
```
```
/get-current-temperature
```
```
/set-current-temperature
```
```
/get-sensor-status
```

## MQTT

- cu MQTT se da publish la mesaje
- la fiecare request HTTP folosim MQTT
- cu ajutorul MQTT se da publish la mesaje folosind un client de MQTT

[Documentatie MQTT](https://www.emqx.com/en/blog/how-to-use-mqtt-in-python)

## Unit testing

Am folosit libraria ```unittest```. Comanda pentru rulare este urmatoarea:
```
python unitTests.py
```


## Integration testing

Am folosit libraria ```unittest```. Comanda pentru rulare este urmatoarea:
```
python integrationTest.py
```

## Resurse

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [MQTT](https://www.emqx.com/en/blog/how-to-use-mqtt-in-python)
- [Python](https://www.python.org/)
- [Postman](https://www.postman.com/)
- [Swagger](https://swagger.io/)
- [Unit testing](https://docs.python.org/3/library/unittest.html)

## Echipa

1. Adrian Catrinoiu
2. Giuliano Florentin Dumitru
3. Maria Neacsu
4. Marinel Arsene
5. Laurentiu Andrei Postole


 
 



