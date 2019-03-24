import matlab.engine


class SolarWindClassifier:
    def __init__(self, path):
        self.data_path = path

    def classify(self):
        eng = matlab.engine.start_matlab('-novm')
        result = eng.classify_solar_wind(self.data_path)
        eng.quit()
        # f = open("./result.dat","w")
        # f.write(result)
        # f.close()


S = SolarWindClassifier("./matlab/omni2_2017.dat")
S.classify()






