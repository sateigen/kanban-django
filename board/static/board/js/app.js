var board_id = $('.here_table').attr('id')

$.ajax({
  url: '/api/board/' + board_id
}).done(function(response) {
  console.log(response.ticket_set)
  response.ticket_set.forEach(function(result) {
    console.log(result);
    var table = $('<table></table>');
    var $tableHead = $('<thead><tr><th>').text(result.name)
    table.append($tableHead);

    $tableHead.click(function() {
      var ticketName = $tableHead.text()
      var ticketId = $tablehead
      $tableHead.empty()

      var $form = $('<form>').appendTo($tableHead)

      var $input = $('<input type="text">').val(ticketName)

      $input.click(function() {
        return false;
      })

      $input.appendTo($form)

      $form.submit(function() {
        var ticketName = $input.val()

        $.ajax({
          method: 'PUT',
          url: '/api/ticket/' + ticketId + '/',
          data: {
            name: ticketName,
            description: result.description,
          }
        })

        $tableHead.empty();
        $tableHead.text(ticketName)

        return false;
      })

    })

    if (result.description) {
      table.append('<tr><td><i>' + result.description + '</i></td></tr>');
    }
    result.task_set.forEach(function(taskInfo) {
      table.append('<tr><td>' + taskInfo.description + '<br />Points: ' + taskInfo.points +'</td></tr>');
    })
    table.appendTo('.here_table');
  })
});
