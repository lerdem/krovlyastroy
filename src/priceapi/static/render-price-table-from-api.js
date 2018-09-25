function getAndRenderTable(url) {

  var jqxhr = $.get(url, function () {
    console.log('start fetch data')
  })
    .done(function (data) {
        renderTable(data)
    })
    .fail(function (data) {
        console.log(data);
    })
    .always(function () {
        console.log('finished');
    });

  function renderTable(data) {

    var tableMask = `
      <table class="table table-bordered table-responsive-sm table-js" style="display: none">
        <caption>Цены на профнастил (от ${formatDate(new Date())})</caption>
        <thead>
        <tr>
          <th scope="col" rowspan="2">Наименование</th>
          <th scope="col" rowspan="2">Толщина</th>
          <th scope="col" rowspan="2">Покрытие</th>
          <th scope="col"colspan="3">Цена грн/м2</th>
        </tr>
        <tr>
          <td>до 50</td>
          <td>50-100</td>
          <td>100+</td>
        </tr>
        </thead>
        <tbody>
        </tbody>
      </table>`;
    $('.nav').append(tableMask);
    $('head').append(
      '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">'
    );

    var style = 'vertical-align: top;';
    var i, j, name, products, productsRow, row;

    // $('.table-js').ready(function () {

    for (i = 0; i < data.length; i++) {
      name = data[i].name;
      products = data[i].product_set;
      row = `<tr>
               <td rowspan="${products.length}">${name}
             </td>`;
      for (j = 0; j < products.length; j++) {
        productsRow = products[j];
        row += `<td>${productsRow.height}</td>
          <td>${productsRow.surface}</td>
          <td>${productsRow.price["50"]}</td>
          <td>${productsRow.price["100"]}</td>
          <td>${productsRow.price["1000"]}</td>
          </tr>`;
        console.log(row);
        $('.table-js > tbody').append(row);
        row = '<tr>'
      }
      row = ''
    }
    $('.table-js').removeAttr('style')
  }

}
