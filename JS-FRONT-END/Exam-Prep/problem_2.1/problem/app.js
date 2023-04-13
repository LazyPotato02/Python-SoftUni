window.addEventListener("load", solve);

function solve() {
  //TODO ....

  let scaryStory = [{
    firstName: '',
    lastName: '',
    age: '',
    storyTitle: '',
    genre: '',
    story: '',
  }]
  const main = document.getElementById('main')
  const firstName = document.getElementById('first-name')
  const lastName = document.getElementById('last-name')
  const age = document.getElementById('age')
  const storyTitle = document.getElementById('story-title')
  const genre = document.getElementById('genre')
  const story = document.getElementById('story')

  const publishButton = document.getElementById('form-btn')

  const ulList = document.getElementById('preview-list')

  publishButton.addEventListener('click', publish)

  function publish() {
    scaryStory['firstName'] = firstName.value
    scaryStory['lastName'] = lastName.value
    scaryStory['age'] = age.value
    scaryStory['storyTitle'] = storyTitle.value
    scaryStory['genre'] = genre.value
    scaryStory['story'] = story.value

    let allInputsAreNonEmpty = Object.values(scaryStory)
        .every((input) => input !== '');

    if (!allInputsAreNonEmpty) {
      console.log("HAS INVALID");
      return;
    }
    
    const li = createElement('li',ulList,null,['story-info'])
    const article = createElement('article',li)
    createElement('h4',article,`Name: ${scaryStory['firstName']} ${scaryStory['lastName']}`)
    createElement('p',article,`Age: ${scaryStory['age']}`)
    createElement('p',article,`Title: ${scaryStory['storyTitle']}`)
    createElement('p',article,`Genre: ${scaryStory['genre']}`)
    createElement('p',article,`${scaryStory['story']}`)
    
    // Buttons
    const saveBtn = createElement('button',li,'Save Story',['save-btn'])
    const editBtn = createElement('button',li, 'Edit Story',['edit-btn'])
    const deleteBtn = createElement('button',li, 'Delete Story',['delete-btn'])

    saveBtn.addEventListener('click',addHandler)
    editBtn.addEventListener('click',editHandler)
    deleteBtn.addEventListener('click',deletHandler)

    publishButton.setAttribute('disabled',true)

    firstName.value = ''
    lastName.value = ''
    age.value = ''
    storyTitle.value = ''
    genre.value = ''
    story.value = ''
  }


  function addHandler(){
    main.innerHTML = ''
    createElement('h1',main,'Your scary story is saved!')


  }
  function editHandler(){
    firstName.value = scaryStory['firstName']
    lastName.value = scaryStory['lastName']
    age.value = scaryStory['age']
    storyTitle.value = scaryStory['storyTitle']
    genre.value = scaryStory['genre']
    story.value = scaryStory['story']

    ulList.removeChild(ulList.childNodes[3])
 
    publishButton.removeAttribute('disabled')
  }
  function deletHandler(){
    ulList.removeChild(ulList.childNodes[3])
 
    publishButton.removeAttribute('disabled')
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
