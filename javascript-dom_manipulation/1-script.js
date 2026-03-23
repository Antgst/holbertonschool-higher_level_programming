const RedHeader = document.querySelector('#red_header');
const header = document.querySelector('header');

RedHeader.addEventListener('click', function () {
  header.style.color = "#FF0000";
});

/*
document.querySelector('#red_header').addEventListener('click', function () {
  document.querySelector('header').style.color = '#FF0000';
});
*/