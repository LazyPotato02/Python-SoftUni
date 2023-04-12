window.addEventListener('load', solve);

function solve() {
    
    let taskstate = {
        title: null,
        description:null,
        label:null,
        estpoints:null,
        assignee:null
    }
    // TODO:
    let createTaskBtn = document.getElementById('create-task-btn')
    let tastkIdCounter = 1
    createTaskBtn.addEventListener('click',addTaskHandler)
    const inputDOMSelectors = {
        title: document.getElementById('title'),
        description: document.getElementById('description'),
        label: document.getElementById('label'),
        estpoints: document.getElementById('points'),
        assignee: document.getElementById('assignee'),
    };


    function addTaskHandler(event){
        event.preventDefault()

        let allInputsAreNonEmpty = Object.values(inputDOMSelectors)
        .every((input) => input.value !== '');


        const colors = {
            'Feature': 'feature',
            'Low Priority Bug': 'low-priority',
            'High Priority Bug': 'high-priority',
        }
        const icons = {
            'Feature': `&#8865`,
            'Low Priority Bug': `&#9737`,
            'High Priority Bug': `&#9888`,
        }
        // if (!allInputsAreNonEmpty) {
        //     console.log("HAS INVALID");
        //     return;
        // }
        if(allInputsAreNonEmpty){
            const taskSection = document.getElementById('tasks-section')
            const taskid = `task-${tastkIdCounter}`
            const article = createElement('article',taskSection,null,['task-card'],taskid,null,null)
            const changecolor = inputDOMSelectors.label.value
            let divelement = createElement('div',article,inputDOMSelectors.label.value,['task-card-label',colors[changecolor]],null)
            const span = document.createElement('span')
            span.innerHTML = icons[changecolor]
            divelement.appendChild(span)
            createElement('h3',article,inputDOMSelectors.title.value,['task-card-title'])
            createElement('p',article,inputDOMSelectors.description.value,['task-card-desctription'])
            createElement('div',article,inputDOMSelectors.estpoints.value,['task-card-points'])
            createElement('div',article,inputDOMSelectors.assignee.value,['task-card-assignee'])
            const deletebtndiv = createElement('div',article,null,['task-card-actions'])
            let deleteBtn = createElement('button',deletebtndiv,'Delete')
            deleteBtn.addEventListener('click',deleteTaskHandler)

            document.querySelector('form').reset();
            for (const key in inputDOMSelectors) {
                taskstate[key] = inputDOMSelectors[key].value;
            }
        }
        tastkIdCounter++
        
    }


    function deleteSongHandler() {
        // event.currentTarget = this
        this.parentNode.remove();
    }


    function deleteTaskHandler(){
        for (const key in inputDOMSelectors) {
            inputDOMSelectors[key].value = taskstate[key];
        }
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