$(document).ready(function () {

    $(document).on("click", '#updateAddress', function () {
        showAddressToChange();
    });

    $(document).on("click", '#updateFN', function () {
        showFirstNameToChange();
    });

    $(document).on("click", '#updateLN', function () {
        showLastNameToChange();
    });

    $(document).on("click", '#sendAddressAjax', function () {
        var csrftoken = getCookie('csrftoken');
        var text = $("#contentAddress").val();
        $.ajaxSetup({
            url: "/update/",
            type: "POST",
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        $.ajax({
            data: {'address': text},
            success: [
                function () {
                    $("#address")
                        .empty()
                        .append('' +
                            '<h4>Your address: <b>' + text + '</b>' +
                            '   <a id="updateAddress">' +
                            '       <button class="btn btn-success">' +
                            '           <span class="glyphicon glyphicon-pencil" aria-hidden="true"></span>' +
                            '       </button>' +
                            '   </a>' +
                            '</h4>');
                }
            ]
        });
    });

    $(document).on("click", '#sendFirstNameAjax', function () {
        var csrftoken = getCookie('csrftoken');
        var text = $("#contentFN").val();
        $.ajaxSetup({
            url: "/update/",
            type: "POST",
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        $.ajax({
            data: {'first_name': text},
            success: [
                function () {
                    $("#first_name")
                        .empty()
                        .append('' +
                            '<h4>Your first name: <b>' + text + '</b>' +
                            '   <a id="updateFN">' +
                            '       <button class="btn btn-success">' +
                            '           <span class="glyphicon glyphicon-pencil" aria-hidden="true"></span>' +
                            '       </button>' +
                            '   </a>' +
                            '</h4>');
                }
            ]
        });
    });

    $(document).on("click", '#sendLastNameAjax', function () {
        var csrftoken = getCookie('csrftoken');
        var text = $("#contentLN").val();
        $.ajaxSetup({
            url: "/update/",
            type: "POST",
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        $.ajax({
            data: {'last_name': text},
            success: [
                function () {
                    $("#last_name")
                        .empty()
                        .append('' +
                            '<h4>Your last name: <b>' + text + '</b>' +
                            '   <a id="updateLN">' +
                            '       <button class="btn btn-success">' +
                            '           <span class="glyphicon glyphicon-pencil" aria-hidden="true"></span>' +
                            '       </button>' +
                            '   </a>' +
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
        .append("<a id='sendAddressAjax'><button>Update</button></a>");
}

function showFirstNameToChange() {
    $("#first_name")
        .empty()
        .append("<input id='contentFN'/>")
        .append("<a id='sendFirstNameAjax'><button>Update</button></a>");
}

function showLastNameToChange() {
    $("#last_name")
        .empty()
        .append("<input id='contentLN'/>")
        .append("<a id='sendLastNameAjax'><button>Update</button></a>");
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