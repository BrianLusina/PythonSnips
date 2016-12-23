from data_science.wine_data import RedWineData


red_wine = RedWineData()
data = red_wine.extract_data()
print(data[2, 3])

