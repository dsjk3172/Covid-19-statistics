function writeTable(col, loc = 0) {
    if (col == "maindata") { //확진자 현황 출력
        $.ajax({
            url: col + '.csv',
            dataType: 'text',
            success: function (data) {
                var color_list = ['#cc0000', '#E54C4C', '#74C600', 'black']
                var allRows = data.split(/\r?\n|\r/);

                var table ='<table class="data_list"><tr style="color:white;">';

                var rowCells = allRows[loc].split(',');
                var names = ['누적 확진', '신규 확진', '치료중', '사망']

                for(var i = 0; i < rowCells.length; i++) //누적 확진, 신규 확진, 치료중, 사망
                    table += `<td style="background-color: ${color_list[i]}";>${names[i]}</td>`;

                table += '</tr><tr style="font-size:x-large">';

                for(var i = 0; i < rowCells.length; i++) //데이터
                    table += `<td style="background-color: bisque;">${rowCells[i]}</td>`;

                table += '</tr>';
                $('#count').append(table);
            }
        })
    }
    else { //선별진료소 현황 출력
        var url_ = col + 'Clinics.csv'

        $.ajax({
            url: url_,
            dataType: 'text',
            success: function (data) {
                var allRows = data.split(/\r?\n|\r/);
                var table ='<table border="1" frame=void style="border-collapse: collapse;text-align:center;font-size:1.2em;background-color:#E4E4E4;width:100%">';
                    table += '<tr>';
                    var rowCells = allRows[0].split(',');
                    for (var rowCell = 0; rowCell < rowCells.length; rowCell++)
                        table += `<td style ="height:50px; font-size:1.1em; font-weight:bold; background-color:darkgrey; color:black;">${rowCells[rowCell]}</td>`;
                    table += '</tr>';
                for(var i = 1; i < allRows.length; i++) {
                    table += '<tr>';
                    var rowCells = allRows[i].split(',');
                    for (var rowCell = 0; rowCell < rowCells.length; rowCell++)
                        table += `<td style ="height:50px; font-size:1em; color:black;">${rowCells[rowCell]}</td>`;
                    table += '</tr>';
                }
                table += '</table>';
                $('#clinics').append(table);
            }
        })

    }
}