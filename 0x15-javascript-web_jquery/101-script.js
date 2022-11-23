window.addEventListener('DOMContentLoaded', () => {
  $('DIV#add_item').click(() => {
    $('<li>Item</li>').appendTo('UL.my_list');
  });
  $('DIV#remove_item').click(() => {
    $('.my_list li').last().remove();
  });
  $('DIV#clear_list').click(() => {
    $('.my_list li').map(() => {
      this.remove();
    });
  });
});
