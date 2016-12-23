from data_science.wine_data import RedWineData


red_wine = RedWineData()
red_wine.extract_data()
print(red_wine.get_shape())
