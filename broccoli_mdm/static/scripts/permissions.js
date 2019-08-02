 function downloadData() {
     $.ajax({
        url: "/api/users",
        type: "GET",
        async : false
    }).done(function(data) {
        list_of_users = data.objects;
    })

     $.ajax({
        url: "/api/tables",
        type: "GET",
        async :false
    }).done(function(data) {
        list_of_tables = data.objects;
    })
}

 function ConvertFromId() {
     downloadData()
    
     table.forEach(function(item) {
            tab = list_of_tables.find( x => x.id === item.table_id );
            user = list_of_users.find( x => x.id === item.user_id );
            item.table_id = tab.name
            item.user_id = user.user_name
        })
     spreadsheet.render();

}

 function ConvertToId() {
    var table_with_id = JSON.parse(JSON.stringify(table))
    
     downloadData()
 
     table_with_id.forEach(function(item) {
        if (item.id) {
            tab = list_of_tables.find( x => x.name === item.table_id );
            user = list_of_users.find( x => x.user_name === item.user_id );
            item.table_id = tab.id
            item.user_id = user.id
        }
    })
    return table_with_id

}

ConvertFromId()

btn_save.onclick = function() {
    var table_with_id =  ConvertToId()
    detectChanges(etalonTable, table_with_id)
    writeBack(cdc, table_with_id)
    cdc = []
    showSnackBar("Data saved successfully");
};