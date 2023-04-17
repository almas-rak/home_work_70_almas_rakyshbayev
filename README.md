# home_work_70_almas_rakyshbayev

admin
login: root
password: root

Tasks 

List
method: GET
url:host/api/tasks/

    {
        "id": "id задачи",
        "summary": "название задачи",
        "status": {
            "id": id статуса,
            "name": "Название статуса"
        },
        "type": [  
            {
                "id": id типа,
                "name": "имя типа"
            }
        ],
        "project": {
            "id": id проекта,
            "name": "Название проекта"
        },
        "created_at": "Дата и время создания задачи(ставится автоматически при создании задачи)",
        "updated_at": "Дата и время обнавления задачи(ставится автоматически при изменении задачи)"
    },
    
Detail
method: GET
url:host/api/tasks/<id задачи>/

{
    "id": 5,
    "summary": "task_4",
    "status": {
        "id": 1,
        "name": "Новая"
    },
    "type": [
        {
            "id": 1,
            "name": "Задача"
        }
    ],
    "description": "task_5",
    "project": {
        "id": 1,
        "name": "HW_59"
    },
    "created_at": "2023-03-09T22:16:17.867000+06:00",
    "updated_at": "2023-03-09T22:16:31.911000+06:00"
}





























