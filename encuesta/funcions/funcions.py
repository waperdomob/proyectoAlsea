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
                'soporte' : pos.soporteRHC,
                'amabilidad': pos.amabilidadRHC,
                'efectividad': pos.efectividadRHC,                
            }
        RH_Contratación.append(obj1)
        obj2 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : pos.soporteRHN,
                'amabilidad':pos.amabilidadRHN,
                'efectividad':pos.efectividadRHN,                
            }
        RH_Nomina.append(obj2)
        obj3 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : pos.soporteCC,
                'amabilidad' :pos.amabilidadCC,
                'efectividad':pos.efectividadCC,             
            }
        Contac_center.append(obj3)
        obj4 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : pos.soporteGA,
                'amabilidad' :pos.amabilidadGA,
                'efectividad':pos.efectividadGA,    
            }
        Gerencia_Administrativa.append(obj4)
        obj5 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : pos.soporteFC,
                'amabilidad' :pos.amabilidadFC,
                'efectividad':pos.efectividadFC,
            }
        Finanzas_Cpp.append(obj5)
        obj6 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : pos.soporteFV,
                'amabilidad' :pos.amabilidadFV,
                'efectividad':pos.efectividadFV,    
            }
        Finanzas_Vposs.append(obj6)
        obj7 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : pos.soporteFT,
                'amabilidad' :pos.amabilidadFT,
                'efectividad':pos.efectividadFT,          
            }
        Finanzas_tes.append(obj7)
        obj8 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' :pos.soporteSSCE,
                'amabilidad':pos.amabilidadSSCE, 
                'efectividad':pos.efectividadSSCE,                
            }
        Sac_supli_chain.append(obj8)
        obj9 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' :pos.soporteSSCA,
                'amabilidad':pos.amabilidadSSCA, 
                'efectividad':pos.efectividadSSCA,               
            }
        Sac_supli_chain_AX.append(obj9)
        obj10 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' :pos.soporteSSCC,
                'amabilidad':pos.amabilidadSSCC,
                'efectividad':pos.efectividadSSCC,            
            }
        Sac_supli_chain_CP.append(obj10)
        obj11 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : pos.soporteMC,
                'amabilidad' :pos.amabilidadMC,
                'efectividad':pos.efectividadMC,           
            }
        Marketing.append(obj11)
        obj12 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' :pos.soporteHSEQ,
                'amabilidad':pos.amabilidadHSEQ,
                'efectividad':pos.efectividadHSEQ,            
            }
        Hseq.append(obj12)
        obj13 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' :pos.soporteLEGAL,
                'amabilidad':pos.amabilidadLEGAL,
                'efectividad':pos.efectividadLEGAL,
            }
        Legal.append(obj13)
        obj14 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : pos.soporteTEC,
                'amabilidad' :pos.amabilidadTEC,
                'efectividad' :pos.efectividadTEC,            
            }
        Tecnologia.append(obj14)
        obj15 = {
                
                'nombre': pos.nombre,
                'cargo': pos.cargo,
                'tienda': pos.tienda,
                'soporte' : pos.soporteAUD,
                'amabilidad':pos.amabilidadAUD,
                'efectividad':pos.efectividadAUD,         
            }
        Auditoria.append(obj15)
    Todos=[RH_Contratación,RH_Nomina,Contac_center,Gerencia_Administrativa,Finanzas_Cpp,Finanzas_Vposs,Finanzas_tes,Sac_supli_chain,Sac_supli_chain_AX,Sac_supli_chain_CP,Marketing,Hseq,Tecnologia,Auditoria]
    return Todos