// TODO
function attachEvents() {

    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/'


    const inputValue = document.getElementById('title')

    const loadBtn = document.getElementById('load-button')
    const addBtn = document.getElementById('add-button')
    const todoList = document.getElementById('todo-list')

    loadBtn.addEventListener('click', loadBtnHandler)
    addBtn.addEventListener('click', addTaskHandler)
    async function loadBtnHandler(event) {
        if (event) {
            event.preventDefault()

        }
        todoList.innerHTML = ''

        try {

            const tasks = await fetch(BASE_URL)
            let response = await tasks.json()
            response = Object.values(response)

            for (const { name, _id } of response) {
                liElement = createElement('li', todoList)
                createElement('span', liElement, `${name}`)

                const removeBtn = createElement('button', liElement, 'Remove')
                const editBtn = createElement('button', liElement, 'Edit')

                liElement.id = _id

                removeBtn.addEventListener('click', removeBtnHandler)
                editBtn.addEventListener('click', loadEditFormHandler)



            }


        } catch (err) {
            console.log(err)
        }

    }


    async function addTaskHandler(event) {
        event.preventDefault()
        let name = inputValue.value
        if( name === ''){
            return
        }

        const httpHeaders = {
            method: 'POST',
            body: JSON.stringify({ name })
        }

        try {
            const awaitResponse = await fetch(BASE_URL, httpHeaders)


        } catch (error) {
            console.log(error)
        }
    }


    function removeBtnHandler() {
        const id = this.parentNode.id
        const httpHeaders = {
            method: 'DELETE',
        }
        fetch(BASE_URL + id, httpHeaders)
        todoList.innerHTML = ''
        loadBtnHandler()
    }

    function loadEditFormHandler(event){
        const liParent = event.currentTarget.parentNode
        const [span, _removeBtn, editBtn] = Array.from(liParent.children)
        const editInput = document.createElement('input')
        editInput.value = span.textContent
        liParent.prepend(editInput)
        const submitBtn = document.createElement('button')
        submitBtn.textContent = 'Submit'
        submitBtn.addEventListener("click", submitTaskHandler)
        liParent.appendChild(submitBtn)
        span.remove()
        editBtn.remove()
    }

    function submitTaskHandler(event) {
        const liParent = event.currentTarget.parentNode
        const id = event.currentTarget.parentNode.id
        const [input] = Array.from(liParent.children)
        const httpHeaders = {
            method: 'PATCH',
            body: JSON.stringify({ name: input.value })
        }

        fetch(`${BASE_URL}${id}`, httpHeaders)
            .then(() => loadBtnHandler())
            .catch((err) => {
                console.error(err)
            })

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

attachEvents();
