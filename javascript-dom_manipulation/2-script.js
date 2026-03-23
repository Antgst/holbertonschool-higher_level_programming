const RedHeader = document.querySelector('#red_header');
const header = document.querySelector('header');

RedHeader.addEventListener('click', function () {
  header.classList.add('red')
});
