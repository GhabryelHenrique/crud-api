# CRUD API For Training Requests

I created this api for my coworkers training http requests in Angular

# Documentation

This API use the simple concept:

- Create data and save in database
- Read data and return then for the user
- Update data and save in database
- Delete data from the database

### /create

Create new user in the database

 methods: POST
 <br>
 
 body: {<br>
    first_name: string<br>
    last_name: string<br>
    company: string<br>
    address: string<br>
    city: string<br>
    state: string<br>
    country: string<br>
    postal_code: string<br>
    phone: string<br>
    email: string<br>
    fax: string<br>
}

### /reed

Return all users

 methods: GET
 
### /delete/:id 

Delete data from database based on id

metheos: DELETE <br>
id: integer
