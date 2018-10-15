/**
 * Cortar un string a length caracteres.
 */
function truncateText(text, length) {
  if (text) {
    const dots = text.length >= length ? '...' : ''
    return text.substring(0, length) + dots
  }
  return ''
}

/**
 * Remplaza \n por <br>.
 */
function lineBreakBr(text) {
  return text.replace(/\n/g, '<br>')
}
