$("#campo1").change(function() {
    if($("#campo1").val() === "1" ){
      $('#id_otrosDocs').prop('disabled', false);
    }else{
      $('#id_otrosDocs').prop('disabled', 'disabled');
    }
  });
  