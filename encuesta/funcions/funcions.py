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
                'soporte' : int(pos.soporteRHC),
                'amabilidad': int(pos.amabilidadRHC),
                'efectividad': int(pos.efectividadRHC),                
            }
        RH_Contratación.append(obj1)
        obj2 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : int(pos.soporteRHN),
                'amabilidad':int(pos.amabilidadRHN),
                'efectividad':int(pos.efectividadRHN),                
            }
        RH_Nomina.append(obj2)
        obj3 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : int(pos.soporteCC),
                'amabilidad' :int(pos.amabilidadCC),
                'efectividad':int(pos.efectividadCC),             
            }
        Contac_center.append(obj3)
        obj4 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : int(pos.soporteGA),
                'amabilidad' : int(pos.amabilidadGA),
                'efectividad': int(pos.efectividadGA),    
            }
        Gerencia_Administrativa.append(obj4)
        obj5 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : int(pos.soporteFC),
                'amabilidad' : int(pos.amabilidadFC),
                'efectividad': int(pos.efectividadFC),
            }
        Finanzas_Cpp.append(obj5)
        obj6 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : int(pos.soporteFV),
                'amabilidad' : int(pos.amabilidadFV),
                'efectividad': int(pos.efectividadFV),    
            }
        Finanzas_Vposs.append(obj6)
        obj7 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : int(pos.soporteFT),
                'amabilidad' :int(pos.amabilidadFT),
                'efectividad':int(pos.efectividadFT),          
            }
        Finanzas_tes.append(obj7)
        obj8 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' :int(pos.soporteSSCE),
                'amabilidad':int(pos.amabilidadSSCE), 
                'efectividad':int(pos.efectividadSSCE),                
            }
        Sac_supli_chain.append(obj8)
        obj9 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' :int(pos.soporteSSCA),
                'amabilidad':int(pos.amabilidadSSCA), 
                'efectividad':int(pos.efectividadSSCA),               
            }
        Sac_supli_chain_AX.append(obj9)
        obj10 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' :int(pos.soporteSSCC),
                'amabilidad':int(pos.amabilidadSSCC),
                'efectividad':int(pos.efectividadSSCC),            
            }
        Sac_supli_chain_CP.append(obj10)
        obj11 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : int(pos.soporteMC),
                'amabilidad' :int(pos.amabilidadMC),
                'efectividad':int(pos.efectividadMC),           
            }
        Marketing.append(obj11)
        obj12 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' :int(pos.soporteHSEQ),
                'amabilidad':int(pos.amabilidadHSEQ),
                'efectividad':int(pos.efectividadHSEQ),            
            }
        Hseq.append(obj12)
        obj13 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' :int(pos.soporteLEGAL),
                'amabilidad':int(pos.amabilidadLEGAL),
                'efectividad':int(pos.efectividadLEGAL),
            }
        Legal.append(obj13)
        obj14 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : int(pos.soporteTEC),
                'amabilidad' :int(pos.amabilidadTEC),
                'efectividad' :int(pos.efectividadTEC),            
            }
        Tecnologia.append(obj14)
        obj15 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : int(pos.soporteAUD),
                'amabilidad':int(pos.amabilidadAUD),
                'efectividad':int(pos.efectividadAUD),         
            }
        Auditoria.append(obj15)


    Todos=[RH_Contratación,RH_Nomina,Contac_center,Gerencia_Administrativa,Finanzas_Cpp,Finanzas_Vposs,Finanzas_tes,Sac_supli_chain,Sac_supli_chain_AX,Sac_supli_chain_CP,Marketing,Hseq,Legal,Tecnologia,Auditoria]
    return Todos