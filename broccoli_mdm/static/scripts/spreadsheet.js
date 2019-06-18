function httpGet(theUrl) {
    var responce;
    $.ajax({
        url: theUrl,
        type: "GET",
        async:false,
        success: function (data) {
            responce = data;
        }
    });
    return responce
}

apiData = httpGet("/api/countries");
etalonTable = apiData.objects
table = JSON.parse(JSON.stringify(etalonTable))

spreadsheet = new Handsontable(hot, {
    data: table,
    colHeaders: true,
    minSpareRows: 2,
    licenseKey: 'non-commercial-and-evaluation',
    colHeaders: Object.keys(table[0]),
    rowHeaders: true
});


$(document).ready(function () {

});


function AppendCreateCDC(item) {
    if (window.cdc || (window.cdc = [])) {
        cdc.push(item);
    }
}

function detectChanges(originTable, modifiedTable) {
    originTable.forEach((element) => {
        modifiedElement = modifiedTable.find( x => x.id === element.id )
        if (modifiedElement && !_.isEqual(modifiedElement,element)) {
            prop = {"index": element.id, "changeType": "edit"}
            AppendCreateCDC(prop)
        }
        else if (!modifiedElement) {
            prop = {"index": element.id, "changeType": "delete"}
            AppendCreateCDC(prop)
        }
    })
    modifiedTable.forEach((element) => {  
        modifiedElement = originTable.find( x => x.id === element.id )
        if (_.isUndefined(modifiedElement) && !(_.isNull(element.id) || element.id == "") ) {
            prop = {"index": element.id, "changeType": "insert"}
            AppendCreateCDC(prop)
        }
    })  
    
}


function writeBack(changesArray, tableArray) {
    changesArray.forEach((element) => {
        row = tableArray.find( x => x.id === element.index )
        if (element.changeType == "edit") {
            axios.put("/api/countries/" + row.id, row)
        }
        else if (element.changeType == "insert") {
            axios.post("/api/countries", row)
        }
        else if (element.changeType == "delete") {
            console.log(element)
            axios.delete("/api/countries/" + element.index)
        }
    })
}


btn_save.onclick = function() {
    detectChanges(etalonTable, table)
    writeBack(cdc, table)
    cdc = []
    alert('data saved'); 
};


function getUrlPath(indent) {
    var url = window.location.pathname;
    var array = url.split("/");
    var array = array.slice(1).slice(-3);
    return array[indent];
}