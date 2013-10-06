

function cargarSeleccionado(){
	radios = document.getElementsByName('grupoSeleccionado');
	for(i in radios){
		if(radios[i].checked){
			document.getElementById('calificar-grupo').src = '../materia/'+radios[i].value+'.html';
			
		}
	}
}