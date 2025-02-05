Project AutoPattern 
AutoPattern is an IOT project desgined to integrate a Rasberry Pi 5 and a connected camera sensor, API to retrieve and visualize data and a cloud infrastructure to store it on.
This project is first and foremost about learning multiple areas of interest in API development, IoT, cloud infrastructure, and computer vision.
The project is designed to be able to start from basic pattern recognition and sufficient data flow in to the API and later on move towards more advanced areas.
```
KEY FEATURES:
     - Real time object recognition and tracking
     - Data sent directly to cloud database
     - FastAPI powered backend to fecth data
     - Visualize data
     - Modularity in structure for scalability 
```
```
TECH STACK:
Programming Language	Python
Hardware	Raspberry      Pi 5, Camera Sensor
Computer Vision	     OpenCV, NumPy
Cloud Database (TBD)	Azure, PostgreSQL
Backend API	          FastAPI (Running on VS Code)
Visualization (TBD)	     Matplotlib, Dash, Power BI
```
```
SYSTEM ARCHITECTURE:
     
  PC (VSCode + API) <---------------------------> CLOUD INFRA (DATABASE)
            \                                       /
             \                                     /
              \                                   / 
            Local network <------------------> Rasbi 5 <--- Camera sensor 
```

SYSTEM WORKFLOW:
1. The Raspberry Pi captures images using a connected camera.
2. OpenCV processes the images and counts detected objects.
3. Object count data is sent to the cloud database.
4. The API (running in VS Code) fetches data from the cloud.
5. Visualization tools display the data.
