class VitamineAsosRoutine:
    # If no value is provided for the parameters then the default values are empty strings.
    def __init__(self, updateFreq="", updateVitType="", type="", frequency=""):
        self.frequency = frequency
        self.type = type
        self.updateVitType = updateVitType
        self.updateFreq = updateFreq
    # The self keyqord is used to access the attributes and methods of the class, the object we are creating. 
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
routine = VitamineAsosRoutine(frequency="mornings")
print(routine.display_frequency())
vit_type = VitamineAsosRoutine(type="Vitamine C")
print(routine.vitamine_type())
# print(routine.update_vitamine_type())
# print(routine.update_frequency())
