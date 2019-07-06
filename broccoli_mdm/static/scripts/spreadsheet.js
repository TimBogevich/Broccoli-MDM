// Initialisation
apiUrl = "/api/"+ getUrlPath(1)
headerUrl = "/api_service/attributes/" + getUrlPath(1)
try {
    apiData = httpGet(apiUrl);
    tableHeader = JSON.parse(httpGet(headerUrl));
    etalonTable = apiData.objects;
    table = JSON.parse(JSON.stringify(etalonTable));
}
catch(error) {
    console.log(error)
    hot.innerText = "You have no permissions to read this object or it doesn't exists"
    throw new Error("You have no permissions to read this object or it doesn't exists");
}

var snackbarOptions =  {
    content: "Data saved", // text of the snackbar
    style: "toast", // add a custom class to your snackbar
    timeout: 5000
}





if(table.length == 0 ) {
    table = {}
    for (i in tableHeader) {
        table[tableHeader[i]] = ""
    }
    table["id"] = 1
    table = [table]
}

// Events
btn_save.onclick = function() {
    detectChanges(etalonTable, table)
    writeBack(cdc, table)
    cdc = []
    $.snackbar(snackbarOptions);
};

btn_add_row.onclick = function() {
    addRow();
}

// Interface
api_link.href = apiUrl





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


spreadsheet = new Handsontable(hot, {
    data: table,
    colHeaders: true,
    licenseKey: 'non-commercial-and-evaluation',
    colHeaders: Object.keys(table[0]),
    contextMenu: true,
    rowHeaders: true,
    hiddenColumns: true,
    startRows:  1
});

var pluginHideColumn = spreadsheet.getPlugin('hiddenColumns');
pluginHideColumn.hideColumn(
    spreadsheet.propToCol("id")
);
spreadsheet.render()

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
            axios.put(apiUrl + "/" + row.id, row)
        }
        else if (element.changeType == "insert") {
            axios.post(apiUrl, row)
        }
        else if (element.changeType == "delete") {
            console.log(element)
            axios.delete(apiUrl + "/" + element.index)
        }
    })
}





function getUrlPath(indent) {
    var url = window.location.pathname;
    var array = url.split("/");
    var array = array.slice(1).slice(-3);
    return array[indent];
}

function addRow() {
    ids = spreadsheet.getDataAtCol(
        spreadsheet.propToCol("id")
    )
    maxId = Math.max(...ids)
    table.push({"id": maxId+1})
    spreadsheet.render()
}