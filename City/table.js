function writeTable(col) {
    $.ajax({
        url: 'maindata.csv',
        dataType: 'text',
        success: function (data) {
            var allRows = data.split(/\r?\n|\r/);
            var table =
                ' <table class="left_contents" id="btlist1" border="1"  frame=void style=" margin-top:40px; border-collapse: collapse;text-align:center;font-size:0.9em;font-weight:bold;background-color:#E4E4E4;width:400px">';
            var singleRow = 3;

            table += '<tr>';

            var rowCells = allRows[singleRow].split(',');
            var names = ['누적 확진', '신규 확진', '치료중', '사망']
            for (var rowCell = 0; rowCell < rowCells.length; rowCell++) {
                table += '<td style ="height:50px;color:black">';
                // table += rowCells[rowCell];
                table += names[rowCell];
                table += '</td>';
                table += '<td style ="height:80px; font-size:1.5em; color:red;">';
                table += rowCells[rowCell];
                table += '</td>';
            }
            table += '</tr>';
            table += '</table>';
            $('#count').append(table);
        }
    })
}