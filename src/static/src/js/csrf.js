// csrf axios
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

// csrf Ajax.
const csrfToken = $('[name=csrfmiddlewaretoken]').val()

// TODO: Mejorar
$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    xhr.setRequestHeader('X-CSRFToken', Cookies.get('csrftoken'))
  }
})
