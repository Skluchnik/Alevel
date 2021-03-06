
/*Задача 1
Создать таблицу, выдающую следующее:

select * from users;

1 | m      | Vasya  | mmm@mail.com
2 | m      | Alex   | mmm@gmail.com
3 | m      | Alexey | alexey@gmail.com
4 | f      | Helen  | hell@gmail.com
5 | f      | Jenny  | eachup@gmail.com
6 | f      | Lora   | tpicks@gmail.com
*/
create table contacts  (id serial, sex VARCHAR(1), name varchar(25), email varchar(254));

/* Заполняем таблицу*/
insert into contacts (id, sex, name, email) values (0, 'm', 'Vasya', 'vasya@example.com'), (1, 'm', 'Alex', 'alex@example.com'), 
 (2, 'm', 'Alexey', 'alexey@example.com'), (3, 'f', 'Helen', 'helen@example.com'), (0, 'f', 'Jenny', 'jenny@example.com');

/* Задача 2
Получить результат вида:
We have 3 boys!
We have 3 girls!
*/
select concat('We have ', count(*), case when sex = 'm' then ' boys!' else ' girls!' end) from contacts group by sex;

/*
Задача 3:

Получить результат вида:

This is Vasya, he has email mmm@mail.com
This is Alex, he has email mmm@gmail.com
This is Alexey, he has email alexey@gmail.com
This is Helen, she has email hell@gmail.com
This is Jenny, she has email eachup@gmail.com
This is Lora, she has email tpicks@gmail.com
*/
select concat('This is ', name, ' ', case when sex = 'f' then 's' else '' end, 'he has email ', email) from contacts;



