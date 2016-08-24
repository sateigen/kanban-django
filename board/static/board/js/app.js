var foo = $('.here_table').attr('id')

$.ajax({
  url: '/api/board/' + foo
}).done(function(response) {
  console.log(response.ticket_set)
  response.ticket_set.forEach(function(result) {
    console.log(result);
    var table = $('<table></table>');
    table.append('<thead><tr><th>'+result.name+'</th></tr></thead>')
    result.task_set.forEach(function(taskInfo) {
      table.append('<tr><td>' + taskInfo.description + '<br />Points: ' + taskInfo.points +'</td></tr>');
    })
    table.appendTo('.here_table');
  })
});