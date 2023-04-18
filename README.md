# home_work_70_almas_rakyshbayev

admin  
login: root  
password: root

Задачи

Список задач  
method: GET  
url: http://host/api/tasks/

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

Детали задачи  
method: GET  
url: http://host/api/tasks/<id задачи>/

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
        "description": "Описание Задачи",
        "project": {
            "id": id проекта,
            "name": "Название проекта"
        },
        "created_at": "Дата и время создания задачи(ставится автоматически при создании задачи)",
        "updated_at": "Дата и время обнавления задачи(ставится автоматически при изменении задачи)"
    }

Создание задачи  
method: POST  
url: http://host/api/tasks/  

    {
        "summary": "Обязательное поле. Строка. Максимум 100 символов",
        "status": Обязательное поле. Число. id статуса,
        "type": [Обязательное поле. Список. Число. id типа ],
        "description": "Строка.",
        "project": Обязательное поле. Число. id проекта
    }

Изменение задачи  
method: PUT  
url: http://host/api/tasks/<id задачи>/ 

    {
        "summary": "Обязательное поле. Строка. Максимум 100 символов",
        "status": Обязательное поле. Число. id статуса,
        "type": [Обязательное поле. Список. Число. id типа ],
        "description": "Строка.",
        "project": Обязательное поле. Число. id проекта
    }

Изменение задачи  
method: PATCH  
url: http://host/api/tasks/<id задачи>/ 

    {
        "summary": " Строка. Максимум 100 символов",
        "status": Число. id статуса,
        "type": [ Список. Число. id типа ],
        "description": "Строка.",
        "project":  Число. id проекта
    }

Удаление задачи  
method: DELETE  
url: http://host/api/tasks/<id задачи>/


Проекты

Список проектов  
method: GET  
url: http://host/api/projects/
    
    {
        "id": id Проекта,
        "name": "Имя проекта",
        "created_at": "Дата начала проекта",
        "completed_at": "Дата окончания проекта"
    },

Детали проекта  
method: GET  
url: http://host/api/projects/<id Проекта>
    
    {
        "id": id Проекта,
        "name": "Имя проекта",
        "description": "Описание поекта",
        "created_at": "Дата начала проекта",
        "completed_at": "Дата окончания проекта",
        "tasks": [ список привязаных задач
            {
                "id": id задачи,
                "summary": "Название задачи"
            },
        ]
    }
    
Создание проекта  
method: POST  
url: http://host/api/projects/

    {
        "name": "Обязательное поле. Строка. Максимум 50 символов",
        "description":"Обязательное поле. Срока. Максимум 3000 символов",
        "created_at": "Обязательное поле. Строка. Формат даты YYYY-MM-DD"
        "completed_at": "Строка. Формат даты YYYY-MM-DD"
    }

Изменение проекта  
method: PUT  
url: http://host/api/projects/<id Проекта>

    {
        "name": "Обязательное поле. Строка. Максимум 50 символов",
        "description":"Обязательное поле. Срока. Максимум 3000 символов",
        "created_at": "Обязательное поле. Строка. Формат даты YYYY-MM-DD"
        "completed_at": "Строка. Формат даты YYYY-MM-DD"
    }


Изменение проекта  
method: PATCH  
url: http://host/api/projects/<id Проекта>

    {
        "name": "Строка. Максимум 50 символов",
        "description":"Срока. Максимум 3000 символов",
        "created_at": "Строка. Формат даты YYYY-MM-DD"
        "completed_at": "Строка. Формат даты YYYY-MM-DD"
    }


Удаление проекта  
method: DELETE  
url: http://host/api/projects/<id Проекта>


Статусы  
Список статусов  
method: GET  
url: http://host/api/statuses/

    {
        "id": id статуса,
        "name": "Название статуса"
    },


Детали статуса  
method: GET  
url: http://host/api/statuses/<id статуса>

    {
        "id": id статуса,
        "name": "Название статуса"
    },

Добавление статуса 
method: POST  
url: http://host/api/statuses/

    {
        "name": "Обязательное поле. Строка. Максимум 20 символов"
    },

Изменения статуса 
method: PUT  
url: http://host/api/statuses/<id статуса>

    {
        "name": "Обязательное поле. Строка. Максимум 20 символов"
    },

Изменения статуса 
method: PATCH  
url: http://host/api/statuses/<id статуса>

    {
        "name": "Строка. Максимум 20 символов"
    },

Удаление статуса  
method: DELETE  
url: http://host/api/statuses/<id статуса>


Типы  
Список типов  
method: GET  
url: http://host/api/types/

    {
        "id": id типа,
        "name": "Название типа"
    },


Детали типа  
method: GET  
url: http://host/api/types/<id типа>

    {
        "id": id типа,
        "name": "Название типа"
    },

Добавление типа 
method: POST  
url: http://host/api/types/

    {
        "name": "Обязательное поле. Строка. Максимум 20 символов"
    },

Изменения типа 
method: PUT  
url: http://host/api/types/<id типа>

    {
        "name": "Обязательное поле. Строка. Максимум 20 символов"
    },

Изменения типа 
method: PATCH  
url: http://host/api/types/<id типа>

    {
        "name": "Строка. Максимум 20 символов"
    },

Удаление типа  
method: DELETE  
url: http://host/api/types/<id типа>









