const input_fields = document.getElementsByTagName('input');
const select_fields = document.querySelectorAll('select');

const array_of_input_fields = Array.from(input_fields);
array_of_input_fields.forEach((input_field) => {
input_field.addEventListener('change', () => {
document.querySelector('form').submit();
});
});

const array_of_select_fields = Array.from(select_fields);
array_of_select_fields.forEach((select_field) => {
select_field.addEventListener('change', () => {
document.querySelector('form').submit();
});
});