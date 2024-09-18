const textarea = document.querySelector("textarea");
const count = document.querySelector(".count");

function contarletras() {

  const textoLength = textarea.value.length;

  count.innerHTML = `${textoLength}`
}