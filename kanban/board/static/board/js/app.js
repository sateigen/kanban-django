$.ajax({
  url: '/api/board'
}).done(function(response) {
  if (response.length > 0) {
    response.forEach(function(result) {
      console.log(result);
      $('<table>').appendTo('#here_table')
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
