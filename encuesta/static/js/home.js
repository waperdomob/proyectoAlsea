
var imagenes = new Array(15); 
const reportBtn = document.getElementById('report-btn')
const modalBody = document.getElementById('modal-body')
const misImagenes= document.querySelectorAll('.images');
const img = document.getElementById('img')
const reportName = document.getElementById('id_nombre')
const reportRemark = document.getElementById('id_comentario')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
const reportForm = document.getElementById('report_form')
const alertBox = document.getElementById('alert-box')

const handleAlerts = (type, msg) => {
  alertBox.innerHTML = `
    <div class="alert alert-${type}" role="alert">
      ${msg}
    </div>
  `
}
var i = 0
for (var item of misImagenes) {  
  imagenes[i] = item;
  i++;
}

if (img) {
  reportBtn.classList.remove('not-visible')
}

  reportBtn.addEventListener('click', ()=>{
   
  reportForm.addEventListener('submit', e=>{
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