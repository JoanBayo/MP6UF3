from eulexistdb import db
import Tkinter as tk

EXISTDB_SERVER_USER = 'admin'
EXISTDB_SERVER_PASSWORD = 'admin'
EXISTDB_SERVER_URL = "http://localhost:8080/exist"
EXISTDB_ROOT_COLLECTION = "/MP03UF6"

db = db.ExistDB(server_url=EXISTDB_SERVER_URL, username='admin', password='admin')


def openBD():
    try:
        lbl_answer.delete('1.0', 'end')
        string = ""
        query = ent_cuerry.get()
        res = db.executeQuery(query)
        hits = db.getHits(res)
        for i in range(hits):
            string = string + "\n" + str(db.retrieve(res, i))
        lbl_answer.insert('1.0',string)
    except Exception as e:
        pass
        error = "The query have the following Error:\n" + str(e)
        lbl_answer.insert('1.0', error)


window = tk.Tk()
window.geometry("500x500")

lbl_name = tk.Label(master=window,
                      text="BAYO",
                      foreground="midnight blue",
                      background="white smoke",
                    )

ent_cuerry = tk.Entry(master=window, bg="white", width="50", )
ent_cuerry.insert(0, "Add here your query")
btn_runCerry = tk.Button(master=window, text="RUN", command=openBD)

lbl_answer = tk.Text(master=window,
                      foreground="black",
                      background="white",
                      width="50",
                      height="20",
                      )
lbl_name.pack(pady="10")
ent_cuerry.pack(pady="5")
btn_runCerry.pack()
lbl_answer.pack()

window.mainloop()
