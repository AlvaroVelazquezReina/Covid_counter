
from covid import Covid
#import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

## para que funcione tiene que estar conectado a internet

covid=Covid(source="worldometers")
def indv():
    def search():
        cname=ctname.get()
        covid = Covid(source="worldometers")
        casos = []
        confirmados = []
        activos = []
        muertos = []
        recuperados = []
        if cname=='':
            return messagebox.showerror('Error','Pais no encontrado')
        else:
                main.update()
                nombres_paises = cname.strip()
                nombres_paises = nombres_paises.replace(" ", ",")
                nombres_paises = nombres_paises.split(",")

                for x in nombres_paises:
                    casos.append(covid.get_status_by_country_name(x))
                    main.update()
                for y in casos:
                    confirmados.append(y["confirmed"])
                    activos.append(y["active"])
                    muertos.append(y["deaths"])
                    recuperados.append(y["recovered"])

                confirmados_p = mpatches.Patch(color="green", label="Confirmados")
                recuperados_p = mpatches.Patch(color="red", label="Recuperados")
                activos_p = mpatches.Patch(color="blue", label="Activos")
                muertes_p = mpatches.Patch(color="black", label="Muertes")

                plt.legend(handles=[confirmados_p, recuperados_p, muertes_p, activos_p])

                for x in range(len(nombres_paises)):
                    plt.bar(nombres_paises[x], confirmados[x],color="green")
                    plt.bar(nombres_paises[x], recuperados[x], color="red")
                    plt.bar(nombres_paises[x], activos[x], color="blue")
                    plt.bar(nombres_paises[x], muertos[x], color="black")
                plt.title("Casos de COVID-19 actuales")
                plt.xlabel("Pais")
                plt.ylabel("Casos (en millones)")
                plt.show()

    ctname=StringVar()
    st=Toplevel()
    st.geometry('500x100')
    st.title('Estatus individual')
    Label(st,text='Paises en ingles y sin espacios',font='Helvetica 12 bold').grid(row=0,column=1, pady = 10)
    Label(st,text='Inserte el nombre del pais:',font='Helvetica 12 bold').grid(row=2,column=1)
    Entry(st,width=15,textvariable=ctname).grid(row=2,column=2)
    Button(st,text='Buscar',command=search).grid(row=2,column=3)

#main window
main=Tk()
main.geometry('500x250')
main.title('Rastreador de Covid19')
Label(main,text='Corona Virus(COVID-19)',font='Helvetica 12 bold').pack(pady = 10)
Label(main,text='Casos totales confirmados: '+str(covid.get_total_confirmed_cases())).pack(pady = 5)
Label(main,text='Casos activos totales: '+str(covid.get_total_active_cases())).pack(pady = 5)
Label(main,text='Muertes totales: '+str(covid.get_total_deaths())).pack(pady = 5)
Label(main,text='Recuperados totales: '+str(covid.get_total_recovered())).pack(pady=5)
Button(main,text='Obtener estatus por paises',command=indv).pack(pady = 10)


main.mainloop()