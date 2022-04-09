function eliminar_Reporte() {

  modalT
  reportBtn.addEventListener('click', ()=>{
   
    reportForm.addEventListener('eliminar', e=>{
      e.preventDefault()
      const formData = new FormData()
      formData.append('csrfmiddlewaretoken',csrf)
      formData.append('name', reportName.value)
      formData.append('remark', reportRemark.value)
      for (let i = 0; i< imagenes.length; i++) {
        formData.append('imagen'+i, imagenes[i].src)
      }    
      console.log(formData)
      $.ajax({
        type: 'POST',
        url:'/reporte/save/',
        data: formData,
        success: function(response){
          console.log(response)
          handleAlerts('success','Reporte creado')
        },
        error: function(error) {
          console.log(error)
          handleAlerts('danger','ups... Algo salió mal')
          
        },
        processData: false,
        contentType: false,
      })
    })
  })

  }