import unittest
from structures import *

class TestWorkoutPlan(unittest.TestCase):
    
    def testWorkoutPlan(self):
        plan = WorkoutPlan("test plan", set(["test", "tag", "plan"]))
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        ex2 = Exercise("Test2", "Computer")
        block2 = ExerciseBlock(ex2, "Second test block", set(["test", "block2"]))
        block2.addSet(12, 20)
        block2.addSet(12, 25)
        block2.addSet(10, 30)

        plan.addExerciseBlock(block1)
        plan.addExerciseBlock(block2)

        
        self.assertEqual(len(plan.exercise_blocks), 2)
        self.assertEqual(len(plan.tags), 3)

    def testEqWorkoutPlan(self):
        plan1 = WorkoutPlan("test plan", set(["test", "tag", "plan"]))
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        ex2 = Exercise("Test2", "Computer")
        block2 = ExerciseBlock(ex2, "Second test block", set(["test", "block2"]))
        block2.addSet(12, 20)
        block2.addSet(12, 25)
        block2.addSet(10, 30)

        plan1.addExerciseBlock(block1)
        plan1.addExerciseBlock(block2)

        plan2 = WorkoutPlan("test plan", set(["test", "tag", "plan"]))
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        ex2 = Exercise("Test2", "Computer")
        block2 = ExerciseBlock(ex2, "Second test block", set(["test", "block2"]))
        block2.addSet(12, 20)
        block2.addSet(12, 25)
        block2.addSet(10, 30)

        plan2.addExerciseBlock(block1)
        plan2.addExerciseBlock(block2)

        self.assertEqual(plan1, plan2)

    def testRemoveExerciseBlock(self):
        plan = WorkoutPlan("test plan", set(["test", "tag", "plan"]))
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        ex2 = Exercise("Test2", "Computer")
        block2 = ExerciseBlock(ex2, "Second test block", set(["test", "block2"]))
        block2.addSet(12, 20)
        block2.addSet(12, 25)
        block2.addSet(10, 30)

        plan.addExerciseBlock(block1)
        plan.addExerciseBlock(block2)

        self.assertEqual(len(plan.exercise_blocks), 2)

        plan.removeExerciseBlock(1)
        
        self.assertEqual(len(plan.exercise_blocks), 1)
        self.assertEqual(plan.exercise_blocks[0], block1)

    def testSerializeExercise(self):
        ex1 = Exercise("Test", "Computer")
        actual = ex1._serialize()

        expected = {
            "name": "Test",
            "equipment": "Computer"
        }

        self.assertEqual(expected, actual)

    def testSerializeExerciseSet(self):
        ex1 = Exercise("Test", "Computer")
        s1 = ExerciseSet(ex1, 12, 40, 1)

        actual = s1._serialize()

        expected = {
            "exercise": ex1._serialize(),
            "reps": 12,
            "weight": 40,
            "units": "lbs",
            "set_index": 1,
            "target": "reps"
        }

        self.assertEqual(expected, actual)

    def testSerializeExerciseBlock(self):
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        actual = block1._serialize()

        expected = {
            "exercise": ex1._serialize(),
            "description": "A test block",
            "tags": sorted(["test","tag", "block"]),
            "sets": [
                {
                    "exercise": ex1._serialize(),
                    "reps": 10,
                    "weight": 25,
                    "units": "lbs",
                    "set_index": 0,
                    "target": "reps"
                },
                {
                    "exercise": ex1._serialize(),
                    "reps": 10,
                    "weight": 35,
                    "units": "lbs",
                    "set_index": 1,
                    "target": "reps"
                }
            ]
        }

        self.maxDiff = None

        self.assertEqual(expected, actual)

    def testSerializeWorkoutPlan(self):
        plan = WorkoutPlan("test plan", set(["test", "tag", "plan"]))
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        ex2 = Exercise("Test2", "Computer")
        block2 = ExerciseBlock(ex2, "Second test block", set(["test", "block2"]))
        block2.addSet(12, 20)
        block2.addSet(12, 25)
        block2.addSet(10, 30)

        plan.addExerciseBlock(block1)
        plan.addExerciseBlock(block2)

        copyblock1 = block1.copy()
        copyblock2 = block2.copy()
        copyblock1.clearSetData()
        copyblock2.clearSetData()

        actual = plan._serialize()

        expected = {
            "name": "test plan",
            "tags": sorted(["test", "tag", "plan"]),
            "description": "",
            "exercise_blocks": [
                block1._serialize(),
                block2._serialize()
            ],
            "actuals": [
                copyblock1._serialize(),
                copyblock2._serialize()
            ]
        }


        self.maxDiff = None
        self.assertEqual(expected, actual)
    
    def testPrintExerciseSet(self):
        ex1 = Exercise("Test", "Computer")
        s1 = ExerciseSet(ex1, 12, 40, 1)

        actual = s1._print()

        expected = f"{s1.reps} @ {s1.weight}{s1.units}"

        self.assertEqual(expected, actual)

    def testPrintExerciseBlock(self):
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        actual = block1._print()

        expected = f"{block1.exercise.__repr__().title()}:\nTags: {", ".join(block1.tags)}\n{block1.sets[0]._print()}\n{block1.sets[1]._print()}\n\n"

        self.maxDiff = None
        self.assertEqual(expected, actual)

    def testPrintWorkoutPlan(self):
        plan = WorkoutPlan("test plan", set(["test", "tag", "plan"]))
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        ex2 = Exercise("Test2", "Computer")
        block2 = ExerciseBlock(ex2, "Second test block", set(["test", "block2"]))
        block2.addSet(12, 20)
        block2.addSet(12, 25)
        block2.addSet(10, 30)

        plan.addExerciseBlock(block1)
        plan.addExerciseBlock(block2)

        actual = plan._print()

        # hline = "-"*os.get_terminal_size()[0]   doesn't work nice; try again later
        expected = f"{plan.name.title()}\n\n{plan.description}\n\n{block1._print()}{block2._print()}"
        
        self.maxDiff = None
        self.assertEqual(expected, actual)

    def testExportTextWorkoutPlan(self):
        plan = WorkoutPlan("test plan", set(["test", "tag", "plan"]))
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        ex2 = Exercise("Test2", "Computer")
        block2 = ExerciseBlock(ex2, "Second test block", set(["test", "block2"]))
        block2.addSet(12, 20)
        block2.addSet(12, 25)
        block2.addSet(10, 30)

        plan.addExerciseBlock(block1)
        plan.addExerciseBlock(block2)

        plan.exportText("/home/cheese/BootDev/projects/WorkoutTracker/tests/testplan.txt")

        self.assertTrue(os.path.exists("/home/cheese/BootDev/projects/WorkoutTracker/tests/testplan.txt"))
        self.assertRaises(FileNotFoundError, plan.exportText, "/home/cheese/BootDev/projects/WorkoutTracker/notreal/testplan.txt")

    def testClearSetDataExerciseBlock(self):
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        self.maxDiff = None

        block1.clearSetData()

        expected = ExerciseSet(ex1, 0, 0, 0)
        actual = block1.sets[0]

        self.assertEqual(expected, actual)

    def testCopyExerciseBlock(self):
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        self.maxDiff = None


        block2 = block1.copy()
        self.assertEqual(block1, block2)
        
        block2.clearSetData()
        self.assertNotEqual(block1.sets[0], block2.sets[0])

    def testSaveWorkoutPlan(self):
        plan = WorkoutPlan("test plan", set(["test", "tag", "plan"]))
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        ex2 = Exercise("Test2", "Computer")
        block2 = ExerciseBlock(ex2, "Second test block", set(["test", "block2"]))
        block2.addSet(12, 20)
        block2.addSet(12, 25)
        block2.addSet(10, 30)

        plan.addExerciseBlock(block1)
        plan.addExerciseBlock(block2)

        plan._save()
        rootdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
        datadir = os.path.join(rootdir, "data")
        filename = f"wp_{plan.name}.json"
        filepath = os.path.join(datadir, filename)

        exists = os.path.exists(filepath)
        self.assertTrue(exists)

        testdir = os.path.join(rootdir, "tests")
        filename = f"wp_{plan.name}.json"
        filepath = os.path.join(testdir, filename)
        plan._save(filepath)
        exists = os.path.exists(filepath)
        self.assertTrue(exists)

    def testLoadWorkoutPlan(self):
        plan1 = WorkoutPlan("test plan2", set(["test", "tag", "plan"]))
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        ex2 = Exercise("Test2", "Computer")
        block2 = ExerciseBlock(ex2, "Second test block", set(["test", "block2"]))
        block2.addSet(12, 20)
        block2.addSet(12, 25)
        block2.addSet(10, 30)

        plan1.addExerciseBlock(block1)
        plan1.addExerciseBlock(block2)

        plan1._save()

        plan2 = WorkoutPlan("test plan2")
        plan2._load()

        self.assertEqual(plan1.exercise_blocks[0].sets[0], plan2.exercise_blocks[0].sets[0])
        self.assertEqual(plan1.exercise_blocks, plan2.exercise_blocks)
        self.assertEqual(plan1.tags, plan2.tags)
        self.assertEqual(plan1.actuals, plan2.actuals)

        self.assertEqual(plan1, plan2)

    
    def testSetActualWorkoutPlan(self):
        plan = WorkoutPlan("test plan", set(["test", "tag", "plan"]))
        ex1 = Exercise("Test", "Computer")
        block1 = ExerciseBlock(ex1, "A test block", set(["test","tag", "block"]))
        block1.addSet(10, 25)
        block1.addSet(10,35)

        ex2 = Exercise("Test2", "Computer")
        block2 = ExerciseBlock(ex2, "Second test block", set(["test", "block2"]))
        block2.addSet(12, 20)
        block2.addSet(12, 25)
        block2.addSet(10, 30)

        plan.addExerciseBlock(block1)
        plan.addExerciseBlock(block2)

        plan._setActual(0, 0, 25, 9)

        actual = plan.actuals[0].sets[0]

        expected = ExerciseSet(ex1, 9, 25, 0)

        self.assertEqual(expected, actual)