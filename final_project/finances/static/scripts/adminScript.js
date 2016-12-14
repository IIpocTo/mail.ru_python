$(document).ready(function () {

    $('.alert').fadeOut(4000);

    $(document).on("click", '.edit', {}, function() {
        var rawId = $(this).attr('id');
        var id = rawId.substring(4);
        editUser(id);
    });

    $(document).on("click", '.delete', {}, function() {
        var rawId = $(this).attr('id');
        var id = rawId.substring(6);
        deleteUser(id);
    });

    $(document).on("click", "#sendEdit", function() {
        try {
            $("#editForm").submit();
        } catch (e) {
            console.log(e);
        }
    });

    $(document).on("click", "#sendDelete", function () {
        try {
            $("#deleteForm").submit();
        } catch (e) {
            console.log(e);
        }
    })

});

var dictionary = {'username': null, 'email': null, 'first_name': null, 'last_name': null, 'phone': null, 'address': null, 'last_login': null}

function deleteUser(data) {
    document.getElementById('deleteForm').getElementsByTagName('input').item(0).attributes.getNamedItem('value').nodeValue = data;
    $("#deleteUser").modal('show');
}

function editUser(data) {
    var tr = $("#" + data);
    for (var key in dictionary) dictionary[key] = tr.children().filter(function (j, elem) {
        return elem.className == key;
    })[0].innerText;
    console.log(dictionary);
    for (key in dictionary) {
        if (key != "phone") {
            $("#id_" + key).val(dictionary[key]);
        } else {
            var gap = dictionary["phone"].indexOf(' ');
            var firstPhone = dictionary['phone'].substring(0, gap);
            var secondPhone = dictionary['phone'].substring(gap + 1);
            console.log(firstPhone, secondPhone);
            $("#id_phone_0").val(firstPhone);
            $("#id_phone_1").val(secondPhone);
        }
    }
    $("#username").text(dictionary["username"]);
    $("#editUser").modal('show');
}

