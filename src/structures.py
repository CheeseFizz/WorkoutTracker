# for classes related to data objects

from os import get_terminal_size

class Exercise():

    def __init__(self, name, equipment):
        self.name = name
        self.equipment = equipment 

    def __repr__(self):
        return f"{self.equipment} {self.name}"

    def __eq__(self, other):
        return (self.name == other.name and self.equipment == other.equipment)

class ExerciseSet():

    def __init__(self, exercise, reps, weight, set_index, units="lbs"):
        self.exercise = exercise
        self.reps = reps
        self.weight = weight
        self.units = units
        self.set_index = set_index

    def __repr__(self):
        return f"[ExerciseSet] {self.exercise}: {self.reps} @ {self.weight}{self.units}"

    def __eq__(self, other):
        if (
            self.exercise == other.exercise and
            self.reps == other.reps and
            self.weight == other.weight and
            self.units == other.units
            ):
            return True
        return False

    def _print(self):
        return f"{self.reps} @ {self.weight}{self.units}"

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

    def __repr__(self):
        return f"[ExerciseBlock] {self.exercise}: {self.description[0:10]}... {len(self.sets)} sets; {len(self.tags)} tags"

    def __eq__(self, other):
        if (
            self.exercise == other.exercise and
            self.description == other.description and
            self.tags == other.tags and
            self.sets == other.sets
            ):
            return True
        return False

    def _print(self):
        rstring = f"{self.exercise.title()}:`nTags: {", ",join(self.tags)}"
        for s in sets:
            rstring += f"{s._print()}'n"
        rstring += "`n"

        return rstring

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

    def __repr__(self):
        return f"[WorkoutPlan] {self.name}: {len(self.exercise_blocks)} exercises; {len(tags)} tags"

    def _print(self):
        hline = "-"*get_terminal_size()[0]
        rstring = f"{self.name.title()}`n`n{self.description}`n {hline}`n`n"
        for block in self.exercise_blocks:
            rstring += f"{block._print}`n`n"

        return rstring
        

    def addExerciseBlock(self, exercise_block):
        self.exercise_blocks.append(
            #ExerciseBlock(exercise) maybe come back to this idea later

            exercise_block
        )

    def removeExerciseBlock(self, index):
        ignore = self.exercise_blocks.pop(index)

    def exportText(self, outfile):
        # some file safety stuff

        # build string
        extext = self._print()

        with open(outfile,'w') as f:
            f.write(extext)
            #write to file
            
        
        
    