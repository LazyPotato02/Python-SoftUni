function attachEvents() {
    document.getElementById('submit').addEventListener('click', sendButtonHandler)
    document.getElementById('refresh').addEventListener('click', getAllMessages)

    async function retrieveMessagesDataHandler(data) {
        const messageBox = document.getElementById('messages')
        const messageList = []


        messageBox.textContent = ''
        for (const dataKey in data) {
            const message = `${data[dataKey].author}: ${data[dataKey].content}`
            messageList.push(message)
        }
        messageBox.textContent = messageList.join('\n')


    }

    async function sendButtonHandler() {
        const authorName = document.getElementsByName('author')[0].value
        const messageContent = document.getElementsByName('content')[0].value

        const url = 'http://localhost:3030/jsonstore/messenger'
        const body = {
            author: authorName,
            content: messageContent
        }
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-type': 'application/json'
            },
            body: JSON.stringify(body)
        })

        getAllMessages()
        authorName.value = ''
        messageContent.value = ''

    }

    async function getAllMessages() {
        const url = 'http://localhost:3030/jsonstore/messenger'
        const response = await fetch(url)
        const data = await response.json()
        retrieveMessagesDataHandler(data)
    }
}

attachEvents();