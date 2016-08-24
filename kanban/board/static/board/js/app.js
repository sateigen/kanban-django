$.ajax({
  url: '/api/board'
}).done(function(response) {
  if (response.length > 0) {
    response.forEach(function(result) {
      console.log(result);
      $('#here_table').append('<table></table>')
      // make a table for each ticket
      var table = $('#here_table').children();
      table.append('<tr><td>a</td><td>b</td></tr>');
    })
  }
});



//
// <table id="abilities">
//       <thead>
//         <tr>
//           <th>
//             name
//           </th>
//           <th>
//             description
//           </th>
//           <th>
//             power level
//           </th>
//         </tr>
//       </thead>
//     </table>
