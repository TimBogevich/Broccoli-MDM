function exportCSV(filename, jsonData) {
    var text = JSONtoCSV(table)
    var blob = new Blob([text], {type: "text/plain;charset=utf-8"});
    saveAs(blob, filename)
}


function JSONtoCSV(jsonArray, delimiter, dateFormat){
	dateFormat = dateFormat || 'YYYY-MM-DDTHH:mm:ss Z'; // ISO
	delimiter = delimiter || ';' ;
	
	var body = '';
	// En tete
	var keys = _.map(jsonArray[0], function(num, key){ return key; });
	body += keys.join(delimiter) + '\r\n';
	// Data
	for(var i=0; i<jsonArray.length; i++){
		var item = jsonArray[i];
		for(var j=0; j<keys.length; j++){
			var obj = item[keys[j]] ;
			if (_.isDate(obj)) { 				
				body += moment(obj).format(dateFormat) ;
			} else {
				body += obj ;
			}		
			if (j < keys.length-1) { 
				body += delimiter; 
			}
		}
		body += '\r\n';
	}
	return body;
}