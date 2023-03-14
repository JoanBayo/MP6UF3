# coding=utf-8
import Tkinter as tk

from eulexistdb import db

EXISTDB_SERVER_USER = 'admin'
EXISTDB_SERVER_PASSWORD = 'admin'
EXISTDB_SERVER_URL = "http://localhost:8080/exist"
EXISTDB_ROOT_COLLECTION = "/MP03UF6"

db = db.ExistDB(server_url=EXISTDB_SERVER_URL, username='admin', password='admin')

def SalaryUpdateEmployersAction():
    lbl_resultatSalaryUpdate.config(text="AQUEST APARTAT NO ESTA DISPONIBLE")

def SalaryEmployersAction():
    try:
        departament = ent_departament.get()
        salary = float(ent_salary.get())

        query = """update replace //treballador[departament='""" + departament + """']/sou/text()
                        with '""" + str(salary) + """'"""

        res = db.executeQuery(query)

        if res != 0:
            lbl_resultatSalary.config(text="El sou s'ha afeguit correctament")
            ent_departament.delete(0, tk.END)
            ent_salary.delete(0, tk.END)
        else:
            lbl_resultatSalary.config(text="Aquest departament no existix")
    except:
        lbl_resultatSalary.config(text="Algo ha fallat")
def ShowEmployersAction():
    try:
        show = ""
        dni = ent_Dni.get()
        query = """for $treballador in //treballador
                        where $treballador/dni = '""" + dni + """'
                        return $treballador"""

        res = db.executeQuery(query)
        answer = db.getHits(res)
        for i in range(answer):
            show = show + str(db.retrieve(res, i)) + '\n'

        lbl_resultatShow.delete('1.0', tk.END)
        lbl_resultatShow.insert('1.0', show)

    except:
        lbl_resultatShow.config(text="Algo ha fallat")
def UpdateEmployersAction():
    try:
        departament = ent_Department.get()
        dni = ent_Dni.get()
        nom = ent_Name.get()
        cognom = ent_Surname.get()
        telefon = ent_TelefonNumber.get()
        mail = ent_Mail.get()
        sou = ent_Salary.get()

        if checkDni(dni):
            query = """update replace //treballador[dni='"""+ dni +"""'] 
                           <treballador>\n 
                               <departament>""" + str(departament) + """</departament>\n
                               <dni>""" + str(dni) + """</dni>\n
                               <nom>""" + nom + """</nom>\n
                               <cognom>""" + cognom + """</cognom>\n
                               <telefon>""" + str(telefon) + """</telefon>\n
                               <mail>""" + mail + """</mail>\n
                               <sou>""" + sou + """</sou>\n
                       <treballador>"""
            res = db.executeQuery(query)

            if res != 0:
                lbl_resultatUpdate.config(text="Treballador modificat correctament")
                ent_Dni.delete(0, tk.END)
                ent_Name.delete(0, tk.END)
                ent_Surname.delete(0, tk.END)
                ent_TelefonNumber.delete(0, tk.END)
                ent_Mail.delete(0, tk.END)
                ent_Salary.delete(0, tk.END)
                ent_Department.delete(0, tk.END)
            else:
                lbl_resultatUpdate.config(text="El treballado no s'ha pogut modificar")
        else:
            lbl_resultatUpdate.config(text="No hi ha cap treballador amb aquest DNI")





    except Exception as e:
        lbl_resultatAdd.config(text="Algo a fallat")

def deleteEmployersAction():
    try:
        dni = ent_Dni.get()

        if checkDni(dni):
            query = """update delete //treballador[dni='""" + dni + """']"""

            res = db.executeQuery(query)

            if res != 0:
                lbl_resultatDelete.config(text="Treballador eliminat")
                ent_Dni.delete(0, tk.END)

        else:
            lbl_resultatDelete.config(text="Aquest DNI no és correcte")

    except:
        lbl_resultatDelete.config(text="Algo ha fallat")


def checkDni(dni):
    alldni = []
    try:
        query = db.executeQuery("""for $dni in //treballador/dni
                                    return $dni/text()""")
        answer = db.getHits(query)

        for i in range(answer):
            alldni.append(str(db.retrieve(query, i)))
        if dni in alldni:
            return True
        else:
            return False
    except:
        pass


def addEmployersAction():
    try:
        departament = ent_Department.get()
        dni = ent_Dni.get()
        nom = ent_Name.get()
        cognom = ent_Surname.get()
        telefon = ent_TelefonNumber.get()
        mail = ent_Mail.get()
        sou = ent_Salary.get()
        
        if checkDni(dni):
            lbl_resultatAdd.config(text="Ja hi ha un treballador amb aquest DNI")
        else:
            query = """update insert 
                        <treballador>\n 
                            <departament>""" + str(departament) + """</departament>\n
                            <dni>""" + str(dni) + """</dni>\n
                            <nom>""" + nom + """</nom>\n
                            <cognom>""" + cognom + """</cognom>\n
                            <telefon>""" + str(telefon) + """</telefon>\n
                            <mail>""" + mail + """</mail>\n
                            <sou>""" + sou + """</sou>\n
                    <treballador>\n
                    into /personal"""

            res = db.executeQuery(query)
            if res != 0:
                lbl_resultatAdd.config(text="Treballador afeguit correctament")
                ent_Dni.delete(0, tk.END)
                ent_Name.delete(0, tk.END)
                ent_Surname.delete(0, tk.END)
                ent_TelefonNumber.delete(0, tk.END)
                ent_Mail.delete(0, tk.END)
                ent_Salary.delete(0, tk.END)
                ent_Department.delete(0, tk.END)
            else:
                lbl_resultatAdd.config(text="El treballado no s'ha pogut afeguir")


    except Exception as e:
        lbl_resultatAdd.config(text="Algo a fallat")



def UpdateSalary():
    frameMenu.pack_forget()
    frameUpdateSalary.pack()


def BackToMenuFromUpdateSalary():
    frameUpdateSalary.pack_forget()
    frameMenu.pack()


def openPutSalaryAllMenu():
    frameMenu.pack_forget()
    framePutSalaryAll.pack()


def BackToMenuFromPutSalaryAll():
    framePutSalaryAll.pack_forget()
    frameMenu.pack()


def openSelectAllEmplyers():
    frameMenu.pack_forget()
    frameSelectAllEmplpoyers.pack()


def BackToMenuFromSelectAllEmployers():
    frameSelectAllEmplpoyers.pack_forget()
    frameMenu.pack()


def openSelectEmplyers():
    frameMenu.pack_forget()
    frameSelectEmplpoyers.pack()


def BackToMenuFromSelectEmployers():
    frameSelectEmplpoyers.pack_forget()
    frameMenu.pack()


def openUpdateEmplyers():
    frameMenu.pack_forget()
    frameUpdateEmplpoyers.pack()


def BackToMenuFromUpdateEmployers():
    frameUpdateEmplpoyers.pack_forget()
    frameMenu.pack()


def openEmployersMenu():
    frameMenu.pack_forget()
    frameEmployers.pack()


def backToMenuFromAddEmployers():
    frameEmployers.pack_forget()
    frameMenu.pack()


def openDeleteEmplyerMenu():
    frameMenu.pack_forget()
    frameDeleteEmployers.pack()


def backToMenuFromDeleteEmployers():
    frameDeleteEmployers.pack_forget()
    frameMenu.pack()


def leaveGame():
    window.destroy()


# MENU PRINCIPAL
window = tk.Tk()
window.geometry("700x300")
frameMenu = tk.Frame(window)
frameMenu.pack()

buttonAddEmployers = tk.Button(frameMenu,
                               text="Insertar un Treballador",
                               command=openEmployersMenu)
buttonGetOut = tk.Button(frameMenu,
                         text="SORTIR",
                         command=leaveGame)
buttonDeleteEmployer = tk.Button(frameMenu,
                                 text="Eliminiar un treballador",
                                 command=openDeleteEmplyerMenu)
buttonUpdateEmployer = tk.Button(frameMenu,
                                 text="Actualitzar un treballador",
                                 command=openUpdateEmplyers)
buttonSelectEmployer = tk.Button(frameMenu,
                                 text="Veure un treballador",
                                 command=openSelectEmplyers)
buttonSelectAllEmployer = tk.Button(frameMenu,
                                    text="Veure tots els treballadors",
                                    command=openSelectAllEmplyers)
buttonPutSalaryAll = tk.Button(frameMenu,
                               text="Posar sou a un departament",
                               command=openPutSalaryAllMenu)
buttonPutUpdateSalary = tk.Button(frameMenu,
                                  text="Augmenta el Sou",
                                  command=UpdateSalary)

buttonAddEmployers.pack()
buttonSelectEmployer.pack()
buttonSelectAllEmployer.pack()
buttonUpdateEmployer.pack()
buttonDeleteEmployer.pack()
buttonPutSalaryAll.pack()
buttonPutUpdateSalary.pack()
buttonGetOut.pack(pady="10")

# AUMENTAR SOU TREBALLADORS
frameUpdateSalary = tk.Frame(window)
lbl_Dni = tk.Label(frameUpdateSalary,
                   text="Posa el DNI del treballador veure: ",
                   foreground="black",
                   background="white smoke"
                   )
ent_Dni = tk.Entry(frameUpdateSalary, bg="white", width="50")

buttonBackToMenuFromUpdateSalary = tk.Button(frameUpdateSalary,
                                             text="Menu principal",
                                             command=BackToMenuFromUpdateSalary)
lbl_resultatSalaryUpdate = tk.Label(frameUpdateSalary,
                      foreground="black",
                      )
buttonSalaryUpdateEmployersAction = tk.Button(frameUpdateSalary,
                                     text="Afeguir Treballador",
                                     command=SalaryUpdateEmployersAction)
lbl_Dni.pack(pady="10")
ent_Dni.pack(pady="5")
lbl_resultatSalaryUpdate.pack()
buttonSalaryUpdateEmployersAction.pack()
buttonBackToMenuFromUpdateSalary.pack(pady="15")

# ASSIGNAR SOU BASE DEPARTAMENT
framePutSalaryAll = tk.Frame(window)
lbl_departament = tk.Label(framePutSalaryAll,
                   text="Posa el departament al que vols posar sou: ",
                   foreground="black",
                   background="white smoke"
                   )
ent_departament = tk.Entry(framePutSalaryAll, bg="white", width="50")

lbl_salary = tk.Label(framePutSalaryAll,
                   text="Posa el sou del departament: ",
                   foreground="black",
                   background="white smoke"
                   )
ent_salary = tk.Entry(framePutSalaryAll, bg="white", width="50")

buttonBackToMenuFromPutSalaryAll = tk.Button(framePutSalaryAll,
                                             text="Menu principal",
                                             command=BackToMenuFromPutSalaryAll)

lbl_resultatSalary = tk.Label(framePutSalaryAll,
                      foreground="black",
                      )

buttonSalaryEmployersAction = tk.Button(framePutSalaryAll,
                                     text="Afeguir Treballador",
                                     command=SalaryEmployersAction)


lbl_departament.pack(pady="10")
ent_departament.pack(pady="5")
lbl_salary.pack(pady="10")
ent_salary.pack(pady="5")
lbl_resultatSalary.pack()
buttonSalaryEmployersAction.pack()
buttonBackToMenuFromPutSalaryAll.pack(pady="15")





# LLISTAR TREBALLADORS
frameSelectAllEmplpoyers = tk.Frame(window)

buttonBackToMenuFromSelectEmployers = tk.Button(frameSelectAllEmplpoyers,
                                                text="Menu principal",
                                                command=BackToMenuFromSelectAllEmployers)
lbl_EmployersLists = tk.Text(master=frameSelectAllEmplpoyers,
                      foreground="black",
                      background="white",
                      width="40",
                      height="15",
                      )

lbl_EmployersLists.pack()
buttonBackToMenuFromSelectEmployers.pack(pady="15")

# MOSTRAR TREBALLADOR
frameSelectEmplpoyers = tk.Frame(window)
lbl_Dni = tk.Label(frameSelectEmplpoyers,
                   text="Posa el DNI del treballador veure: ",
                   foreground="black",
                   background="white smoke"
                   )
ent_Dni = tk.Entry(frameSelectEmplpoyers, bg="white", width="50")

buttonBackToMenuFromSelectEmployers = tk.Button(frameSelectEmplpoyers,
                                                text="Menu principal",
                                                command=BackToMenuFromSelectEmployers)
lbl_resultatShow = tk.Label(frameSelectEmplpoyers,
                      foreground="black",
                      )

buttonShowEmployersAction = tk.Button(frameSelectEmplpoyers,
                                     text="Afeguir Treballador",
                                     command=ShowEmployersAction)

lbl_Dni.pack(pady="10")
ent_Dni.pack(pady="5")
lbl_resultatShow.pack()
buttonShowEmployersAction.pack()
buttonBackToMenuFromSelectEmployers.pack(pady="15")




# MODIFICAR TREBALLADORS
frameUpdateEmplpoyers = tk.Frame(window)
lbl_Dni = tk.Label(frameUpdateEmplpoyers,
                   text="Posa el DNI del treballador a modificar: ",
                   foreground="black",
                   background="white smoke"
                   )
ent_Dni = tk.Entry(frameUpdateEmplpoyers, bg="white", width="50")

buttonBackToMenuFromUpdateEmployers = tk.Button(frameUpdateEmplpoyers,
                                                text="Menu principal",
                                                command=BackToMenuFromUpdateEmployers)

lbl_resultatUpdate = tk.Label(frameUpdateEmplpoyers,
                      foreground="black",
                      )

buttonUpdateEmployersAction = tk.Button(frameUpdateEmplpoyers,
                                     text="Afeguir Treballador",
                                     command=UpdateEmployersAction)
lbl_Dni.pack(pady="10")
ent_Dni.pack(pady="5")
lbl_resultatUpdate.pack()
buttonUpdateEmployersAction.pack()
buttonBackToMenuFromUpdateEmployers.pack(pady="15")



# ELIMINAR TREBALLADORS
frameDeleteEmployers = tk.Frame(window)
lbl_Dni = tk.Label(frameDeleteEmployers,
                   text="Posa el DNI del treballador a eliminar: ",
                   foreground="black",
                   background="white smoke"
                   )
ent_Dni = tk.Entry(frameDeleteEmployers, bg="white", width="50")

buttonBackToMenuFromDeleteEmployers = tk.Button(frameDeleteEmployers,
                                                text="Menu principal",
                                                command=backToMenuFromDeleteEmployers)

lbl_resultatDelete = tk.Label(frameDeleteEmployers,
                      foreground="black",
                      )

buttonDeleteEmployersAction = tk.Button(frameDeleteEmployers,
                                     text="Afeguir Treballador",
                                     command=deleteEmployersAction)

lbl_Dni.pack(pady="10")
ent_Dni.pack(pady="5")
lbl_resultatDelete.pack()
buttonDeleteEmployersAction.pack()

buttonBackToMenuFromDeleteEmployers.pack(pady="15")




# AFEGUIR TREBALLADORS
frameEmployers = tk.Frame(window)

lbl_Department = tk.Label(frameEmployers,
                          text="Departament: ",
                          foreground="black",
                          background="white smoke"
                          )

ent_Department = tk.Entry(frameEmployers, bg="white", width="50")

lbl_Dni = tk.Label(frameEmployers,
                   text="DNI: ",
                   foreground="black",
                   background="white smoke"
                   )
ent_Dni = tk.Entry(frameEmployers, bg="white", width="50")

lbl_Name = tk.Label(frameEmployers,
                    text="Nom: ",
                    foreground="black",
                    background="white smoke"
                    )
ent_Name = tk.Entry(frameEmployers, bg="white", width="50")

lbl_Surname = tk.Label(frameEmployers,
                       text="Cognom: ",
                       foreground="black",
                       background="white smoke"
                       )
ent_Surname = tk.Entry(frameEmployers, bg="white", width="50")

lbl_TelefonNumber = tk.Label(frameEmployers,
                             text="Numero de telefon: ",
                             foreground="black",
                             background="white smoke"
                             )
ent_TelefonNumber = tk.Entry(frameEmployers, bg="white", width="50")

lbl_Mail = tk.Label(frameEmployers,
                    text="Mail: ",
                    foreground="black",
                    background="white smoke"
                    )
ent_Mail = tk.Entry(frameEmployers, bg="white", width="50")

lbl_Salary = tk.Label(frameEmployers,
                      text="Sou: ",
                      foreground="black",
                      background="white smoke"
                      )
ent_Salary = tk.Entry(frameEmployers, bg="white", width="50")

buttonAddEmployersAction = tk.Button(frameEmployers,
                                     text="Afeguir Treballador",
                                     command=addEmployersAction)

buttonBackToMenuFromAddEmployers = tk.Button(frameEmployers,
                                             text="Menu principal",
                                             command=backToMenuFromAddEmployers)

lbl_resultatAdd = tk.Label(frameEmployers,
                      foreground="black",
                      )

lbl_Department.grid(column=0, row=1)
ent_Department.grid(column=1, row=1)

lbl_Dni.grid(column=0, row=2)
ent_Dni.grid(column=1, row=2)

lbl_Name.grid(column=0, row=3)
ent_Name.grid(column=1, row=3)

lbl_Surname.grid(column=0, row=4)
ent_Surname.grid(column=1, row=4)

lbl_TelefonNumber.grid(column=0, row=5)
ent_TelefonNumber.grid(column=1, row=5)

lbl_Mail.grid(column=0, row=6)
ent_Mail.grid(column=1, row=6)

lbl_Salary.grid(column=0, row=7)
ent_Salary.grid(column=1, row=7)
lbl_resultatAdd.grid(column=1, row=8)
buttonAddEmployersAction.grid(column=1, row=9, pady=5)
buttonBackToMenuFromAddEmployers.grid(column=0, row=9, pady=5)

window.mainloop()
