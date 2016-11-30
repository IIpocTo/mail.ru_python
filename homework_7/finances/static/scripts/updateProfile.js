$(document).ready(function () {

    $(document).on("click", '#updateAddress', function () {
        showAddressToChange();
    });

    $(document).on("click", '#sendAjax', function () {
        var csrftoken = getCookie('csrftoken');
        var text = $("#contentAddress").val();
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        $.ajax({
            type: "POST",
            url: "/update/",
            data: {'address': text},
            success: [
                function () {
                    $("#address")
                        .empty()
                        .append('' +
                            '<h4>Your address: <b>' + text + '</b>' +
                            '   <a id="updateAddress"><button>Change your address</button></a>' +
                            '</h4>');
                }
            ]
        });
    });

});

function showAddressToChange() {
    $("#address")
        .empty()
        .append("<input id='contentAddress'/>")
        .append("<a id='sendAjax'><button>Update</button></a>");
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}