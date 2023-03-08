
const textInput = document.getElementById('textInput')
const result = document.getElementById('result')
function changeString(){
    let text = textInput.value
    
    result.innerHTML = `${handleString(text)}`
    
}

function handleString(text){
    let newText = []
    text = text.split("")
    const count = text.length
    for(let x = count; x >= 0; x-- ){
        newText.push(text[x])
    }
    text = newText
    text = text.join("")
    return text
}