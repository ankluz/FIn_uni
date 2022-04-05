pole = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
];
turns = 0

function pressed(id) {
    self = document.getElementById(id)

    if (turns % 2 == 0) {
        key = 'X'

    } else {
        key = 'O'
    }

    pole[Number(id)] = key
    self.innerHTML = key
    self.disabled = true
    turns++

    if ((pole[0] == pole[1] && pole[1] == pole[2]) || (pole[3] == pole[4] && pole[4] == pole[5]) || (pole[6] == pole[7] && pole[7] == pole[8]) ||
        (pole[0] == pole[3] && pole[3] == pole[6]) || (pole[1] == pole[4] && pole[4] == pole[7]) || (pole[2] == pole[5] && pole[5] == pole[8]) ||
        (pole[0] == pole[4] && pole[4] == pole[8]) || (pole[2] == pole[4] && pole[4] == pole[6])) {

        alert(`Победитель - уважаемыые ${key}`)
        location.reload();
    } else if (turns >= 9) {
        alert('Ничья!')
    }
}