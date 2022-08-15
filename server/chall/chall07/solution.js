result = 'g0sye8dsletbfckasekip2j1sepcmeabetsiz5enaib2uwzu5y33lujndoat8meaolao1l38dmla34'
console.log(deshuffle(result.split('')).toString().replaceAll(',', ''))

function deshuffle(array) {
    rand = i(1883393164);

    shuffleIndexes = []

    for (index = array.length - 1; index > 0; index--) {
        j = Math.floor(rand() * (index + 1))
        shuffleIndexes.push(j)
    }

    for (index = 1; index < array.length; index++) {
        j = shuffleIndexes[shuffleIndexes.length - index]
        o = array[index]
        array[index] = array[j]
        array[j] = o;
    } return array;
}