# FaceAttendanceSystem
**Face Attendance System: Real-Time Face Recognition and Attendance Tracking**

The Face Attendance System is a comprehensive real-time application designed for efficient face recognition, attendance tracking, and data storage. Leveraging various Python libraries and Firebase, the system provides a robust solution for managing student attendance. Below is an overview of the system's components and functionalities:

### **1. Overview:**
The Face Attendance System performs real-time face recognition and attendance tracking for students, utilizing Python scripts and integrating with Firebase for data storage.

### **2. System Components:**

#### a. **main.py:**
   - **Description:**
      - The main script for real-time face recognition and attendance tracking.
      - Utilizes OpenCV for webcam access and video capture.
      - Integrates face_recognition library by Adam Geitgey for accurate face recognition.
      - Implements cvzone library for additional graphical overlays on images.

   - **Functionality:**
      - Loads student face encodings from 'EncodeFile.p'.
      - Captures video frames from the webcam and detects faces.
      - Compares detected faces with the known faces in the database.
      - Displays real-time information, updates attendance, and shows student details.

#### b. **AddDatatoDatabase.py:**
   - **Description:**
      - A script to initialize and populate the Firebase Realtime Database with student data.
      - Uses the Firebase Admin SDK for Python.

   - **Functionality:**
      - Initializes the Firebase app and establishes a connection to the database.
      - Adds student data, including name, major, starting year, total attendance, etc., to the 'Students' node in the database.

#### c. **EncodeGenerator.py:**
   - **Description:**
      - Generates face encodings for student images and saves them for later use.
      - Utilizes the face_recognition library for encoding faces.
      - Uploads student images to Firebase Storage for easy access.

   - **Functionality:**
      - Reads student images from the 'Images' folder.
      - Converts images to face encodings using face_recognition library.
      - Saves the face encodings along with student IDs to 'EncodeFile.p'.
      - Uploads student images to Firebase Storage.

### **3. Setup and Usage:**

#### a. **Requirements:**
   - Python 3.x
   - OpenCV
   - face_recognition library
   - cvzone library
   - Firebase Admin SDK

#### b. **Installation:**
   - Install the required Python libraries using pip:
     ```
     pip install opencv-python face_recognition cvzone firebase-admin
     ```

#### c. **Usage:**
   - Run `AddDatatoDatabase.py` to initialize and populate the Firebase Realtime Database with student data.
   - Execute `EncodeGenerator.py` to generate face encodings and upload student images to Firebase Storage.
   - Launch the main application with `main.py` for real-time face recognition and attendance tracking.

### **4. Notes:**
   - Ensure that the Firebase Admin SDK key file (`serviceAccountKey.json`) is present in the project directory.
   - Adjust webcam settings as needed in `main.py` (e.g., resolution).

### **5. Acknowledgments:**
   - Special thanks to the developers of OpenCV, face_recognition, cvzone, and Firebase for providing the tools used in this project.



