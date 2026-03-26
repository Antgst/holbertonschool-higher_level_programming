const item = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

item.addEventListener('click', function () {
  const li = document.createElement('li');
  li.textContent = 'Item';
  list.append(li);
});
