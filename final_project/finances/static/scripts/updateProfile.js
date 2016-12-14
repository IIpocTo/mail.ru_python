$(document).ready(function () {

    $(document).on("click", '#update', function () {
        showForm();
    });

    $(document).on("click", '#cancel', function () {
        cancelForm();
    });

    $('.alert').fadeOut(4000);

    $(document).on("click", '.delete', {}, function() {
        var rawId = $(this).attr('id');
        var _ = rawId.indexOf('_');
        var id = rawId.substring(6,_);
        var number = rawId.substring(_ + 1);
        deleteAccount(id, number);
    });

    $(document).on("click", '.edit', {}, function() {
        var rawId = $(this).attr('id');
        var _ = rawId.indexOf('_');
        var id = rawId.substring(4,_);
        var number = rawId.substring(_ + 1);
        editAccount(id, number);
    });

    $(document).on("click", '.delete-charge', {}, function() {
        var id = $(this).attr('id');
        deleteCharge(id);
    });

    $(document).on("click", "#sendDelete", function () {
        try {
            $("#deleteForm").submit();
        } catch (e) {
            console.log(e);
        }
    });

    $(document).on("click", "#sendEdit", function () {
        try {
            $("#editForm").submit();
        } catch (e) {
            console.log(e);
        }
    });

    $(document).on("click", "#sendDeleteCharge", function () {
        try {
            $("#deleteChargeForm").submit();
        } catch (e) {
            console.log(e);
        }
    });

});

function deleteCharge(id) {
    document.getElementById('deleteChargeForm').getElementsByTagName('input').item(0).attributes.getNamedItem('value').nodeValue = id;
    $("#deleteCharge").modal('show');
}

function deleteAccount(id, number) {
    document.getElementById('deleteForm').getElementsByTagName('input').item(0).attributes.getNamedItem('value').nodeValue = number;
    $("#deleteAccount").modal('show');
}

function editAccount(id, number) {
    var inputs = document.getElementById('editForm').getElementsByTagName('input');
    inputs.item(0).attributes.getNamedItem('value').nodeValue = document.location.href;
    inputs.item(1).attributes.getNamedItem('value').nodeValue = number;
    inputs.item(2).attributes.getNamedItem('value').nodeValue = number;
    $("#editAccount").modal('show');
}

function showForm() {
    var address = $('#ar').html();
    var lastName = $('#ln').html();
    var firstName = $('#fn').html();
    var username = $('#username').html();
    var email = $('#email').html();
    var phone = $('#phone').html();
    document.cookie = "address=" + address;
    document.cookie = "firstName=" + firstName;
    document.cookie = "lastName=" + lastName;
    document.cookie = "username=" + username;
    document.cookie = "email=" + email;
    document.cookie = "phone=" + phone;
    $("#personal")
        .empty()
        .append("<form method='post' action='/profile/'>" +
            "<div class='form-group'> " +
            "<label class='control-label' for='id_first_name'>First name</label> " +
            "<input class='form-control' id='id_first_name' maxlength='30' name='first_name' title='' type='text' value='" + getCookie("firstName") + "'> " +
            "</div>" +
            "<div class='form-group'> " +
            "<label class='control-label' for='id_last_name'>Last name</label>" +
            "<input class='form-control' id='id_last_name' maxlength='30' name='last_name' title='' type='text' value='" + getCookie("lastName") + "'>" +
            "</div> " +
            "<div class='form-group'> " +
            "<label class='control-label' for='id_address'>Address</label>" +
            "<input class='form-control' id='id_address' maxlength='100' name='address' title='' type='text' value='" + getCookie("address") + "'>" +
            "</div>" +
            "<button class='btn btn-success' type='submit'>Submit</button>" +
            "</form>" +
    "<a id='cancel'><button class='btn btn-warning'>Cancel</button></a>");
}

function cancelForm() {
    $("#personal")
        .empty()
        .append("<a id='update'>" +
                "<button class='btn btn-success'>" +
                "Edit personal data " +
                "</button>" +
                "</a> " +
                "<h4>Your username: <b id='username'>" + getCookie("username")+ "</b></h4> " +
                "<h4>Your email: <b id='email'>" + getCookie("email") + "</b></h4> " +
                "<h4>Your telephone number: <b id='phone'>" + getCookie("phone") + "</b></h4> " +
                "<div id='first_name'>" +
                "<h4>Your first name: <b id='fn'>" + getCookie("firstName") + "</b></h4>" +
                "</div> " +
                "<div id='last_name'>" +
                "<h4>Your last name: <b id='ln'>" + getCookie("lastName") + "</b></h4> " +
                "</div>" +
                "<div id='address'>" +
            "<h4>Your address: <b id='ar'>" + getCookie("address") + "</b></h4> " +
            "</div>");
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

