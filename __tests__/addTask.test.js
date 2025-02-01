const { addTask, getTaskList, clearTasks } = require("../script");

describe('addTask', () => {
    beforeEach(() => {
        document.body.innerHTML = `<input id="taskInput" type="text"><ul id="taskList"></ul>`;
        clearTasks(); // Clear taskList before each test
    });

    test('An alert will appear with an empty task entry', () => {
        const taskInput = document.getElementById('taskInput');
        taskInput.value = ''; // Set empty input

        // Set up mock alerts
        global.alert = jest.fn();

        addTask();

        expect(global.alert).toHaveBeenCalledWith('Please enter a task.');
    });

    test('Task is successfully added', () => {
        const taskInput = document.getElementById('taskInput');
        taskInput.value = 'Test Task';

        addTask();

        const taskList = getTaskList(); // Use the exported function to get the taskList
        expect(taskList.length).toBe(1); // Is one task added?
        expect(taskList[0].text).toBe('Test Task');
    });

    test('Duplicate tasks are not added', () => {
        const taskInput = document.getElementById('taskInput');
        taskInput.value = 'Duplicate Task';
        addTask(); // Initial addition
        addTask(); // re-add

        const taskList = getTaskList(); // Use the exported function to get the taskList
        expect(taskList.length).toBe(1); // Duplicate tasks are not added.
    });
});
