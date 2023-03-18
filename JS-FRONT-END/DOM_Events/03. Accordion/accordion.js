function toggle() {
    const mainElement = document.getElementById('accordion')
    const titleText = mainElement.children[0]
    const extraText = mainElement.children[1]

    if (extraText.style.display === 'none') {
        titleText.children[0].textContent = 'Less'
        extraText.style.display = 'block'
    }else{
        titleText.children[0].textContent = 'More'
        extraText.style.display = 'none'
    }
}