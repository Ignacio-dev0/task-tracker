# Task Tracker

Build a CLI app to track your tasks and manage your to-do list.
Sample solution for the [task-tracker](https://roadmap.sh/projects/task-tracker) challenge from [roadmap.sh](https://roadmap.sh/).


## Overview

Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

## How to run

Clone the repository and run the following command:

```bash
git clone https://github.com/Ignacio-dev0/task-tracker.git
cd task-tracker
python app.py
```
```python
# To add a task
add "Buy drinks"

# To update a task
update 1 "Buy drinks and cook dinner"

# To delete a task
delete 1

# To mark a task as in progress/done/todo
mark-in-progress 1
mark-done 1
mark-todo 1

# To list all tasks
list
list done
list todo
list in-progress
```