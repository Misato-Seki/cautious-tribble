const { addImportantTask, getTaskList, clearTasks } = require("../script");

describe('addImportantTask', () => {
    beforeEach(() => {
        document.body.innerHTML = `<input id="importantTaskInput" type="text"><ul id="taskList"></ul>`;
        clearTasks(); // Clear taskList before each test
    });

    test('An alert will appear with an empty task entry', () => {
        const taskInput = document.getElementById('importantTaskInput');
        taskInput.value = ''; // Set empty input

        // Set up mock alerts
        global.alert = jest.fn();

        addImportantTask();

        expect(global.alert).toHaveBeenCalledWith('Please enter a task.');
    });

    // test('Task is successfully added', () => {
    //     const taskInput = document.getElementById('importantTaskInput');
    //     taskInput.value = 'Test Task';

    //     addImportantTask();

    //     const taskList = getTaskList(); // Use the exported function to get the taskList
    //     expect(taskList.length).toBe(1); // Is one task added?
    //     expect(taskList[0].text).toBe('Test Task');
    // });

    // test('Duplicate tasks are not added', () => {
    //     const taskInput = document.getElementById('importantTaskInput');
    //     taskInput.value = 'Duplicate Task';
    //     addImportantTask(); // Initial addition
    //     addImportantTask(); // re-add

    //     const taskList = getTaskList(); // Use the exported function to get the taskList
    //     expect(taskList.length).toBe(1); // Duplicate tasks are not added.
    // });
});
