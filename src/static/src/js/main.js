/* globals axios, Cookies */

$(document).ready(function () {
  /**
   * Muestra el nombre del archivo en input.custom-file
   */
  $('.custom-file-input').on('change', function () {
    let fileName = $(this).val().split('\\').pop()
    $(this).next('.custom-file-label').addClass('selected').html(fileName)
  })
})
