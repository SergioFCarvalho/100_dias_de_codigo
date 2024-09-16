let box = document.querySelector('.box');
let input1 = document.querySelector('.in1');
let input2 = document.querySelector('.in2');

input1.addEventListener('input', () => {
  box.style.borderRadius = input1.value;
})
input2.addEventListener('input', () => {
  box.style.backgroundColor = input2.value;
})