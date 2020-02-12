$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-user .modal-content").html("");
      },
      success: function (data) {
        $("#modal-user .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#user-table tbody").html(data.html_user_list);
          $("#modal-user").modal("hide");
        }
        else {
          $("#modal-user .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Update user
  $("#user-table").on("click", ".js-update-user", loadForm);
  $("#modal-user").on("submit", ".js-user-update-form", saveForm);

});
