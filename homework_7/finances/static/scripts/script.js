/**
 * Created by Егор on 30.11.2016.
 */
$(document).ready(function() {
    $("#updateAdress").click(function () {
        showAdressToChange();
    });
    // $("#sendAjaxAddress").click(function () {
    //     sendAjax();
    // });
});

function showAdressToChange() {
    $("#address").empty();
    $("#address").append("<form action='javascript:sendAjax();'><input id='contentAddress'/>");
    $("#address").append(" <input type='submit'>Update</input></form>");
}

function sendAjax() {
    alert("asdsa");
    var text = $("#contentAddress").innerText;
    $.ajax({
        type: "POST",
        url: "/update",
        data: {'address':text},
        dataType: 'text/plain',
        success: function() {
            $("#address").empty();
            $("#address").append('<h4>Your address: <b>{{ request.user.address }}</b>  <a id="updateAdress"><button>Change your address</button></a>');
            alert('You have successfully changed your address!');
        }
    });
}