from encuesta.models import Encuestas,EncuestasManager

def filtrar(filtros):   

    if filtros['ciudad'] and filtros['tienda'] and filtros['cargo'] and filtros['marca']:
        encuestas = Encuestas.encuestas_objects.get_by_all(filtros['ciudad'],filtros['tienda'],filtros['cargo'],filtros['marca'])
            
    elif filtros['ciudad'] and filtros['tienda'] and filtros['cargo']:
        encuestas = Encuestas.encuestas_objects.get_by_three(filtros['ciudad'],filtros['tienda'],filtros['cargo'])
    elif filtros['ciudad'] and filtros['tienda'] and filtros['marca']:
        encuestas = Encuestas.encuestas_objects.get_by_three2(filtros['ciudad'],filtros['tienda'],filtros['marca'])
    elif filtros['tienda'] and filtros['cargo'] and filtros['marca']:
        encuestas = Encuestas.encuestas_objects.get_by_three3(filtros['tienda'],filtros['cargo'],filtros['marca'])
    elif filtros['ciudad'] and filtros['cargo'] and filtros['marca']:
        encuestas = Encuestas.encuestas_objects.get_by_three4(filtros['ciudad'],filtros['cargo'],filtros['marca'])
        
    elif filtros['ciudad'] and filtros['tienda']:
        encuestas = Encuestas.encuestas_objects.get_by_two(filtros['ciudad'],filtros['tienda'])
    elif filtros['ciudad'] and filtros['cargo']:
        encuestas = Encuestas.encuestas_objects.get_by_two2(filtros['ciudad'],filtros['cargo'])
    elif filtros['ciudad'] and filtros['marca']:
        encuestas = Encuestas.encuestas_objects.get_by_two3(filtros['ciudad'],filtros['marca'])
    elif filtros['tienda'] and filtros['cargo']:
        encuestas = Encuestas.encuestas_objects.get_by_two4(filtros['tienda'],filtros['cargo'])
    elif filtros['tienda'] and filtros['marca']:
        encuestas = Encuestas.encuestas_objects.get_by_two5(filtros['tienda'],filtros['marca'])
    elif filtros['cargo'] and filtros['marca']:
        encuestas = Encuestas.encuestas_objects.get_by_two6(filtros['cargo'],filtros['marca'])

    elif filtros['ciudad']:
        encuestas = Encuestas.encuestas_objects.get_by_ciudad(filtros['ciudad'])
    elif filtros['tienda']:
        encuestas = Encuestas.encuestas_objects.get_by_tienda(filtros['tienda'])
    elif filtros['cargo']:
        encuestas = Encuestas.encuestas_objects.get_by_cargo(filtros['cargo'])
    elif filtros['marca']:
        encuestas = Encuestas.encuestas_objects.get_by_marca(filtros['marca'])

    return encuestas


def pasar_dicc(encuestas):
    RH_Contratación =[]
    RH_Nomina = []
    Contac_center =[]
    Gerencia_Administrativa =[]
    Finanzas_Cpp =[]
    Finanzas_Vposs =[]
    Finanzas_tes =[]
    Sac_supli_chain =[]
    Sac_supli_chain_AX =[]
    Sac_supli_chain_CP =[]
    Marketing =[]
    Hseq=[]
    Legal=[]
    Tecnologia =[]
    Auditoria =[] 
    for pos in encuestas:
        obj1 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'SOPORTE' : int(pos.soporteRHC),
                'AMABILIDAD': int(pos.amabilidadRHC),
                'EFECTIVIDAD': int(pos.efectividadRHC),                
            }
        RH_Contratación.append(obj1)
        obj2 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'SOPORTE' : int(pos.soporteRHN),
                'AMABILIDAD':int(pos.amabilidadRHN),
                'EFECTIVIDAD':int(pos.efectividadRHN),                
            }
        RH_Nomina.append(obj2)
        obj3 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'SOPORTE' : int(pos.soporteCC),
                'AMABILIDAD' :int(pos.amabilidadCC),
                'EFECTIVIDAD':int(pos.efectividadCC),             
            }
        Contac_center.append(obj3)
        obj4 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'SOPORTE' : int(pos.soporteGA),
                'AMABILIDAD' : int(pos.amabilidadGA),
                'EFECTIVIDAD': int(pos.efectividadGA),    
            }
        Gerencia_Administrativa.append(obj4)
        obj5 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'SOPORTE' : int(pos.soporteFC),
                'AMABILIDAD' : int(pos.amabilidadFC),
                'EFECTIVIDAD': int(pos.efectividadFC),
            }
        Finanzas_Cpp.append(obj5)
        obj6 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'SOPORTE' : int(pos.soporteFV),
                'AMABILIDAD' : int(pos.amabilidadFV),
                'EFECTIVIDAD': int(pos.efectividadFV),    
            }
        Finanzas_Vposs.append(obj6)
        obj7 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'SOPORTE' : int(pos.soporteFT),
                'AMABILIDAD' :int(pos.amabilidadFT),
                'EFECTIVIDAD':int(pos.efectividadFT),          
            }
        Finanzas_tes.append(obj7)
        obj8 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'SOPORTE' :int(pos.soporteSSCE),
                'AMABILIDAD':int(pos.amabilidadSSCE), 
                'EFECTIVIDAD':int(pos.efectividadSSCE),                
            }
        Sac_supli_chain.append(obj8)
        obj9 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'SOPORTE' :int(pos.soporteSSCA),
                'AMABILIDAD':int(pos.amabilidadSSCA), 
                'EFECTIVIDAD':int(pos.efectividadSSCA),               
            }
        Sac_supli_chain_AX.append(obj9)
        obj10 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'SOPORTE' :int(pos.soporteSSCC),
                'AMABILIDAD':int(pos.amabilidadSSCC),
                'EFECTIVIDAD':int(pos.efectividadSSCC),            
            }
        Sac_supli_chain_CP.append(obj10)
        obj11 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'SOPORTE' : int(pos.soporteMC),
                'AMABILIDAD' :int(pos.amabilidadMC),
                'EFECTIVIDAD':int(pos.efectividadMC),           
            }
        Marketing.append(obj11)
        obj12 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'SOPORTE' :int(pos.soporteHSEQ),
                'AMABILIDAD':int(pos.amabilidadHSEQ),
                'EFECTIVIDAD':int(pos.efectividadHSEQ),            
            }
        Hseq.append(obj12)
        obj13 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'SOPORTE' :int(pos.soporteLEGAL),
                'AMABILIDAD':int(pos.amabilidadLEGAL),
                'EFECTIVIDAD':int(pos.efectividadLEGAL),
            }
        Legal.append(obj13)
        obj14 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'SOPORTE' : int(pos.soporteTEC),
                'AMABILIDAD' :int(pos.amabilidadTEC),
                'EFECTIVIDAD' :int(pos.efectividadTEC),            
            }
        Tecnologia.append(obj14)
        obj15 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'SOPORTE' : int(pos.soporteAUD),
                'AMABILIDAD':int(pos.amabilidadAUD),
                'EFECTIVIDAD':int(pos.efectividadAUD),         
            }
        Auditoria.append(obj15)


    Todos=[RH_Contratación,RH_Nomina,Contac_center,Gerencia_Administrativa,Finanzas_Cpp,Finanzas_Vposs,Finanzas_tes,Sac_supli_chain,Sac_supli_chain_AX,Sac_supli_chain_CP,Marketing,Hseq,Legal,Tecnologia,Auditoria]
    return Todos


    kmts = float(input("Ingrese los kilometros recorridos"))
    Lts_Gas = float(input("Ingrese los litros de combustible consumidos"))

    print("El consumo por Km es de: "+str((kmts/Lts_Gas)))


def agregar_elemento1(lista):
        
    lista.insert(0,"Suma")
    lista.insert(1,"----")
    lista.insert(2,"----")

    return lista

def agregar_elemento2(lista):
        
    lista.insert(0,"Promedio")
    lista.insert(1,"----")
    lista.insert(2,"----")

    return lista