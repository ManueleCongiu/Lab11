from database.DAO import DAO

prod = DAO.getProducts()

print(len(prod))
color = []
for c in prod:
    if c.Color() == "Silver":
        color.append(c._Product)

print(color)
