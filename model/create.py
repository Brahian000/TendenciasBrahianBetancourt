#Employee
class Employee():
    def __init__(self, fullName, idNumber, email, phoneNumber, bornDate, adress, rol, userName, password):
        self.fullName = fullName
        self.idNumber = idNumber
        self.email = email
        self.phoneNumber = phoneNumber
        self.bornDate = bornDate
        self.adress = adress
        self.rol = rol
        self.userName = userName
        self.password = password

#hospital
class Hospital():
    def __init__(self):
        self.patients=[]
        self.employees=[]
        self.appointments=[]
        self.clinicalHistories={}
        self.stockMedicine=[]
        self.procedures=[]
        self.orders=[]
        self.patientVisits=[]

#MedicalAppointment
class MedicalAppointment():
    def __init__(self, idPatient, idDoctor, date):
        self.id = idPatient
        self.idPatient = idPatient
        self.idDoctor = idDoctor
        self.date = date

#Invoice
class Invoice():
    def __init__(self, medicalAppointment, user):
        self.medicalAppointment = medicalAppointment
        self.patient = user



#Medication
class Medication():
    def __init__(self,id, name, price, dosage):
        self.id = id
        self.name = name
        self.price = price
        self.dosage = dosage

#Procedure
class Procedure():
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


#ClinicalVisit
class ClinicalVisit():
    def __init__(self, idPatient, date, vitalData):
        self.idPatient = idPatient
        self.date = date
        self.medication = []
        self.procedure = []
        self.vitalData = vitalData