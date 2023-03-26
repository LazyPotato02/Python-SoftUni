function solve() {
    const busContainer = document.querySelector('#info > span')
    const departButton = document.getElementById('depart')
    const arriveButton = document.getElementById('arrive')
    const BASE_URL = 'http://localhost:3030/jsonstore/bus/schedule/'
    let nextStopId = 'depot'
    let stopName = null

    function depart() {
        arriveButton.disabled = false
        departButton.disabled = true


        fetch(`${BASE_URL}${nextStopId}`)

            .then((nextStopInfo) => {
                const {name, next} = nextStopInfo
                console.log(nextStopInfo)
                busContainer.textContent = `Next stop ${name}`

                nextStopId = next
                stopName = name
            })
            .catch(() => {
                busContainer.textContent = 'Error'
                arriveButton.disabled = true
                departButton.disabled = true
            })
    }

    async function arrive() {
        arriveButton.disabled = true
        departButton.disabled = false
        busContainer.textContent = `Arriving at ${stopName}`
    }

    return {
        depart,
        arrive
    };
}

let result = solve();