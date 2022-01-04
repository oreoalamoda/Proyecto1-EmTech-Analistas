from datos import lifestore_searches as busquedas
from datos import lifestore_sales  as ventas
from datos import lifestore_products   as productos

# busquedas(id busqueda , id producto)
# ventas(id de venta,id de producto , calificación,fecha , reembolso)
# productos(id producto,nombre, precio,categoria, disponibilidad)

# Credenciales necesaria para tener acceso al programa
credenciales = {"usuario":["ADMIN","Retail_manager"],"contraseña":["prueba","EmTech" ]}

# Creamos una función  para pedir numeros enteros la cual generara un error en caso de no introducirlo
def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input(": "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num

# se crea la función menu la cual tendra el cuerpo de nuestro programa
def Menu():
    salir = False
# Se crea el ciclo el cual se ejecutara hasta que el usuario lo detenga
    while not salir:
# Se imprime las opciones del menu
        print("###################### LifeStore ######################")
        print("Bienvenido al menu de RetailAnalytics")
        print("Dado nuestro menu digita la opción de tu interés")
        print("1) Productos más vendidos y productos rezagados")
        print("2) Productos por reseña en el servicio")
        print("3) Total de ingresos y ventas")
        print("4) Salir:")
        print("###################### LifeStore #######################")

        
        opcion = pedirNumeroEntero()
        
        if opcion == 1:
            # dada la lista ventas creamos una nueva lista donde se guardaran 
            # el id de los productos vendidos
            ven= []
            for i in range(0,len(ventas)):
                ven.append(ventas[i][1])
            # se iteran sobre todos los productos para contar cuantas veces se ha vendido cada uno
            # y se crea una nueva lista con los valores
            contador=[]
            for i in range(1,len(productos)+1):
                contador.append(ven.count(i))
            # se ordena la lista que hemos creado
            contador.sort()
            # guardamos los ultimos 5 valores de la lista creada
            idmas = []
            for i in range(len(productos)-5,len(productos)):
                idmas.append(contador[i])
            # una vez tenemos los valores volvemos a ejecutar esta parte
            # para saber que posición dentro de la lista ocupan
            contador=[]
            for i in range(0,len(productos)):
                contador.append(ven.count(i))
            # la posición en la lista será el id del producto
            venp = []
            for i in idmas:
                venp.append(contador.index(i))
            # finalmente imprimimos los valores obtenidos
            print("###################################")
            print("lOS 5 PRODUCTOS MÁS VENDIDOS SON:")
            nombrep = []
            for i in venp:
                nombrep.append(productos[i][1])
            for i in range(0,5):
                print(nombrep[i],"Ventas:",idmas[i])
                
                
            
                
            # dada la lista busquedas creamos una nueva lista donde se guardaran 
            # el id de los productos mas buscados
            bus= []
            for i in range(0,len(busquedas)):
                bus.append(busquedas[i][1])
            # se iteran sobre todos los productos para contar cuantas veces se ha buscado cada uno
            # y se crea una nueva lista con los valores
            contadorbus=[]
            for i in range(1,len(productos)+1):
                contadorbus.append(bus.count(i))
            # se ordena la lista que hemos creado
            contadorbus.sort()
            # guardamos los ultimos 10 valores de la lista creada
            idbus = []
            for i in range(len(productos)-10,len(productos)):
                idbus.append(contadorbus[i])
            # una vez tenemos los valores volvemos a ejecutar esta parte
            # para saber que posición dentro de la lista ocupan
            contadorbus=[]
            for i in range(0,len(productos)):
                contadorbus.append(bus.count(i))
            # la posición en la lista será el id del producto
            busp = []
            for i in idbus:
                busp.append(contadorbus.index(i))
            # finalmente imprimimos los valores obtenidos
            print("###################################")
            print("lOS 10 PRODUCTOS MÁS BUSCADOS SON:")
            nombrebus = []
            for i in busp:
                nombrebus.append(productos[i][1])
            for i in range(0,10):
                print(nombrebus[i],"busquedas:",idbus[i])
                
                
            # dada la lista ventas creamos una nueva lista donde se guardará
            # el id de los productos vendidos por categorias

            idprocesadores= []
            idtarjeta = []
            idmadre=[]
            iddiscos=[]
            idusb = []
            idpantallas = []
            idbocinas = []
            idaudifonos = []
            for i in range(0,len(productos)):
                if productos[i][3] == "procesadores":
                    idprocesadores.append(productos[i][0])
                if productos[i][3] == "tarjetas de video":
                    idtarjeta.append(productos[i][0])   
                if productos[i][3] == "tarjetas madre":
                    idmadre.append(productos[i][0])   
                if productos[i][3] == "discos duros":
                    iddiscos.append(productos[i][0])   
                if productos[i][3] == "memorias usb":
                    idusb.append(productos[i][0])  
                if productos[i][3] == "pantallas":
                    idpantallas.append(productos[i][0]) 
                if productos[i][3] == "bocinas":
                    idbocinas.append(productos[i][0]) 
                if productos[i][3] == "audifonos":
                    idaudifonos.append(productos[i][0]) 
            #se iteran sobre todos los productos para contar cuantas veces se ha vendido cada uno
            #y se crea una nueva lista con los valores
            contador=[]
            for i in range(1,len(productos)+1):
                contador.append(ven.count(i))

                # se crea nueva lista por numero de ventas por categoria , id y producto:
            procesadores= []
            tarjeta = []
            madre=[]
            discos=[]
            usb = []
            pantallas = []
            bocinas = []
            audifonos = []
            for i in range(0,len(productos)):
                if i in idprocesadores:
                    procesadores.append([contador[i],i,productos[i][1]])
                if i in idtarjeta:
                    tarjeta.append([contador[i],i,productos[i][1]])
                if i in idmadre:
                    madre.append([contador[i],i,productos[i][1]])
                if i in iddiscos:
                    discos.append([contador[i],i,productos[i][1]])
                if i in idusb:
                    usb.append([contador[i],i,productos[i][1]])
                if i in idpantallas:
                    pantallas.append([contador[i],i,productos[i][1]])
                if i in idbocinas:
                    bocinas.append([contador[i],i,productos[i][1]])
                if i in idaudifonos:
                    audifonos.append([contador[i],i,productos[i][1]])
            #ordenamos cada una de las ventas por categoria
            procesadores.sort()
            tarjeta.sort()
            madre.sort()
            discos.sort()
            usb.sort()
            pantallas.sort()
            bocinas.sort()
            audifonos.sort()
            print("##################################################")
            print(" 5 PROCESADORES CON MENORES VENTAS")
            for i in range(0,5):
                print(procesadores[i][2],",con un numero de ventas de:",procesadores[i][0])
            print("##################################################")
            print(" 5 TARJETAS DE VIDEO CON MENORES VENTAS")
            for i in range(0,5):
                print(tarjeta[i][2],",con un numero de ventas de:",tarjeta[i][0])
            print("##################################################")
            print(" 5 TARJETAS MADRE CON MENORES VENTAS")
            for i in range(0,5):
                print(madre[i][2],",con un numero de ventas de:",madre[i][0])
            print("##################################################")
            print(" 5 DISCOS DUROS CON MENORES VENTAS")
            for i in range(0,5):
                print(discos[i][2],",con un numero de ventas de:",discos[i][0])
            print("##################################################")
            print(" 2 MEMORIAS USB CON MENORES VENTAS")
            for i in range(0,2):
                print(usb[i][2],",con un numero de ventas de:",usb[i][0])
            print("##################################################")
            print(" 5 PANTALLAS CON MENORES VENTAS")
            for i in range(0,5):
                print(pantallas[i][2],",con un numero de ventas de:",pantallas[i][0])
            print("##################################################")
            print(" 5 BOCINAS CON MENORES VENTAS")
            for i in range(0,4):
                print(bocinas[i][2],",con un numero de ventas de:",bocinas[i][0])
            print("##################################################")
            print(" 5 AUDIFONOS CON MENORES VENTAS")
            for i in range(0,5):
                print(audifonos[i][2],",con un numero de ventas de:",audifonos[i][0])
            
            #se iteran sobre todos los productos para contar cuantas veces se a buscado cada uno
            #y se crea una nueva lista con los valores
            buss = []
            for i in range(0,len(busquedas)):
                buss.append(busquedas[i][1])
                
            conbus=[]
            for i in range(1,len(productos)+1):
                conbus.append(buss.count(i))

                # se crea nueva lista por numero de ventas por categoria , id y producto:
            busprocesadores= []
            bustarjeta = []
            busmadre=[]
            busdiscos=[]
            bususb = []
            buspantallas = []
            busbocinas = []
            busaudifonos = []
            for i in range(0,len(productos)):
                if i in idprocesadores:
                    busprocesadores.append([conbus[i],i,productos[i][1]])
                if i in idtarjeta:
                    bustarjeta.append([conbus[i],i,productos[i][1]])
                if i in idmadre:
                    busmadre.append([conbus[i],i,productos[i][1]])
                if i in iddiscos:
                    busdiscos.append([conbus[i],i,productos[i][1]])
                if i in idusb:
                    bususb.append([conbus[i],i,productos[i][1]])
                if i in idpantallas:
                    buspantallas.append([conbus[i],i,productos[i][1]])
                if i in idbocinas:
                    busbocinas.append([conbus[i],i,productos[i][1]])
                if i in idaudifonos:
                    busaudifonos.append([conbus[i],i,productos[i][1]])
            #ordenamos cada una de las ventas por categoria
            busprocesadores.sort()
            bustarjeta.sort()
            busmadre.sort()
            busdiscos.sort()
            bususb.sort()
            buspantallas.sort()
            busbocinas.sort()
            busaudifonos.sort()
            print("##################################################")
            print(" PROCESADORES CON MENORES BUSQUEDAS")
            for i in range(0,9):
                print(busprocesadores[i][2],",con un numero de busquedas de:",busprocesadores[i][0])
            print("##################################################")
            print(" 10 TARJETAS DE VIDEO CON MENORES BUSQUEDAS")
            for i in range(0,10):
                print(bustarjeta[i][2],",con un numero de busquedas de:",bustarjeta[i][0])
            print("##################################################")
            print(" 10 TARJETAS MADRE CON MENORES BUSQUEDAS ")
            for i in range(0,10):
                print(busmadre[i][2],",con un numero de busquedas de:",busmadre[i][0])
            print("##################################################")
            print(" 10 DISCOS DUROS CON MENORES BUSQUEDAS")
            for i in range(0,10):
                print(busdiscos[i][2],",con un numero de busquedas de:",busdiscos[i][0])
            print("##################################################")
            print(" 2 DISCOS MEMORIAS USB CON MENORES BUSQUEAS")
            for i in range(0,2):
                print(bususb[i][2],",con un numero de busquedas de:",bususb[i][0])
            print("##################################################")
            print(" 10 PANTALLAS CON MENORES BUSQUEDAS")
            for i in range(0,10):
                print(buspantallas[i][2],",con un numero de busquedas de:",buspantallas[i][0])
            print("##################################################")
            print(" 4 BOCINAS CON MENORES BUSQUEDAS")
            for i in range(0,4):
                print(busbocinas[i][2],",con un numero de busquedas de:",busbocinas[i][0])
            print("##################################################")
            print(" 10 AUDIFONOS CON MENORES BUSQUEDAS")
            for i in range(0,10):
                print(busaudifonos[i][2],",con un numero de busquedas de:",busaudifonos[i][0])
                
                
            


        elif opcion==2:
            # dada la lista ventas creamos una nueva lista donde se guardaran 
            # el id de los productos vendidos
            proid = []
            for i in range(0,len(productos)):
                x = productos[i][0]
                proid.append(x)
    
            ven= []
            re = []
            for i in range(0,len(ventas)):
                ven.append(ventas[i][1])
                re.append(ventas[i][2])
            # se iteran sobre todos los productos para contar cuantas veces se ha buscado cada uno
            # y se crea una nueva lista con los valores
            contador=[]
            for i in range(1,len(productos)+1):
                contador.append(ven.count(i))
            # creamos la lista reseñas 
            reseñas = []
            # creamos un doble ciclo for usando la lista ven
            # este ciclo nos hará guardar la suma total de las reseñas
            # dado que están en orden la primera reseña corresponde
            # al producto con id == 1 y así sucesivamente
            for j in range(1,len(productos)+1):
                res = 0
                for i in range(0,len(ven)):
                    if ven[i] == j:
                        res = res +re[i]
                    #guardamos la lista de todas las reseñas
                reseñas.append(res)
            # Los productos que no han sido comprados no cuentan con reseñas
            # así que eliminaremos de contador  y de reseñas los producto que tenga valores de 0


            #eliminamos los valores iguales a 0 de todas las listas
            # Creamos una lista para guardar los valores que no contengan al cero 
            reseñas0 = []
            proid0 = []
            contador0=[]
            for i in range(0,len(proid)):
                if reseñas[i]!=0 :
                    reseñas0.append(reseñas[i]) 
                    proid0.append(proid[i]) 
                    contador0.append(contador[i]) 
            # ahora usamos la lista reseñas y la lista contador para obtener la reseña promedio
            for i in range(0,len(reseñas0)):
                reseñas0[i] = reseñas0[i]/contador0[i]

            #antes de ordenar la lista las metemos todas en una sola lista
            nueva = []
            for i in range(0,len(reseñas0)):
                nn = [reseñas0[i],proid0[i],contador0[i]]
                nueva.append(nn)

            # una vez hecho ordenamos la lista
            nueva.sort()
            # creamos una lista con las 5 peores reseñas
            peores = []
            for i in range(0,5):
                peores.append(nueva[i])
    
            # creamos una lista con las 5 mejores reseñas
            mejores = []
            for i in range(len(reseñas0)-5,len(reseñas0)):
                mejores.append(nueva[i])
            print("##################################################")
            print("LOS PRODUCTOS CON LAS MEJORES RESEÑAS SON:")
            # Creamos una lista con los nombre de todos los productos
            nombre = []
            for i in range(0,len(productos)):
                nombre.append(productos[i][1])
            # imprimomos los id que corresponden a las mejores reseñas
            for i in range(0,5):
                print(nombre[mejores[i][1]], ",con un reseña de :",mejores[i][0],"estrellas")
            print("##################################################")
            print("LOS PRODUCTOS CON LAS PEORES RESEÑAS SON:")
            # Creamos una lista con los nombres de todos los productos
            nombre = []
            for i in range(0,len(productos)):
                nombre.append(productos[i][1])
            # imprimomos los id que corresponden a las mejores reseñas
            for i in range(0,5):
                print(nombre[peores[i][1]], ",con un reseña de :",peores[i][0],"estrellas")

        elif opcion == 3:
            # dada la lista ventas creamos una nueva lista donde se guardaran 
            # el id de los productos vendidos
            proid = []
            for i in range(0,len(productos)):
                x = productos[i][0]
                proid.append(x)
    
            ven= []
            for i in range(0,len(ventas)):
                ven.append(ventas[i][1])
            # se iteran sobre todos los productos para contar cuantas veces se ha comprado cada uno
            # y se crea una nueva lista con los valores
            contador=[]
            for i in range(1,len(productos)+1):
                contador.append(ven.count(i))
            # Creamos la variable en la que se guardará el precio de cada producto
            precio = []
            for i in range(0,len(productos)):
                x = productos[i][2]
                precio.append(x)
            # calculamos las ventas totales anuales
            totalventas = sum(contador)
            # calculamos los ingresos totales anuales
            ingresos = 0
            for i in range(0,len(contador)):
                ingresos  = precio[i]*contador[i] + ingresos
            print("##################################################")
            print("VENTAS TOTALES ANUALES:",totalventas)
            print("INGRESOS TOTALES ANUALES:",ingresos)
            print("##################################################")
            print("VENTAS PROMEDIO MENSUALES:",totalventas/12)
            print("INGRESOS PROMEDIO MENSUALES:",ingresos/12)

            # creamos la lista fechas donde guardaremos las fechas de ventas
            fecha=[]
            for i in range(0,len(ventas)):
                fecha.append(ventas[i][3])
            #importamos la librería para poder cambiar la cadena a fechas
            from datetime import datetime
            # ventas en enero
            eneroini = datetime.strptime('01/01/2020', '%d/%m/%Y')
            enerofin = datetime.strptime('31/01/2020', '%d/%m/%Y')
            dt_dates = [datetime.strptime(date, '%d/%m/%Y') for date in fecha]
            enero = []
            for d in dt_dates:
                if d >= eneroini and d <= enerofin:
                    enero.append(d)
            # ventas en febrero
            febreroini = datetime.strptime('01/02/2020', '%d/%m/%Y')
            febrerofin = datetime.strptime('28/02/2020', '%d/%m/%Y')
            febrero = []
            for d in dt_dates:
                if d >= febreroini and d <= febrerofin:
                    febrero.append(d)
            # ventas en marzo
            marzoini = datetime.strptime('01/03/2020', '%d/%m/%Y')
            marzofin = datetime.strptime('31/03/2020', '%d/%m/%Y')
            marzo = []
            for d in dt_dates:
                if d >= marzoini and d <= marzofin:
                    marzo.append(d)
            # ventas en abril
            abrilini = datetime.strptime('01/04/2020', '%d/%m/%Y')
            abrilfin = datetime.strptime('30/04/2020', '%d/%m/%Y')
            abril = []
            for d in dt_dates:
                if d >= abrilini and d <= abrilfin:
                    abril.append(d)
            # ventas en mayo
            mayoini = datetime.strptime('01/05/2020', '%d/%m/%Y')
            mayofin = datetime.strptime('31/05/2020', '%d/%m/%Y')
            mayo = []
            for d in dt_dates:
                if d >= mayoini and d <= mayofin:
                    mayo.append(d)
            # ventas en junio
            junioini = datetime.strptime('01/06/2020', '%d/%m/%Y')
            juniofin = datetime.strptime('30/06/2020', '%d/%m/%Y')
            junio = []
            for d in dt_dates:
                if d >= junioini and d <= juniofin:
                    junio.append(d)
            # ventas en julio
            julioini = datetime.strptime('01/07/2020', '%d/%m/%Y')
            juliofin = datetime.strptime('31/07/2020', '%d/%m/%Y')
            julio = []
            for d in dt_dates:
                if d >= julioini and d <= juliofin:
                    julio.append(d)
            # ventas en agosto
            agostoini = datetime.strptime('01/08/2020', '%d/%m/%Y')
            agostofin = datetime.strptime('31/08/2020', '%d/%m/%Y')
            agosto = []
            for d in dt_dates:
                if d >= agostoini and d <= agostofin:
                    agosto.append(d)
            # ventas en septiembre
            septiembreini = datetime.strptime('01/09/2020', '%d/%m/%Y')
            septiembrefin = datetime.strptime('30/09/2020', '%d/%m/%Y')
            septiembre = []
            for d in dt_dates:
                if d >= septiembreini and d <= septiembrefin:
                    septiembre.append(d)
            # ventas en octubre
            octubreini = datetime.strptime('01/10/2020', '%d/%m/%Y')
            octubrefin = datetime.strptime('31/10/2020', '%d/%m/%Y')
            octubre = []
            for d in dt_dates:
                if d >= octubreini and d <= octubrefin:
                    octubre.append(d)
            # ventas en noviembre
            noviembreini = datetime.strptime('01/11/2020', '%d/%m/%Y')
            noviembrefin = datetime.strptime('30/11/2020', '%d/%m/%Y')
            noviembre = []
            for d in dt_dates:
                if d >= noviembreini and d <= noviembrefin:
                    noviembre.append(d)
            # ventas en diciembre
            diciembreini = datetime.strptime('01/12/2020', '%d/%m/%Y')
            diciembrefin = datetime.strptime('31/12/2020', '%d/%m/%Y')
            diciembre = []
            for d in dt_dates:
                if d >= diciembreini and d <= diciembrefin:
                    diciembre.append(d)

            # creamos la lista con los meses y sus ventas
            meses = [[len(enero),"enero"],[len(febrero),"febrero"],[len(marzo),"marzo"],[len(abril),"abril"],[len(mayo),"mayo"],[len(junio),"julio"]
            ,[len(julio),"julio"],[len(agosto),"agosto"],[len(septiembre),"septiembre"],[len(octubre),"octubre"],[len(noviembre),"noviembre"]
            ,[len(diciembre),"diciembre"]]
            # ordenamos la lista
            meses.sort()
            print("##################################################")
            print("EL NUMERO DE VENTAS POR MES ES :")
            for i in range(0,12):
                print(meses[i])
        elif opcion ==4:
            print("Has seleccionado la opción: Salir")
            salir = True
# credenciales para poder usar el programa
usuario = input("Ingrese su usuario:")
contraseña = input("Ingrese su contraseña:")
if usuario in credenciales["usuario"] and contraseña in credenciales["contraseña"]:
    print("Credenciales ingresadas correctamente")
    Menu()
else:
    print("Credenciales incorrectas, verifique sus datos")