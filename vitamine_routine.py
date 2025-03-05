class vitamineAsosRoutine:
    def __init__(self, updateFreq="", updateVitType="", type="", frequency=""):
        self.frequency = frequency
        self.type = type
        self.updateVitType = updateVitType
        self.updateFreq = updateFreq

    # routine for asos's vitamine
    def display_routine(self):
        print("How many times a day Asos wants his vitamine?")
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
routine = vitamineAsosRoutine("mornings")
# print(routine.display_routine())
type = vitamineAsosRoutine("D3")
# print(type.vitamine_type())
update_VitaminType = vitamineAsosRoutine("B12")
# print(update_VitaminType.update_vitamine_type())
updateFrequency = vitamineAsosRoutine("evenings")
print(updateFrequency.update_frequency())
