class VitamineAsosRoutine:
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
routine = VitamineAsosRoutine("mornings")
# print(routine.display_routine())
type = VitamineAsosRoutine("D3")
# print(type.vitamine_type())
update_VitaminType = VitamineAsosRoutine("B12")
# print(update_VitaminType.update_vitamine_type())
updateFrequency = VitamineAsosRoutine("evenings")
print(updateFrequency.update_frequency())
