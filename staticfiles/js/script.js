document.getElementById("copyButton").addEventListener("click", function() {
    var textarea = document.createElement('textarea')
    textarea.id = 'temp_element'
    textarea.style.height = 0
    document.body.appendChild(textarea)
    textarea.value = document.getElementById('emailToCopy').innerText
    var selector = document.querySelector('#temp_element')
    selector.select()
    document.execCommand('copy')
    document.body.removeChild(document.getElementById('temp_element'))
    alert("Email copied to clipboard!")
})