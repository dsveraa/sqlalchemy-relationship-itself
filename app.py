from models import session, User

# creating users
ddssvvaa = User(username="David Vera")
enf_alejandra = User(username="Alejandra Saldaña")
itaroki = User(username="Simón Vera")


# creating relationships
ddssvvaa.following.append(enf_alejandra)
enf_alejandra.following.append(itaroki)
itaroki.following.append(ddssvvaa)

# adding users to the session and committing changes to the database
session.add_all([ddssvvaa, enf_alejandra, itaroki])
session.commit()

print(f"{ddssvvaa.following = }")
print(f"{enf_alejandra.following = }")
print(f"{itaroki.following = }")
