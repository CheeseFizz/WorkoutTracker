# for classes related to data objects

class Exercise():

    def __init__(self, name, equipment):
        self.name = name
        self.equipment = equipment 

class ExerciseSet():

    def __init__(self, exercise, reps, weight, set_index):
        self.exercise = exercise
        self.reps = reps
        self.weight = weight

    def _getMax(self):
        #get recorded max for set number
        pass

    def _setMax(self):
        #set recorded max for set number
        pass

class ExerciseBlock():
    
    def __init__(self, exercise, description="", tags=set()):
        self.exercise = exercise
        self.description = description
        self.tags = tags
        self.sets = []

    def addSet(self, reps, weight):
        new_index = len(self.sets)
        self.sets.append(
            ExerciseSet(self.exercise, reps, weight, new_index)
        )

    def removeSet(self, index):
        ignore = self.sets.pop(index)

    def setDescription(description):
        self.description = description

    def addTag(tag):
        self.tags.add(tag)

    def removeTag(tag):
        self.tags.remove(tag)


class WorkoutPlan():

    def __init__(self, name, tags):
        self.name = name
        self.tags = tags
        self.exercise_blocks = []

    def addExerciseBlock(self, exercise):
        self.exercise_blocks.append(
            ExerciseBlock(exercise)
        )

    def removeExerciseBlock(self, index):
        ignore = self.exercise_blocks.pop(index)

    def exportText(self, outfile):
        # some file safety stuff

        # build string

        with open(outfile,'w') as f:
            pass
            #write to file
            
        
        
    