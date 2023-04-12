function solve(input) {
    // sprint board template "{assignee}:{taskId}:{title}:{status}:{estimatedPoints}"
    let iterations = Number(input.shift())
    let sprint = {}

    let commandParser = {
        'Add New': addNew,
        'Change Status': changeStatus,
        'Remove Task': removeTask
    }

    for (let i = 0; i < iterations; i++) {
        let task = input.shift().split(':')
        let personName = task[0]
        let taskId = task[1]
        let taskTitle = task[2]
        let taskStatus = task[3]
        let taskPoints = task[4]
        sprint[taskId] = {personName, taskTitle, taskStatus, taskPoints}

    }

    while (input.length > 0) {
        let row = input.shift().split(':')
        let command = row.shift()
        commandParser[command](...row)

    }

    function addNew(...row) {
        let personalName = row[0]
        let taskId = row[1]
        let taskTitle = row[2]
        let taskStatus = row[3]
        let taskPoints = row[4]
        let nameList = []
        for (const sprintKey in sprint) {
            nameList.push(sprint[sprintKey].personName)
        }
        if (nameList.includes(personalName)) {
            sprint[taskId] = {personalName, taskTitle, taskStatus, taskPoints}
        } else {
            console.log(`Assignee ${personalName} does not exist on the board!`)
        }
    }


    function changeStatus(...input) {
        let personalName = input[0]
        let taskId = input[1]
        let status = input[2]
        let isTaskId = false
        let isAssignee = false
        for (const sprintKey in sprint) {
            if (sprintKey === taskId) {
                sprint[taskId].taskStatus = status
                isTaskId = true

            } else {
                isTaskId = false
            }
            if (sprint[sprintKey].personName === personalName) {
                isAssignee = true
                break
            } else {
                isAssignee = false
            }
        }
        if (isAssignee === false) {
            console.log(`Assignee ${personalName} does not exist on the board!`)

        } else if (isTaskId === false) {
            console.log(`Task with ID ${taskId} does not exist for ${personalName}!`)

        }

    }


    function removeTask(...input) {
        let assignee = input[0]
        let ids = Number(input[1])
        let assigneeTask = {}
        let taskIds = []
        let isAssignee = true
        for (const sprintKey in sprint) {

            if (sprint[sprintKey].personName === assignee) {
                assigneeTask[sprintKey] = sprint[sprintKey]
            }


        }
        let taskCount = 0
        for (const assigneeTaskElement in assigneeTask) {
            taskCount++
        }
        if (taskCount === 0) {
            console.log(`Assignee ${assignee} does not exist on the board!`)
        }

        for (const assigneeTaskElement in assigneeTask) {
            taskIds.push(assigneeTaskElement)
        }

        if (taskCount > 0) {
            if (ids < 0 || ids >= taskIds.length) {
                console.log("Index is out of range!")
            } else {
                let taskToDelete = taskIds[ids]
                delete sprint[taskToDelete]
            }
        }

    }

    let todoPoints = 0
    let inProgressPoints = 0
    let CodeReview = 0
    let donePoints = 0


    for (const sprintElement in sprint) {
        if (sprint[sprintElement].taskStatus === 'ToDo') {
            todoPoints += Number(sprint[sprintElement].taskPoints)
        } else if (sprint[sprintElement].taskStatus === 'In Progress') {
            inProgressPoints += Number(sprint[sprintElement].taskPoints)
        } else if (sprint[sprintElement].taskStatus === 'Code Review') {
            CodeReview += Number(sprint[sprintElement].taskPoints)
        } else if (sprint[sprintElement].taskStatus === 'Done') {
            donePoints += Number(sprint[sprintElement].taskPoints)
        }

    }
    console.log(`ToDo: ${todoPoints}pts`)
    console.log(`In Progress: ${inProgressPoints}pts`)
    console.log(`Code Review: ${CodeReview}pts`)
    console.log(`Done Points: ${donePoints}pts`)
    let sumOfTasks = inProgressPoints + CodeReview + todoPoints
    if (donePoints >= sumOfTasks) {
        console.log('Sprint was successful!')
    } else {
        console.log('Sprint was unsuccessful...')
    }
}


solve([
    '4',
    'Kiril:BOP-1213:Fix Typo:Done:1',
    'Peter:BOP-1214:New Products Page:In Progress:2',
    'Mariya:BOP-1215:Setup Routing:ToDo:8',
    'Georgi:BOP-1216:Add Business Card:Code Review:3',
    'Add New:Sam:BOP-1237:Testing Home Page:Done:3',
    'Change Status:Georgi:BOP-1216:Done',
    'Change Status:Will:BOP-1212:In Progress',
    'Remove Task:Georgi:3',
    'Change Status:Mariya:BOP-1215:Done',
])