highway_cons = float(input('Kérem adja meg az országúti fogyasztást (l / 100 km) = '))
city_cons = float(input('Kérem adja meg a városi fogyasztást (l / 100 km) = '))
highway_dist = int(input('Kérem adja meg az országúton megtett utat odafelé (km) = '))
city_dist = int(input('Kérem adja meg a városban megtett utat odafelé (km) = '))
fuel_cost = int(input('Kérem adja meg a benzin árát (Ft / l) = '))

one_way_cons = (highway_dist * highway_cons / 100) + (city_dist * city_cons / 100)

print()
print('Az autó fogyasztása csak oda = ', one_way_cons, 'l')
print('Az autó fogyasztása oda-vissza = ', 2 * one_way_cons, 'l')
print('A teljes utiköltség = ', 2 * one_way_cons * fuel_cost, 'Ft')
