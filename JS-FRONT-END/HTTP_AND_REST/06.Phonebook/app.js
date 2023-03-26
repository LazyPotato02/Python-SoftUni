function attachEvents() {
    const phonebookContainer = document.getElementById('phonebook')
    const personInput = document.getElementById('person')
    const phoneInput = document.getElementById('phone')
    const loadBtn = document.getElementById('btnLoad')
    const createBtn = document.getElementById('btnCreate')
    const BASE_URL = 'http://localhost:3030/jsonstore/phonebook/'

    loadBtn.addEventListener('click', loadPhoneBookHandler)
    createBtn.addEventListener('click', createPhoneBookHandler)

    async function loadPhoneBookHandler() {
        try {
            const phoneBookResponse = await fetch(BASE_URL)
            let phoneBookData = await phoneBookResponse.json()
            phoneBookData = Object.values(phoneBookData)
            phonebookContainer.innerHTML = ''
            for (const {phone, person, _id} of phoneBookData) {
                const li = document.createElement('li')
                const btn = document.createElement('button')
                btn.textContent = 'Delete'
                btn.id = _id
                btn.addEventListener('click', deletePhoneBookHandler)
                li.innerHTML = `${person}: ${phone}`
                li.appendChild(btn)
                phonebookContainer.appendChild(li)

            }
        } catch (err) {
            console.log(err)
        }
    }

    function createPhoneBookHandler() {
        const person = personInput.value
        const phone = phoneInput.value
        const httpHeaders = {
            method: 'POST',
            body: JSON.stringify({person, phone})
        }
        console.log(person)
        console.log(phone)
        fetch(BASE_URL, httpHeaders)
            .then((res) => res.json())
            .then(() => {
                loadPhoneBookHandler();
                personInput.value = ''
                phoneInput.value = ''
            })
            .catch((err) => {
                console.log(err)
            })
    }

    async function deletePhoneBookHandler() {
        const id = this.id
        const httpHeaders = {
            method: 'DELETE'
        }

        fetch(`${BASE_URL}${id}`, httpHeaders)
            .then((res) => res.json())
            .then(loadPhoneBookHandler)
            .catch((err) =>{
                console.log(err)
            })
    }

}

attachEvents();