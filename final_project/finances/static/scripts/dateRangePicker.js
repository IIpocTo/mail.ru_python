$(function () {
    $('.datepicker').daterangepicker({
        autoUpdateInput: false,
        locale: {
            cancelLabel: 'Clear'
        }
    }).on('apply.daterangepicker', function (ev, picker) {
        $(this).val(picker.startDate.format('YYYY-MM-DD') + ' - ' + picker.endDate.format('YYYY-MM-DD'));
    }).on('cancel.daterangepicker', function (ev, picker) {
        $(this).val('');
    });
});

$(document).ready( function () {

   $(document).on("click","#graphShow",function () {
    $("#graphView").modal('show');
});

   $(document).on("click", "#histogramShow", function() {
    $("#histogramView").modal('show');
   })

});

function get_index(arr, el) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i][0] == el) {
            return i;
        }
    }
    return -1;
}