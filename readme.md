Useful when you need a relation between users

user.following = [User(...), ...]

An association table is needed in order to avoid a circular dependency.

results:

ddssvvaa.following = [<User(id=11, username='Alejandra Saldaña, following=[<User(id=12, username='Simón Vera, following=[<User(id=10, username='David Vera, following=[...]')>]')>]')>]

enf_alejandra.following = [<User(id=12, username='Simón Vera, following=[<User(id=10, username='David Vera, following=[<User(id=11, username='Alejandra Saldaña, following=[...]')>]')>]')>]

itaroki.following = [<User(id=10, username='David Vera, following=[<User(id=11, username='Alejandra Saldaña, following=[<User(id=12, username='Simón Vera, following=[...]')>]')>]')>]