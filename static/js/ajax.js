function RenderTab(url, tabId) {
    $.ajax({
        url: url,
        type: 'GET',
        success: function(data) {
            $('#' + tabId).html(data);
        }
    });
}