'''
Joseph Wu
CMSC389O section 0301
uid: 118956183
I pledge on my honor that I have not given or received any unauthorized 
assistance on this assignment/examination.

Note to grader: I am not sure how the prior queues in python works so there may be some 
logic/syntax naming conventions that I am unfamiliar with. Please let me know of you have any suggestions.


QUESTION 1:
note: questions 2 and 3 are at the bottom of this file

The problem my system solves: 
My system handles calls and requests for non-life-threatening appointments for an urgent care 
clinic. It catogorizes the patient based on the immediate urgency level and future potential 
severity. The reasoning for this is in symptoms might get worse if not treated in a timely 
manner. The simple fix that could have taken doctors a couple minutes could turn into a 
whole surgury. My system also allows for updates on a patient's urgency level and 
potential severity.
Ex: Lacerations can get infected if not treated. 

How does my system work?
My system has a doctor, patient and clinic class. The doctor and patient class represent the people objects with 
their associated attributes such as name, medical speciality for doctors, potiential severity 
and urgent level for the patients. The clinic class adds and processes the patient appointment requests by using a 
priority queue which sees the patient with the highest urgency level and highest potiential severity. The queues are 
also sorted by which doctor they need to see which is something that I would implement better if I had more time
 and knew more python.


If I had more time:
For the sake of simplicity, my code does not take into account how long treatment takes, the 
doctors stamina, and how the long the patient has waited. In an ideal system, no patient should 
wait longer than 2 days and account for understaffing of doctors. The potential severity and 
new urgency level would also update every day the patient isn't treated automatically.
'''

from enum import Enum
from queue import PriorityQueue


class SPECIALTY(Enum):
    GENERAL_PRACTITIONER = "General Practitioner"
    HEART = "Heart"
    ORTHOPEDIC = "Orthopedic"
    ENT = "ENT"

#doctor person/object
class Doctor: 
    #initilizes doctor with a name and speciality
    def __init__(self, name, special):
        self.name = name
        self.special = special
    #returns the doctor's speciality
    def get_specialty(self):
        return self.specialty.value

#patient person/object
class Patient:
    #initilizes a patient with a name, urgency level, and potential severity
    #for potiential severity system will automatially assigned based on patient description (not implemented)
    def __init__(self, name, urgency_level, potential_severity, special):
        self.name = name
        self.urgency_level = urgency_level
        self.potential_severity = potential_severity
        self.special = special
    #returns the urgency level
    def get_urgency_level(self):
        return self.urgency_level

    #returns the potential severity
    def get_potential_severity(self):
        return self.potential_severity
    #return the doctor specialty needed based on request
    def get_doctor_specialty(self):
        return self.special
    #updates urgency level with new urgency level
    def update_urgency(self, new_urgency):
        self.urgency_level = new_urgency

    #updates potential severity with new severity
    def update_severity(self, new_severity):
        self.potential_severity = new_severity

#clinic object
class Clinic:
    #initializes the clinic with a priority queue of patients to see
    def __init__(self):
        self.urgency_queue = PriorityQueue()
        self.severity_queue = PriorityQueue()
        self.general_practitioner_queue = PriorityQueue()
        self.heart_queue = PriorityQueue()
        self.orthopedic_queue = PriorityQueue()
        self.ent_queue = PriorityQueue()

    
    def request_appointment(self, patient):
        self.urgency_queue.put((patient.get_urgency_level(), patient))
        self.severity_queue.put((patient.get_potential_severity(), patient))
        
        #adds the patient into the appropriate queue for the specified doctor
        doctor_specialty = patient.get_doctor_specialty()
        if doctor_specialty == SPECIALTY.GENERAL_PRACTITIONER:
            self.general_practitioner_queue.put((patient.get_urgency_level(), patient))
        elif doctor_specialty == SPECIALTY.HEART:
            self.heart_queue.put((patient.get_urgency_level(), patient))
        elif doctor_specialty == SPECIALTY.ORTHOPEDIC:
            self.orthopedic_queue.put((patient.get_urgency_level(), patient))
        elif doctor_specialty == SPECIALTY.ENT:
            self.ent_queue.put((patient.get_urgency_level(), patient)) 

    #appointment for patient with highest urgency level is done
    def process_urgency_queue(self):
        while not self.urgency_queue.empty():
            patient = self.urgency_queue.get()    
    #appointment for patient with highest potential severity level is done
    def process_severity_queue(self):
        while not self.severity_queue.empty():
            patient = self.severity_queue.get()
    
    #this queue processes everytime a patient of that specialty is seen and 
    #is a redundant system that helps the doctors know which patients are in their department of care and which are not.
    def process_specialty_queue(self, specialty_queue):
        while not specialty_queue.empty():
            patient = specialty_queue.get()



'''
QUESTION 2:
Now suppose that after seeing 5 patients, doctors need to take at least a 20-minute break. How would you modify your design to accomplish this?
I would a new variable for doctor status. Since doctors in the real world would have to take more than just 20 minute breaks every 
5 patients (working hours, lunch break, etc.). For the status options, I would use, one, two, three, four and five patient 
status (each for how many patents seen since break), a break status that would reset after 20 minutes and a off status meaning they are 
not working right now. After every queue process, the doctor status would update.

Question 3
Describe a situation related to the urgent care clinic where inheritance would be useful. Again, do NOT write code, only explain your thoughts in a block comment.
Inheritance could be used on doctors. There could be a general doctors class and specialty of doctors could use inheritance. This is because all the doctors would 
share the same attributes such as their stamina status and name. I could have a class with just the general doctor stuff like name and status. 
I could then use inheritance to have doctors with specialties.

'''