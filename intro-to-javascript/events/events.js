let button = document.querySelector('#btn1');
let greeting = document.querySelector('#greeting');
let input = document.querySelector('#name-input');

button.addEventListener('click', () => {
    greeting.textContent = "Hello " + input.value + "How are you doing today";
})

input.addEventListener('input', () => {
    let inputValue;
    console.log("Input field changed. New value: " + input.value);
});