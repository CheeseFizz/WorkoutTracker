# for classes related to data objects

import datetime
import os
import json

class Exercise():

    def __init__(self, name, equipment):
        self.name = name
        self.equipment = equipment 
        rootdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
        datadir = os.path.join(rootdir, "data")
        filename = f"e_{self.name.replace(" ", "")}_{self.equipment.replace(" ","")}.json"
        if not os.path.exists(datadir):
            os.mkdir(datadir)
        self.filepath = os.path.join(datadir, filename)
        self._load() # sets self.data

    def __repr__(self):
        return f"{self.equipment} {self.name}"

    def __eq__(self, other):
        return (self.name == other.name and self.equipment == other.equipment)

    def _save(self):
        with open(self.filepath, "w") as f:
            json.dump({
                "name": self.name,
                "equipment": self.equipment,
                "data": self.data
            },f, indent=4)

    def _load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                jsonobj = json.load(f)
            if (self.name != jsonobj['name']) or (self.equipment != jsonobj['equipment']):
                raise ValueError(f"Invalid data loaded for {self.__repr__()} from file: {self.filepath}")
            self.data = jsonobj['data']
        else:
            self.data = {
                "weightmax": dict(),
                "repmax": dict(),
                "history": dict()
            }

    def _serialize(self):
        return {
            "name": self.name,
            "equipment": self.equipment
        }

    def _getMax(self, target, reps, weight, units):
        if target.lower() == "weight":
            try:
                return self.data["weightmax"][f"{reps}reps"]
            except KeyError:
                return None
        if target.lower() == "reps":
            try:
                return self.data["repmax"][f"{weight}{units}"]
            except KeyError:
                return None

    def _setMax(self, target, reps, weight, units):
        if target.lower() == "weight":
            self.data["weightmax"][f"{reps}reps"] = weight
        if target.lower() == "reps":
            self.data["repmax"][f"{weight}{units}"] = reps

    def _gtMax(self, target, reps, weight, units):
        current = self._getMax(target, reps, weight, units)
        if not current:
            return True

        if target.lower() == "weight":
            if weight > current:
                return True
            return False
            
        if target.lower() == "reps":
            if reps > current:
                return True
            return False
            
    def _getHistory(self, date, setnum=0):
        try:
            datestr = date.isoformat().replace("-","")
            return self.data['history'][datestr][f"set{setnum}"]
        except KeyError:
            return None

    def _setHistory(self, date, setnum, target, reps, weight, units):
        datestr = date.isoformat().replace("-","")
        if datestr not in self.data['history'].keys():
            self.data['history'][datestr] = dict()
        self.data['history'][datestr][f"set{setnum}"] = {
            "target": target,
            "reps": reps,
            "weight": weight,
            "units": units
            }

class ExerciseSet():

    def __init__(self, exercise, reps, weight, set_index, units="lbs", target="reps"):
        self.exercise = exercise
        self.reps = reps
        self.weight = weight
        self.units = units
        self.set_index = set_index
        self.target = target

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

    def copy(self):
        return ExerciseSet(self.exercise, self.reps, self.weight, self.set_index, self.units, self.target)

    def _print(self):
        return f"{self.reps} @ {self.weight}{self.units}"

    def _serialize(self):
        serialdict = {
            "exercise": self.exercise._serialize(),
            "reps": self.reps,
            "weight": self.weight,
            "units": self.units,
            "set_index": self.set_index,
            "target": self.target
        }
        return serialdict

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
        self.complete_sets = []

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
        rstring = f"{self.exercise.__repr__().title()}:\nTags: {", ".join(self.tags)}\n"
        for s in self.sets:
            rstring += f"{s._print()}\n"
        rstring += "\n"

        return rstring

    def _serialize(self):
        # return class data as dictionary
        serialdict = {
            "exercise": self.exercise._serialize(),
            "description": self.description,
            "tags": sorted(list(self.tags)),
            "sets": []
        }
        for s in self.sets:
            serialdict['sets'].append(s._serialize())
        
        return serialdict

    def _fromData(data):
        new_block = ExerciseBlock(
            Exercise(data["exercise"]["name"], data["exercise"]["equipment"]), 
            data["description"], 
            set(data["tags"])
            )
        i = 0
        for sdata in data["sets"]:
            s = ExerciseSet(
                new_block.exercise,
                sdata["reps"],
                sdata["weight"],
                i,
                sdata["units"],
                sdata["target"]
                )
            new_block.sets.append(s)
            i += 1
        return new_block

    def copy(self):
        new_block = ExerciseBlock(self.exercise, self.description, self.tags.copy())
        for s in self.sets:
            new_block.sets.append(s.copy())
        return new_block

    def addSet(self, reps, weight):
        new_index = len(self.sets)
        self.sets.append(
            ExerciseSet(self.exercise, reps, weight, new_index)
        )
        self.complete_sets.append(False)

    def removeSet(self, index):
        ignore = self.sets.pop(index)

    def _completeSet(self, index):
        self.complete_sets[index] = True

    def clearSetData(self):
        for s in self.sets:
            s.weight = 0
            s.reps = 0

    def setDescription(description):
        self.description = description

    def addTag(tag):
        self.tags.add(tag)

    def removeTag(tag):
        self.tags.remove(tag)


class WorkoutPlan():

    def __init__(self, name, tags=set(), description=""):
        self.name = name
        self.tags = tags
        self.description = description
        self.exercise_blocks = []
        self.actuals = []

        rootdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
        datadir = os.path.join(rootdir, "data")
        filename = f"wp_{self.name}.json"
        if not os.path.exists(datadir):
            os.mkdir(datadir)
        self.filepath = os.path.join(datadir, filename)

    def __repr__(self):
        return f"[WorkoutPlan] {self.name}: {len(self.exercise_blocks)} exercises; {len(tags)} tags"

    def __eq__(self, other):
        if (
            self.name == other.name and
            self.tags == other.tags and
            self.description == other.description and
            self.exercise_blocks == other.exercise_blocks and
            self.actuals == other.actuals
            ):
            return True
        return False

    def _print(self):
        # hline = "-"*os.get_terminal_size()[0]   doesn't work nice; try again later
        rstring = f"{self.name.title()}\n\n{self.description}\n\n"
        for block in self.exercise_blocks:
            rstring += f"{block._print()}"

        return rstring
        
    def addExerciseBlock(self, exercise_block):
        self.exercise_blocks.append(
            #ExerciseBlock(exercise) maybe come back to this idea later
            exercise_block
        )
        self.actuals.append(
            exercise_block.copy()
        )
        self.actuals[-1].clearSetData()

    def removeExerciseBlock(self, index):
        ignore = self.exercise_blocks.pop(index)

    def _setActual(self, block_index, set_index, weight, reps):
        self.actuals[block_index].sets[set_index].weight = weight
        self.actuals[block_index].sets[set_index].reps = reps

    def completeSet(self, block_index, set_index, weight, reps):
        self._setActual(block_index, set_index, weight, reps)
        self.exercise_blocks[block_index]._completeSet(set_index)

    def saveResults(self):
        today = datetime.date.today()
        i = 0
        for eb in self.actuals:
            n = 0
            for s in eb.sets:
                if not (self.exercise_blocks[i].complete_sets[n]):
                    n += 1
                    continue
                if s.exercise._gtMax(s.target, s.reps, s.weight, s.units):
                    s.exercise._setMax(s.target, s.reps, s.weight, s.units)
                s.exercise._setHistory(today, s.set_index, s.target, s.reps, s.weight, s.units)
                n += 1
            s.exercise._save()
            i += 1
        self._save(self.filepath)

    def exportText(self, outfile):
        # some file safety stuff
        parentdir = os.path.join(os.path.dirname(os.path.realpath(outfile)), os.pardir)
        if not os.path.exists(parentdir):
            raise FileNotFoundError(f"directory does not exist: {parentdir}")

        # build string
        extext = self._print()

        with open(outfile,'w') as f:
            f.write(extext)
            #write to file

    def _serialize(self):
        serialdict = {
            "name": self.name,
            "description": self.description,
            "tags": sorted(list(self.tags)),
            "exercise_blocks": [],
            "actuals": []
        }
        for block in self.exercise_blocks:
            serialdict["exercise_blocks"].append(block._serialize())
        for block in self.actuals:
            serialdict["actuals"].append(block._serialize())


        return serialdict

    def _save(self, filepath=None):
        serialdict = self._serialize()
        if not filepath:
            filepath = self.filepath
        with open(filepath, 'w') as f:
            json.dump(serialdict, f, indent=4)

    def _load(self, from_actuals=False, filepath=None):
        if not filepath:
            filepath = self.filepath
        with open(filepath, 'r') as f:
            data = json.load(f)
        self.name = data["name"]  # this is typically redundant, but would support an import use case
        self.description = data["description"]
        self.tags = set(data["tags"])

        if from_actuals:
            for bdata in data["actuals"]:
                self.exercise_blocks.append(ExerciseBlock._fromData(bdata))
                self.actuals.append(ExerciseBlock._fromData(bdata))
                self.actuals[-1].clearSetData()
        else:
            for bdata in data["exercise_blocks"]:
                self.exercise_blocks.append(ExerciseBlock._fromData(bdata))
            for bdata in data["actuals"]:
                self.actuals.append(ExerciseBlock._fromData(bdata))
            
            
        
        
    