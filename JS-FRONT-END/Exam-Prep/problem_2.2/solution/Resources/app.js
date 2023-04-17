window.addEventListener('load', solve);

function solve() {

    let totalLIkesCount = 0 

    const inputFields = {
        'genre': document.getElementById('genre'),
        'songName': document.getElementById('name'),
        'authorName': document.getElementById('author'),
        'dateOfCreation': document.getElementById('date'),
    }
    // const genre = document.getElementById('genre')
    // const songName = document.getElementById('name')
    // const authorName = document.getElementById('author')
    // const dateOfCreation = document.getElementById('date')


    const addBtn = document.getElementById('add-btn')

    // const songCollection = document.getElementsByClassName('all-hits-container')
    const songCollection = document.querySelector('.all-hits-container')
    const savedSongs = document.querySelector('.saved-container')
    const totalLikes = document.querySelector('.likes > p')

    addBtn.addEventListener('click', addSongHandler)

    function addSongHandler(event) {
        event.preventDefault()

        let allInputsAreNonEmpty = Object.values(inputFields)
            .every((input) => input.value !== '');

        if (!allInputsAreNonEmpty) {
            console.log("HAS INVALID");
            return;
        }
        // console.log(totalLikes)
        const hitInfoElement = createElement('div',songCollection,null,['hits-info'])
        createElement('img',hitInfoElement,null,null,null,{ src: './static/img/img.png' })
        createElement('h2',hitInfoElement,`Genre: ${inputFields['genre'].value}`)
        createElement('h2',hitInfoElement,`Name: ${inputFields['songName'].value}`)
        createElement('h2',hitInfoElement,`Author: ${inputFields['authorName'].value}`)
        createElement('h3',hitInfoElement,`Date: ${inputFields['dateOfCreation'].value}`)
        
        const saveSongBtn = createElement('button',hitInfoElement,'Save song',['save-btn'])
        const likeSongBtn = createElement('button',hitInfoElement,'Like song',['like-btn'])
        const deleteSongBtn = createElement('button',hitInfoElement,'Delete',['delete-btn'])

        saveSongBtn.addEventListener('click',saveSongHandler)
        likeSongBtn.addEventListener('click',likeSongHandler)
        deleteSongBtn.addEventListener('click',deleteSongHandler)


        document.querySelector('form').reset();

    }

    function saveSongHandler(){
        songRefference = this.parentNode
        saveBtn = songRefference.querySelector('.save-btn')
        likeBtn = songRefference.querySelector('.like-btn')
        
        savedSongs.appendChild(songRefference)
        saveBtn.remove()
        likeBtn.remove()

    }
    function likeSongHandler(){
        this.setAttribute('disabled', true);
        totalLIkesCount++
        totalLikes.textContent = `Total Likes: ${totalLIkesCount}`

    }
    function deleteSongHandler(){
        this.parentNode.remove()

    }




    function createElement(type, parentNode, content, classes, id, attributes, useInnerHtml) {
        const htmlElement = document.createElement(type);

        if (content && useInnerHtml) {
            htmlElement.innerHTML = content;
        } else {
            if (content && type !== 'input') {
                htmlElement.textContent = content;
            }

            if (content && type === 'input') {
                htmlElement.value = content;
            }
        }

        if (classes && classes.length > 0) {
            htmlElement.classList.add(...classes);
        }

        if (id) {
            htmlElement.id = id;
        }

        // { src: 'link', href: 'http' }
        if (attributes) {
            for (const key in attributes) {
                htmlElement.setAttribute(key, attributes[key])
            }
        }

        if (parentNode) {
            parentNode.appendChild(htmlElement);
        }

        return htmlElement;
    }

}

