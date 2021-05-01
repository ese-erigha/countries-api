const db_user = 'app_user';
const count = db.system.users.find({user: db_user}).count();
if(count === 0){
    db.createUser({
        user: db_user,
        pwd: 'moNGO7135..',
        roles: [
            {
                role: 'dbOwner',
                db: 'countries_dev',
            },
        ],
    });
}