
;(async () => {
    const response = await axios.get('/api/tables')
    fillTableList(response.data.objects)
  })();

function fillTableList(objects) {
    objects.forEach(element => {
        if (element.is_active==1) {
            table_list.innerHTML = table_list.innerHTML + '<a href="/table/' + element.name.toLowerCase() + '" class="sidenav-item">'+ element.name + '</a>'
        }
    });
}