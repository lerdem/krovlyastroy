var hostApi = 'https://krovlyastroy.pythonanywhere.com/';
(function getShemaOrg() {
  var jqxhr = $.get(`${hostApi}api/common-info/schema_org/`, function () {
  console.log('start fetch data')
})
  .done(function (data) {
      appendShemaOrgJson(data)
  })
  .fail(function (data) {
      console.log(data);
  })
  .always(function () {
      console.log('finished');
  });
})();

(function getTable() {
  var jqxhr = $.get(`${hostApi}api/common-info/`, function () {
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
})();

function renderTable(data) {

  var tableMask = `
    <table class="table table-bordered table-responsive-sm table-js" style="display: none">
      <caption>Цены на профнастил (на ${formatDate(new Date())})</caption>
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
        <td>>100</td>
      </tr>
      </thead>
      <tbody>
      </tbody>
    </table>`;
  // TODO add custom place apending, for now hardcode
  $('h1').append(tableMask);
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
      $('.table-js > tbody').append(row);
      row = '<tr>'
    }
    row = ''
  }
  $('.table-js').removeAttr('style')
}

// usage formatDate(new Date())
function formatDate(date) {
  var monthNames = [
    "января",
    "февраля",
    "марта",
    "апреля",
    "мая",
    "июня",
    "июля",
    "августа",
    "сентября",
    "октября",
    "ноября",
    "декабря"
  ];

  var day = date.getDate();
  var monthIndex = date.getMonth();
  var year = date.getFullYear();

  return day + ' ' + monthNames[monthIndex] + ' ' + year;
}

function appendShemaOrgJson(data) {
  var script = document.createElement("script");
  script.type = "application/ld+json";
  script.text = JSON.stringify(data);
  document.head.appendChild(script);
}
