class VitamineAsosRoutine:
    def __init__(self, updateFreq="", updateVitType="", type="", frequency=""):
        self.frequency = frequency
        self.type = type
        self.updateVitType = updateVitType
        self.updateFreq = updateFreq

    # routine for asos's vitamine
    def display_frequency(self):
        return self.frequency
    # vitamine type
    def vitamine_type(self):
        return self.type
    # update vitamine type
    def update_vitamine_type(self):
        return self.updateVitType
    # update frequency
    def update_frequency(self):
        return self.updateFreq

# Create an instance of vitamine's routine
routine = VitamineAsosRoutine(updateFreq="", updateVitType="", type="", frequency="mornings")
print(routine.display_frequency())
# print(routine.vitamine_type())
# print(routine.update_vitamine_type())
# print(routine.update_frequency())
