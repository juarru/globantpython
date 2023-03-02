# globantpython
Juan Arillo challenge for globant

## Requirements
Install docker in the machine, the service is ready to be deployed in a docker container.

## Steps
- Download this repository.  
- With docker running on your machine, execute `docker build -t globant .` in a terminal.  
- Then execute `docker run -d --name globantcontainer -p 80:80 globant` .  
- Now the service is running in port 80.  
- Try on the terminal `curl --location 'localhost:80/api/v1/weather?city=Bogota&country=co'` or, using an application like Postman `localhost:80/api/v1/weather?city=Bogota&country=co`

## Run tests
- Open the terminal.  
- Execute `docker exec -ti globantcontainer /bin/sh` .  
- Then execute `pytest`

## Other considerations
- Added the .env file, what shouldn´t be done (just for doing things easy).

## SQL Challenge
Find top two salary for each department.  
Table: Employees  
Columns: Name, Salary, DepartmentID  

```sql
    select * from Employees 
             where id = (select top 2 Salary from Employees 
                                        where DepartmentID = DepartmentID 
                                        order by Salary desc)
```
