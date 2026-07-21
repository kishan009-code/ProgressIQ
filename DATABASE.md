User Table(login page)

columns       data type          constraints
name          varchar             not null
age            int                not null
height         float             not null
weight         float             not null
password       varchar            not null
goal           varchar            not null   
user-id        int                 primary key
email          varchar            not null,unique

workout log(depends on user)

coulmns           data type 
workout_id            int
user_id              int 
date                date
workout_name        varchar

Excercise log(user based)

columns                              data type
excercise_id                           int 
workout_name                           varchar
weight                                 int
sets                                   int
reps                                   int
pr attempt                             int 

nutrition log

columns(calorie/protein)      data type
food_id                        int
food_name                      varchar
calories                        int
protein                          int


pr table                 data type
pr_id                      int 
user_id                    int 
exercise                   varchar
weight                     int
reps                        int
date                       date


body progress

column                  data type
user_id                    int
weight                     float
date                       date