function writeStep(data) {
    var s = ['', '', '', '', '']
    s[data] = 'style="background-color:red"';
    $('#step').append(
        `
        <table id="distance">
            <caption>거리두기</caption>

            <tbody>
                <tr>
                    <td ${s[0]}>1</td>
                    <td ${s[1]}>1.5</td>
                    <td ${s[2]}>2</td>
                    <td ${s[3]}>2.5</td>
                    <td ${s[4]}>3</td>
                </tr>
            </tbody>
        </table>`
    );
}